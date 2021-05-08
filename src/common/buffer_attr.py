# metadata buffer
import pickle
import sys


class BufferAttr:
    def __init__(self, gid=None, qp_num=0, addr: int = 0, length: int = 0, local_stag="", remote_stag=""):
        self.gid = gid
        self.qp_num = qp_num
        self.addr = addr
        self.length = length
        self.local_stag = local_stag
        self.remote_stag = remote_stag

    def __str__(self) -> str:
        return "buffer_addr: %s; buffer_len: %s; lkey: %s; rkey: %s;\ngid: %s; qp_num: %s\n" % \
               (self.addr, self.length, self.local_stag, self.remote_stag, self.gid, self.qp_num)

    def __len__(self) -> int:
        return len(serialize(self))

    def size(self) -> int:
        return sys.getsizeof(self)


def serialize(buffer_attr: BufferAttr) -> bytes:
    return pickle.dumps(buffer_attr)


def deserialize(b: bytes) -> BufferAttr:
    return pickle.loads(b)
