from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple, NamedTuple

from .cIPrange import IPRange

IPv4 = NamedTuple('IPv4', [('range1', IPRange), ('range2', IPRange), ('range3', IPRange), ('range4', IPRange)])
IPv6 = NamedTuple('IPv6', [('range1', IPRange), ('range2', IPRange), ('range3', IPRange), ('range4', IPRange)])


class IPAddress(ABC):

    @abstractmethod
    def __init__(self, ):
        pass

    @abstractmethod
    def __repr__(self):
        pass


@dataclass
class IPAddressV4(ABC):
    address: IPv4

    def __init__(self, ip_numbers: Tuple[int, int, int, int]):
        ip_ranges = tuple([IPRange(x) for x in ip_numbers])
        self.address = IPv4(*ip_ranges)

    def __repr__(self) -> str:
        return '.'.join([str(byte) for byte in self.address])


@dataclass
class IPAddressV6(ABC):
    address: IPv6

    def __init__(self, ip_numbers: Tuple[int, int, int, int]):
        ip_ranges = tuple([IPRange(x) for x in ip_numbers])
        self.address = IPv6(*ip_ranges)

    def __repr__(self):
        return '.'.join([str(byte) for byte in self.address])
