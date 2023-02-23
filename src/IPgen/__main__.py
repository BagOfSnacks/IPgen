from random import sample
from typing import Optional, Sequence

from .ArgParser import ArgParser
from .FileSaver import TxtSaver, JSONSaver
from .IPAddress import IPAddressV4
from .const import IP_RANGE_MIN, IP_RANGE_MAX, IP_v4_BYTES


def random_IPv4_Adress() -> IPAddressV4:
    address = tuple(sample(range(IP_RANGE_MIN, IP_RANGE_MAX+1), IP_v4_BYTES))
    return IPAddressV4(address)

def main(argv: Optional[Sequence[str]] = None):
    arg_parser = ArgParser(argv)
    AMOUNT_OF_ADDRESSES = arg_parser.get_setting('amount')

    ip_addresses = [random_IPv4_Adress() for x in range(0, AMOUNT_OF_ADDRESSES)]

    if loc_txt := arg_parser.get_setting('filename'):
        TxtSaver(loc_txt, ip_addresses).save_to_file()

    if loc_json := arg_parser.get_setting('json'):
        JSONSaver(loc_json, ip_addresses).save_to_file()

    print(ip_addresses)

if __name__ == "__main__":
    main()