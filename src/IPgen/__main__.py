#!/usr/bin/env python3

from random import sample
from typing import Optional, Sequence

from IPgen.ArgParser import ArgParser
from IPgen.FileSaver import TxtSaver, JSONSaver
from IPgen.IPAddress import IPAddressV4
from IPgen.const import IP_v4_RANGE_MIN, IP_v4_RANGE_MAX, IP_v4_BYTES


def random_ipv4_address() -> IPAddressV4:
    address = tuple(sample(range(IP_v4_RANGE_MIN, IP_v4_RANGE_MAX+1), IP_v4_BYTES))
    return IPAddressV4(address)


def main(argv: Optional[Sequence[str]] = None):
    arg_parser = ArgParser(argv)
    AMOUNT_OF_ADDRESSES = arg_parser.get_setting('amount')

    ip_addresses = [random_ipv4_address() for x in range(0, AMOUNT_OF_ADDRESSES)]

    if loc_txt := arg_parser.get_setting('filename'):
        TxtSaver(loc_txt, ip_addresses).save_to_file()

    if loc_json := arg_parser.get_setting('json'):
        JSONSaver(loc_json, ip_addresses).save_to_file()

    print(ip_addresses)


if __name__ == "__main__":
    main()
