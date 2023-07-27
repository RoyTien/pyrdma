#!/usr/bin/python3
import argparse

# PACKET_SIZE = 1082.0
PACKET_SIZE = 4154.0
PACKET_UNIT = 'bytes'
GB_TO_BYTE = 1024 * 1024 * 1024
Gb_TO_BYTE = GB_TO_BYTE / 8

# TIME_INTERVAL_UNIT = 'microsecond'  # microsecond 1 second = 1000000 microsecond

SEC_TO_MICROSEC = 1000000
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Calculaor for transfer data per second")
    parser.add_argument('-p', '--packets_num', type=int,
                        help='The number of packet be transfered')
    parser.add_argument('-t', '--time_interval', type=int,
                        help='The time interval that these packets be transfered')
    parser.add_argument('-f', '--first_packet_number', type=int,
                        help='The number of the first packet be transfered')
    parser.add_argument('-l', '--last_packet_number', type=int,
                        help='The number of the last packet be transfered')
    parser.add_argument('-s', '--time_interval_start', type=int,
                        help='The time of the first packet be transfered')
    parser.add_argument('-c', '--time_interval_complete', type=int,
                        help='The time of the last packet be transfered')
    args = parser.parse_args()
    args_vars = vars(args)
    packets_num = args_vars.get('packets_num') if args_vars.get('packets_num') else args_vars.get('last_packet_number') - args_vars.get('first_packet_number')
    time_interval = args_vars.get('time_interval') if args_vars.get('time_interval') else args_vars.get('time_interval_complete') - args_vars.get('time_interval_start')  # microsecond
    data_per_microsec = packets_num * PACKET_SIZE / time_interval  # bytes / microsecond
    data_per_sec = data_per_microsec * SEC_TO_MICROSEC / Gb_TO_BYTE  # Gb / second
    print("{} Gb/s".format(data_per_sec))
    print("{} GB/s".format(data_per_sec / 8))
