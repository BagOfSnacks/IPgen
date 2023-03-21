import re

from IPgen.const import IP_v4_PATTERN, IP_v6_PATTERN


def is_ipv4_address(address: str) -> bool:
    matches = re.match(IP_v4_PATTERN, address)
    return True if matches else False


def is_ipv6_address(address: str) -> bool:
    matches = re.match(IP_v6_PATTERN, address)
    return True if matches else False


def num_to_hex(num: int) -> str:
    return str(hex(num)[2::]).upper()
