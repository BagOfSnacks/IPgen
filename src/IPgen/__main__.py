#!/usr/bin/env python3

import sys

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
    address_partition_range = range(IP_v4_RANGE_MIN, IP_v4_RANGE_MAX+1)
    address = tuple(sample(address_partition_range, IP_v4_LENGTH))
    return IPAddressV4(address)


def random_ipv6_address() -> IPAddressV6:
    address_partition_range = range(IP_v6_RANGE_MIN, IP_v6_RANGE_MAX+1)
    address = tuple(sample(address_partition_range, IP_v6_LENGTH))
    return IPAddressV6(address)


def main(argv: Optional[Sequence[str]] = None):
    ARG_PARSER = ArgParser(argv)
    AMOUNT_OF_ADDRESSES = ARG_PARSER.get_setting('amount')

    # Generate x amount of addresses based on selected version
    if ARG_PARSER.get_setting('version') == 6:
        ip_addresses: list[IPAddressV6] = [random_ipv6_address() for _ in range(0, AMOUNT_OF_ADDRESSES)]
    else:
        ip_addresses: list[IPAddressV4] = [random_ipv4_address() for _ in range(0, AMOUNT_OF_ADDRESSES)]

    # If save location has been specified save to it
    if loc_txt := ARG_PARSER.get_setting('txt'):
        TxtSaver(loc_txt, ip_addresses).save_to_file()

    if loc_json := ARG_PARSER.get_setting('json'):
        JSONSaver(loc_json, ip_addresses).save_to_file()

    print([list(map(str, ip_addresses))])
    sys.exit(0)


if __name__ == "__main__":
    main()
