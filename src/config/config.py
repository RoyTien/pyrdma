import pyverbs.enums as e

ADDR = "192.168.236.129"
PORT_INT = 50008
PORT_STR = "50008"
NAME = "mlx5_3"
TIMEOUT_IN_MS = 500
BUFFER_SIZE = 1024
FILE_SIZE = 10 * BUFFER_SIZE * BUFFER_SIZE  # 10MB

OPTIONS = {
    "qp_init": {
        "qp_type": e.IBV_QPT_RC,  # https://stackoverflow.com/questions/35620376/to-create-multiple-queue-pairs-in-rdma
        # "max_send_wr": 4,
        # "max_recv_wr": 4,
        # "max_send_sge": 2,
        # "max_recv_sge": 2,
        "max_send_wr": 2800,
        "max_recv_wr": 2800,
        "max_send_sge": 32,
        "max_recv_sge": 32,
    },
    "cq_init": {
        # "cqe": 8
        "cqe": 2048

    },
    "gid_init": {
        "port_num": 1,
        "gid_index": 3,  # 3 mean to use the RoCE v2 interface `$ show_gids`
    }
}
