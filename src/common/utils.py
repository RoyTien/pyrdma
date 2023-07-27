# request struct and config
import os

import pyverbs.cq
import pyverbs.enums as e


def check_msg(msg, msg2):
    return msg.decode("UTF-8", "ignore").strip("\x00").encode() == msg2


def die(reason):
    print(reason)
    exit(1)


def print_info(text=""):
    print("===============================================================")
    print(text)
    print("===============================================================")


def check_wc_status(wc: pyverbs.cq.WC):
    if wc.status != e.IBV_WC_SUCCESS:
        print(wc)
        die("on_completion: status is not IBV_WC_SUCCESS")
        """
        Recently, there will be two kinds of Error: 
        1. IBV_WC_RETRY_EXC_ERR
        2. IBV_WC_RNR_RETRY_EXC_ERR
        https://www.ibm.com/docs/en/sdk-java-technology/8?topic=jverbs-workcompletionstatus
        https://linux-rdma.vger.kernel.narkive.com/lD05eFPQ/work-completion-error-transport-retry-counter-exceeded

        IBV_WC_RETRY_EXC_ERR
        - This event is generated when a sender is unable to receive feedback from the receiver. 
        - This means that either the receiver just never ACKs sender messages in a specified time period, 
        or it has been disconnected or it is in a bad state which prevents it from responding.
        - Transport Retry Counter Exceeded: The local transport timeout retry counter was exceeded while trying to send this message. 
            This means that the remote side didn't send any Ack or Nack. 
            If this happens when sending the first message, usually this mean that the connection attributes are wrong or 
            the remote side isn't in a state that it can respond to messages. If this happens after sending the first message, 
            usually it means that the remote QP isn't available anymore. 
        - Relevant for RC QPs.
        
        IBV_WC_RNR_RETRY_EXC_ERR
        - This event is generated when the RNR NAK retry count is exceeded. 
        - This may be caused by lack of receive buffers on the responder side.
        - This usually means that the remote side didn't post any WR to its Receive Queue. 
        - Relevant for RC QPs.
        """
    if wc.opcode & e.IBV_WC_RECV:
        print("received message")
    elif wc.opcode == e.IBV_WC_SEND:
        print("send completed successfully")
    elif wc.opcode == e.IBV_WC_RDMA_WRITE:
        print("write complete")
    elif wc.opcode == e.IBV_WC_RECV_RDMA_WITH_IMM:
        print("write with imm_data:", wc.imm_data)
    elif wc.opcode == e.IBV_WC_RDMA_READ:
        print("read complete")
    else:
        die("completion isn't a send, write, read or a receive")


def create_file(file_name):
    dirname = os.path.dirname(file_name)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    return open(file_name, "wb+")
