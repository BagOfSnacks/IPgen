"""Partitions of IP Addresses"""

from dataclasses import dataclass, field

from abc import ABC, abstractmethod
from IPgen.const import IP_v4_RANGE_MIN, IP_v4_RANGE_MAX, IP_v6_RANGE_MAX, IP_v6_RANGE_MIN
from IPgen.util import num_to_hex


@dataclass(order=True, frozen=True)
class IP_Partition(ABC):
    """
    Abstract data class that represents a single fragment/partition of IPv4 or IPv6 address.
    Provides sorting and order/comparison logic between addresses of the same type.
    """
    _sort_index: int = field(repr=False, init=False)
    value: int
    range_min: int
    range_max: int

    @abstractmethod
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("Address partition isn't an integer")

    @abstractmethod
    def clamp_range(self, val):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


@dataclass(order=True, frozen=True)
class IP_Partition_v4(IP_Partition):
    """
        Represents a single partition of an IPv4 Address.

        Params:
            value: int
                Integer value of a partition that then gets automatically clamped to a range of 0-255
    """

    _sort_index: int = field(repr=False, init=False)
    value: int
    range_min: int = IP_v4_RANGE_MIN
    range_max: int = IP_v4_RANGE_MAX

    def __init__(self, value: int):
        super().__init__(value)
        object.__setattr__(self, 'value', self.clamp_range(value))
        object.__setattr__(self, '_sort_index', self.value)

    def clamp_range(self, val: int) -> int:
        if val < self.range_min:
            return self.range_min
        elif val > self.range_max:
            return self.range_max
        return val

    def __repr__(self) -> str:
        return str(self.value)


@dataclass(order=True, frozen=True)
class IP_Partition_v6(IP_Partition):
    """
        Represents a single partition of an IPv6 Address.

        Params:
            value: int
                Integer value of a partition that then gets automatically clamped to a range of 0-65535
                Value then gets converted to a hexadecimal system
    """

    _sort_index: int = field(repr=False, init=False)
    value: str
    range_min: int = IP_v6_RANGE_MIN
    range_max: int = IP_v6_RANGE_MAX


    def __init__(self, value: int):
        super().__init__(value)
        object.__setattr__(self, 'value', self.clamp_range(value))
        object.__setattr__(self, '_sort_index', self.value)

    def clamp_range(self, val: int):
        if val < self.range_min:
            return "0000"
        if val > self.range_max:
            return "FFFF"
        return num_to_hex(val)

    def __repr__(self) -> str:
        return str(self.value)
