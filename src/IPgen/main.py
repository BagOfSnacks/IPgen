from random import sample
from typing import Optional, Sequence

from ArgParser import ArgParser
from FileSaver import TxtSaver, JSONSaver, FileSaver
from IPAddress import IPAddressV4
from const import IP_RANGE_MIN, IP_RANGE_MAX, IP_v4_BYTES


def random_IPv4_Adress() -> IPAddressV4:
    address = tuple(sample(range(IP_RANGE_MIN, IP_RANGE_MAX+1), IP_v4_BYTES))
    return IPAddressV4(address)

def main(argv: Optional[Sequence[str]] = None):
    arg_parser = ArgParser(argv)
    AMOUNT_OF_ADDRESSES = arg_parser.get_setting('amount')

    ip_adresses = [random_IPv4_Adress() for x in range(0, AMOUNT_OF_ADDRESSES)]

    if loc_txt := arg_parser.get_setting('filename'):
        file_saver: FileSaver = TxtSaver(loc_txt)

    if loc_json := arg_parser.get_setting('json'):
        file_saver: FileSaver = JSONSaver(loc_json)

    print(ip_adresses)

if __name__ == "__main__":
    main()