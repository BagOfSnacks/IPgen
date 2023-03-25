"""IP Address classes"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Tuple, NamedTuple

from IPgen.IP_Partition import IP_Partition_v4, IP_Partition_v6
from IPgen.const import IP_v4_PARTITION_DIVIDER, IP_v6_PARTITION_DIVIDER
from IPgen.util import is_ipv4_address, is_ipv6_address


IPv4 = NamedTuple('IPv4',
                  [('range1', IP_Partition_v4),
                   ('range2', IP_Partition_v4),
                   ('range3', IP_Partition_v4),
                   ('range4', IP_Partition_v4)])

IPv6 = NamedTuple('IPv6',
                  [('part1', IP_Partition_v6),
                   ('part2', IP_Partition_v6),
                   ('part3', IP_Partition_v6),
                   ('part4', IP_Partition_v6),
                   ('part5', IP_Partition_v6),
                   ('part6', IP_Partition_v6),
                   ('part7', IP_Partition_v6),
                   ('part8', IP_Partition_v6)])


@dataclass(order=True, frozen=True)
class IPAddress(ABC):
    """Abstract data class representation of IP Address"""

    address: NamedTuple = field(default=None, init=False)

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def ip_address_from_str(cls, address_str: str) -> object:
        pass


@dataclass(order=True, frozen=True)
class IPAddressV4(IPAddress):

    _sort_index: int = field(repr=False, init=False)
    address: IPv4

    def __init__(self, ip_numbers: Tuple[int, int, int, int]):
        """
        Create IPv4 address from a tuple of 4 numbers
        Integers will automatically be clamped to a range of 0-255
        Address will be represented as the 'address' property as a namedTuple 'IPv4'
        To display address in a regular IPv4 format, convert this class instance to a string
        """
        super().__init__()
        ip_ranges = tuple([IP_Partition_v4(x) for x in ip_numbers])
        object.__setattr__(self, 'address', IPv4(*ip_ranges))
        object.__setattr__(self, '_sort_index', tuple(self.address))

    def __str__(self) -> str:
        """
        When converting to string display IP Address in the correct IPv4 format
        Format: x.x.x.x
        """
        return '.'.join([str(byte) for byte in self.address])

    @classmethod
    def ip_address_from_str(cls, address_str: str) -> object:
        """
            Construct IPAddressV4 instance from a valid string
            ex. '255.103.64.18' -> IPAddressv4(255, 103, 64, 18)
        """
        if not is_ipv4_address(address_str):
            raise ValueError("String input isn't a valid IPv4 address")

        address_partitions: list[str] = address_str.split(IP_v4_PARTITION_DIVIDER)
        address_partitions: list[int] = [int(part) for part in address_partitions]
        return cls(tuple(address_partitions))


@dataclass(order=True, frozen=True)
class IPAddressV6(IPAddress):

    address: IPv6

    def __init__(self, ip_numbers: Tuple[int, int, int, int, int, int, int, int]):
        """
        Create IPv6 address from a tuple of 8 numbers
        Integers will be automatically converted to hexadecimal system
        Address will be represented as the 'address' property as a namedTuple 'IPv6'
        To display address in a regular IPv6 format, convert this class instance to a string
        """
        super().__init__()
        ip_ranges = [IP_Partition_v6(x) for x in ip_numbers]
        object.__setattr__(self, 'address', IPv6(*ip_ranges))

    def __str__(self):
        """
        When converting to string display IP Address in the correct IPv6 format
        Format: x:x:x:x:x:x:x:x
        """
        return ':'.join([str(byte) for byte in self.address])

    @classmethod
    def ip_address_from_str(cls, address_str: str) -> object:
        """
            Construct IPAddressV6 instance from a valid string
            ex. '0:0:0:0:0:0:0:0' -> IPAddressv6(0, 0, 0, 0, 0, 0, 0, 0)
        """
        if not is_ipv6_address(address_str):
            raise ValueError("String input isn't a valid IPv6 address")

        address_partitions: list[str] = address_str.split(IP_v6_PARTITION_DIVIDER)
        number_partitions: list[int] = [int(part, 16) for part in address_partitions]
        return cls(tuple(number_partitions))
