import re

from IPgen.const import IP_v4_PATTERN


def is_ipv4_address(address: str) -> bool:
    matches = re.match(IP_v4_PATTERN, address)
    return True if matches else False
