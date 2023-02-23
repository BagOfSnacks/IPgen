import re

from .const import IP_v4_PATTERN

def is_IPv4_adress(address: str) -> bool:
    matches = re.match(IP_v4_PATTERN, address)
    return True if matches else False