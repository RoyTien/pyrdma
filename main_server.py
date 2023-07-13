#!/usr/bin/python3
# main
import argparse
from src.rdma.socket.rdma_socket_server import RdmaSocketServer
from src.config.config import ADDR, PORT_STR, OPTIONS
from src.socket.server import SocketServer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Python Test Program for RDMA.")
    parser.add_argument('-d', '--ib_dev', required=True,
                        help='RDMA device to run the tests on.')
    args = parser.parse_args()
    args_vars = vars(args)
    # s = RdmaServer(ADDR, PORT_STR, OPTIONS)
    # s.run()
    # s.close()
    s = SocketServer(name=args_vars.get('ib_dev'))
    s.serve()
    # s = RdmaSocketServer(ADDR, PORT_STR, OPTIONS)
    # s.serve()
