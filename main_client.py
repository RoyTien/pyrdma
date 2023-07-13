#!/usr/bin/python3
# main
import argparse
from src.rdma.socket.rdma_socket_client import RdmaSocketClient
from src.config.config import ADDR, PORT_STR
from src.socket.client import SocketClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Python Test Program for RDMA.")
    parser.add_argument('-d', '--ib_dev', required=True,
                        help='RDMA device to run the tests on.')
    args = parser.parse_args()
    args_vars = vars(args)
    # c = RdmaClient(ADDR, PORT_STR)
    # c.request()
    # c.close()
    c = SocketClient(name=args_vars.get('ib_dev'))
    # c.request()
    c.push_file("/tmp/Data16g.txt")
    # c.pull_file("./test/pull/des/50M.file")
    # c = RdmaSocketClient(ADDR, PORT_STR)
    # c.request()
