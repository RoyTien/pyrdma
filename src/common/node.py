# const
import pyverbs.cm_enums as ce
import pyverbs.enums as e
# config
import src.config.config as c
# common
from src.common.connection import Connection
# pyverbs
from pyverbs.device import Context
from pyverbs.cmid import CMID, AddrInfo, CMEventChannel
from pyverbs.qp import QPInitAttr, QPCap, QP, QPAttr
from pyverbs.wr import RecvWR, SGE
from pyverbs.cq import CompChannel, CQ
from pyverbs.pd import PD


# a common node for server or client

class Node:
    def __init__(self, addr, port, name, is_server=False, options=c.OPTIONS):
        self.options = options
        self.is_server = is_server
        if is_server:
            self.addr_info = AddrInfo(src=addr, service=port, port_space=ce.RDMA_PS_TCP, flags=ce.RAI_PASSIVE)
            print(ce.RDMA_PS_TCP, ce.RAI_PASSIVE)
        else:
            self.addr_info = AddrInfo(src=addr, dst=addr, service=port, port_space=ce.RDMA_PS_TCP)
        # cmid
        self.event_channel = CMEventChannel()
        self.cid = CMID(creator=self.event_channel)
        self.pd = None
        self.comp_channel = None
        self.cq = None
        self.event = None
        self.qp = None
        self.conn = None

    # if a server, here cmid is an event id; if a client, here cmid is it's cid
    def prepare_resource(self, cmid):
        # pd, comp_channel, cq, qp

        # protection domains
        self.pd = PD(cmid.context)
        # comp_channel cq
        self.comp_channel = CompChannel(cmid.context)
        cqe = self.options.get("cq_init").get("cqe")
        self.cq = CQ(cmid.context, cqe, None, self.comp_channel, 0)
        self.cq.req_notify()

        # build_qp_attr
        qp_options = self.options.get("qp_init")
        cap = QPCap(max_send_wr=qp_options.get("max_send_wr"), max_recv_wr=qp_options.get("max_recv_wr"),
                    max_send_sge=qp_options.get("max_send_sge"), max_recv_sge=qp_options.get("max_recv_sge"))
        qp_init_attr = QPInitAttr(qp_type=qp_options.get("qp_type"), qp_context=cmid.context,
                                  cap=cap, scq=self.cq, rcq=self.cq)

        # create_qp and bind in cmid
        cmid.create_qp(qp_init_attr)
        self.conn = Connection(pd=self.pd)
        cmid.post_recv(self.conn.recv_mr)

        # create_qp alone
        # qp_attr = QPAttr(qp_state=e.IBV_QPT_RC)
        # QP
        # self.qp = QP(self.pd, qp_init_attr, qp_attr)
        # sge = SGE(addr=id(self.conn.recv_region), length=c.BUFFER_SIZE, lkey=self.conn.recv_mr.lkey)
        # wr = RecvWR(num_sge=1, sg=[sge])
        # self.qp.post_recv(wr)

    def process_work_completion_events(self):
        print(1)
        self.comp_channel.get_cq_event(self.cq)
        print(2)
        self.cq.req_notify()
        (npolled, wcs) = self.cq.poll()
        print(npolled, wcs)
        # for wc in wcs:
        #     if wc.status !=

