# metadata buffer
import pickle
import sys


class BufferAttr:
    # gid=None, qp_num=0,
    def __init__(self, addr: int = 0, length: int = 0, local_stag="", remote_stag="", gid="", qp_num=0):
        # self.gid = gid
        # self.qp_num = qp_num
        self.addr = addr
        self.length = length
        self.local_stag = local_stag
        self.remote_stag = remote_stag
        self.gid = gid
        self.qp_num = qp_num

    def __str__(self) -> str:
        return "buffer_addr: %s;\nbuffer_len: %s;\nlkey: %s;\nrkey: %s;\ngid: %s;\nqp_num: %s;\n%s\n" % \
               (self.addr, self.length, self.local_stag, self.remote_stag, self.gid, self.qp_num, 
                "\"QP Number 简称为QPN，就是每个QP的编号。IB协议中规定用24个bit来表示QPN，即每个节点最大可以同时使用个QP。每个节点都各自维护着QPN的集合，相互之间是独立的，即不同的节点上可以存在编号相同的QP。\"")

    def __len__(self) -> int:
        return len(serialize(self))

    def size(self) -> int:
        return sys.getsizeof(self)


def serialize(buffer_attr) -> bytes:
    return pickle.dumps(buffer_attr)


def deserialize(b: bytes):
    return pickle.loads(b)

