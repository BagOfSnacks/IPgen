#!/usr/bin/env python3

import sys

from typing import Optional, Sequence

from IPgen.ArgParser import ArgParser
from IPgen.FileSaver import TxtSaver, JSONSaver
from IPgen.IPAddress import IPAddressV4, IPAddressV6
from IPgen.generators import random_ipv4_address, random_ipv6_address


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
