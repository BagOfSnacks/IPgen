import argparse
from typing import Any

class ArgParser:
    def __init__(self, args: [str]):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-v',
                                 '--version',
                                 type=int,
                                 default=4,
                                 choices=[4, 6],
                                 help='Choose IP Address version\n'
                                      'Accepts integer of either "4" or "6" as input')
        self.parser.add_argument('-n',
                                 '--amount',
                                 type=int,
                                 default=1,
                                 help='Specify number of generated IP adresses')
        self.parser.add_argument('-i',
                                 '--info',
                                 help='Display info of generated address(es) in JSON format\n'
                                      'Creates an API call to https://ipinfo.io/\n'
                                      'Requires internet connection to work')
        self.parser.add_argument('-f',
                                 '--filename',
                                 type=str,
                                 help='Save list of addresses to a specified location as a .txt file')
        self.parser.add_argument('-j',
                                 '--json',
                                 type=str,
                                 help='Save list of addresses to a specified location as a json file')

        self.args = self.parser.parse_args(args)
        self.settings: dict = vars(self.args)
        print(self.settings)

    def get_setting(self, key: str) -> Any:
        return self.settings.get(key)