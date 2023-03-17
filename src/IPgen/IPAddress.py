"""IP Address classes"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Tuple, NamedTuple

from IPgen.IPrange import IPRange_v4, IPRange_v6


IPv4 = NamedTuple('IPv4',
                  [('range1', IPRange_v4), ('range2', IPRange_v4), ('range3', IPRange_v4), ('range4', IPRange_v4)])

IPv6 = NamedTuple('IPv6',
                  [('part1', IPRange_v6),
                   ('part2', IPRange_v6),
                   ('part3', IPRange_v6),
                   ('part4', IPRange_v6),
                   ('part5', IPRange_v6),
                   ('part6', IPRange_v6),
                   ('part7', IPRange_v6),
                   ('part8', IPRange_v6)])


@dataclass(order=True, frozen=True)
class IPAddress(ABC):
    """Abstract data class representation of IP Address"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


@dataclass(order=True, frozen=True)
class IPAddressV4(IPAddress):
    sort_index: int = field(repr=False, init=False)
    address: IPv4

    def __init__(self, ip_numbers: Tuple[int, int, int, int]):
        """
        Create IPv4 address from a tuple of 4 numbers
        Integers will automatically be clamped to a range of 0-255
        Address will be represented as the 'address' property as a namedTuple 'IPv4'
        To display address in a regular IPv4 format, convert this class instance to a string
        """
        super().__init__()
        ip_ranges = tuple([IPRange_v4(x) for x in ip_numbers])
        object.__setattr__(self, 'address', IPv4(*ip_ranges))
        object.__setattr__(self, 'sort_index', tuple(self.address))

    def __str__(self) -> str:
        """
        When converting to string display IP Address in the correct IPv4 format
        Format: x.x.x.x
        """
        return '.'.join([str(byte) for byte in self.address])


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
        ip_ranges = [IPRange_v6(x) for x in ip_numbers]
        object.__setattr__(self, 'address', IPv6(*ip_ranges))

    def __str__(self):
        """
        When converting to string display IP Address in the correct IPv6 format
        Format: x:x:x:x:x:x:x:x
        """
        return ':'.join([str(byte) for byte in self.address])
