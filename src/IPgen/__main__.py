#!/usr/bin/env python3

from __future__ import annotations

import sys

from typing import Optional, Sequence, TYPE_CHECKING

from IPgen.ArgParser import ArgParser
from IPgen.FileSaver import TxtSaver, JSONSaver
from IPgen.generators import random_ipv4_address, random_ipv6_address
from IPgen.ipinfo import APIRequest

if TYPE_CHECKING:
    from IPgen.IPAddress import IPAddressV4, IPAddressV6


def main(argv: Optional[Sequence[str]] = None):
    ARG_PARSER = ArgParser(argv)
    AMOUNT_OF_ADDRESSES = ARG_PARSER.get_setting("amount")

    if ARG_PARSER.get_setting("version") == 6:
        ip_addresses: list[IPAddressV6] = [
            random_ipv6_address() for _ in range(0, AMOUNT_OF_ADDRESSES)
        ]
    else:
        ip_addresses: list[IPAddressV4] = [
            random_ipv4_address() for _ in range(0, AMOUNT_OF_ADDRESSES)
        ]

    if ARG_PARSER.get_setting("info"):
        API = APIRequest()
        response = [API.send_API_request(str(ip)) for ip in ip_addresses]
        ip_addresses = response
        print(response)
    else:
        print([list(map(str, ip_addresses))])

    if loc_txt := ARG_PARSER.get_setting("txt"):
        TxtSaver(loc_txt, ip_addresses).save_to_file()

    if loc_json := ARG_PARSER.get_setting("json"):
        JSONSaver(loc_json, ip_addresses).save_to_file()

    sys.exit(0)


if __name__ == "__main__":
    main()
