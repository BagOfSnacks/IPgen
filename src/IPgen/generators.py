"""Generate random IP addresses & address partitions"""

import random

from IPgen.util import num_to_hex
from IPgen.IPAddress import IPAddressV4, IPAddressV6
from IPgen.const import IP_v4_RANGE_MIN, \
    IP_v4_RANGE_MAX, \
    IP_v4_LENGTH, \
    IP_v6_LENGTH, \
    IP_v6_RANGE_MIN, \
    IP_v6_RANGE_MAX


def random_ipv4_address() -> IPAddressV4:
    address_partition_range = range(IP_v4_RANGE_MIN, IP_v4_RANGE_MAX+1)
    address = tuple(random.sample(address_partition_range, IP_v4_LENGTH))
    return IPAddressV4(address)


def random_ipv6_address() -> IPAddressV6:
    address_partition_range = range(IP_v6_RANGE_MIN, IP_v6_RANGE_MAX+1)
    address = tuple(random.sample(address_partition_range, IP_v6_LENGTH))
    return IPAddressV6(address)


def random_ipv4_partition() -> str:
    partition = random.randint(IP_v4_RANGE_MIN, IP_v4_RANGE_MAX)
    return str(partition)


def random_ipv6_partition() -> str:
    partition = random.randint(IP_v6_RANGE_MIN, IP_v6_RANGE_MAX)
    partition = num_to_hex(partition)
    return str(partition)
