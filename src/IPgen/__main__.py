#!/usr/bin/env python3

from random import sample
from typing import Optional, Sequence

from IPgen.ArgParser import ArgParser
from IPgen.FileSaver import TxtSaver, JSONSaver
from IPgen.IPAddress import IPAddressV4, IPAddressV6
from IPgen.const import IP_v4_RANGE_MIN, \
    IP_v4_RANGE_MAX, \
    IP_v4_LENGTH, \
    IP_v6_LENGTH, \
    IP_v6_RANGE_MIN, \
    IP_v6_RANGE_MAX


def random_ipv4_address() -> IPAddressV4:
    address = tuple(sample(range(IP_v4_RANGE_MIN, IP_v4_RANGE_MAX+1), IP_v4_LENGTH))
    return IPAddressV4(address)


def random_ipv6_address() -> IPAddressV6:
    address = tuple(sample(range(IP_v6_RANGE_MIN, IP_v6_RANGE_MAX+1), IP_v6_LENGTH))
    return IPAddressV6(address)


def main(argv: Optional[Sequence[str]] = None):
    arg_parser = ArgParser(argv)
    AMOUNT_OF_ADDRESSES = arg_parser.get_setting('amount')

    # Generate x amount of addresses based on selected version
    if arg_parser.get_setting('version') == 6:
        ip_addresses = [random_ipv6_address() in range(0, AMOUNT_OF_ADDRESSES)]
    else:
        ip_addresses = [random_ipv4_address() in range(0, AMOUNT_OF_ADDRESSES)]

    # If save location has been specified save to it
    if loc_txt := arg_parser.get_setting('filename'):
        TxtSaver(loc_txt, ip_addresses).save_to_file()

    if loc_json := arg_parser.get_setting('json'):
        JSONSaver(loc_json, ip_addresses).save_to_file()

    print(ip_addresses)


if __name__ == "__main__":
    main()
