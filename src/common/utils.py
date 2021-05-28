# request struct and config
import os

import pyverbs.enums as e
import threading


def die(reason):
    print(reason)
    exit(1)


def print_info(text=""):
    print("===============================================================")
    print(text)
    print("===============================================================")


def check_wc_status(wc):
    if wc.status != e.IBV_WC_SUCCESS:
        print(wc)
        die("on_completion: status is not IBV_WC_SUCCESS")
    if wc.opcode & e.IBV_WC_RECV:
        print("wc received message")
    elif wc.opcode == e.IBV_WC_SEND:
        print("wc send completed successfully")
    elif wc.opcode == e.IBV_WC_RDMA_WRITE:
        print("wc rdma_write ok")
    elif wc.opcode == e.IBV_WC_RDMA_READ:
        print("wc rdma_read ok")
    else:
        die("on_completion: completion isn't a send or a receive")


class PollThread(threading.Thread):
    def __init__(self, context, thread_id=1, on_completion=None):
        threading.Thread.__init__(self)
        self.context = context
        self.threadID = thread_id
        self.on_completion = on_completion

    def run(self):
        pass


def create_file(file_name):
    dirname = os.path.dirname(file_name)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    return open(file_name, "wb+")