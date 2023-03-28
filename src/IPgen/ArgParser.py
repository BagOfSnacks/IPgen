"""Console argument parser"""

from argparse import ArgumentParser
from typing import Any


class ArgParser(ArgumentParser):
    def __init__(self, args: list[str]):
        """
        Parse console arguments for use in script.

        Params:
            args: list[str] - List of console flags as provided by the main() function from __main__.py file

                -h, --help                      show help message and exit
                -n [int], --amount [int]        n of IP Addresses to generate
                -v, --version {4, 6}            choose IP Address version; IPv4 or IPv6
                -i, --info                      display info of generated address(es) in JSON format
                -f [path], --filename [path]    save list of generated addresses as a .txt file to a specified location
                -j [path], --json [path]        save list of generated addresses as a .json file to a specified location
        """

        super().__init__()
        self.setup()

        self.args = self.parse_args(args)
        self.args: dict = vars(self.args)
        print(self.args)

    def get_setting(self, key: str) -> Any:
        return self.args.get(key)

    def setup(self):
        self.add_argument(
            "-n",
            "--amount",
            type=int,
            default=1,
            help="Specify number of generated IP addresses",
        )
        self.add_argument(
            "-v",
            "--version",
            type=int,
            default=4,
            choices=[4, 6],
            help="Choose IP Address version\n"
            'Accepts integer of either "4" or "6" as input',
        )
        self.add_argument(
            "-i",
            "--info",
            action="store_true",
            help="Display info of generated address(es) in JSON format\n"
            "Creates an API call to http://ip-api.com/\n"
            "Requires internet connection to work",
        )
        self.add_argument(
            "-t",
            "--txt",
            type=str,
            help="Save list of addresses to a specified location as a .txt file",
        )
        self.add_argument(
            "-j",
            "--json",
            type=str,
            help="Save list of addresses to a specified location as a json file",
        )
