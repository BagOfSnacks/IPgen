import re
import ipaddress

from IPgen.const import (
    IP_v4_PATTERN,
    IP_v6_PATTERN,
    IP_v4_PARTITION_PATTERN,
    IP_v6_PARTITION_PATTERN,
)


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


def is_private_ip(ip_str: str):
    if is_ipv4_address(ip_str):
        ip = ipaddress.IPv4Address(ip_str)
        return ip.is_private

    if is_ipv6_address(ip_str):
        ip = ipaddress.IPv6Address(ip_str)
        return ip.is_private


def num_to_hex(num: int) -> str:
    return str(hex(num)[2::]).upper()
