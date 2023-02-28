from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Tuple, NamedTuple

from IPgen.IPrange import IPRange


IPv4 = NamedTuple('IPv4', [('range1', IPRange), ('range2', IPRange), ('range3', IPRange), ('range4', IPRange)])
IPv6 = NamedTuple('IPv6', [('range1', IPRange), ('range2', IPRange), ('range3', IPRange), ('range4', IPRange)])


@dataclass(order=True, frozen=True)
class IPAddress(ABC):

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
        super().__init__()
        ip_ranges = tuple([IPRange(x) for x in ip_numbers])
        object.__setattr__(self, 'address', IPv4(*ip_ranges))
        object.__setattr__(self, 'sort_index', self.address[0].range)

    def __str__(self) -> str:
        return '.'.join([str(byte) for byte in self.address])


@dataclass(order=True, frozen=True)
class IPAddressV6(IPAddress):
    address: IPv6

    def __init__(self, ip_numbers: Tuple[int, int, int, int]):
        super().__init__()
        ip_ranges = tuple([IPRange(x) for x in ip_numbers])
        object.__setattr__(self, 'address', IPv6(*ip_ranges))

    def __str__(self):
        return '.'.join([str(byte) for byte in self.address])
