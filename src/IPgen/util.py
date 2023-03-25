import re

from IPgen.const import IP_v4_PATTERN, IP_v6_PATTERN, IP_v4_PARTITION_PATTERN, IP_v6_PARTITION_PATTERN


def is_ipv4_address(address: str) -> bool:
    matches = re.match(IP_v4_PATTERN, address)
    return True if matches else False


def is_ipv6_address(address: str) -> bool:
    matches = re.match(IP_v6_PATTERN, address)
    return True if matches else False


def is_ipv4_partition(address_partition: str) -> bool:
    matches = re.match(IP_v4_PARTITION_PATTERN, address_partition)
    return True if matches else False


def is_ipv6_partition(address_partition: str) -> bool:
    matches = re.match(IP_v6_PARTITION_PATTERN, address_partition)
    return True if matches else False


def num_to_hex(num: int) -> str:
    return str(hex(num)[2::]).upper()
