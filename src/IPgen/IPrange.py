from dataclasses import dataclass, field

from abc import ABC, abstractmethod
from IPgen.const import IP_v4_RANGE_MIN, IP_v4_RANGE_MAX, IP_v6_RANGE_MAX, IP_v6_RANGE_MIN
from IPgen.util import num_to_hex


@dataclass(order=True, frozen=True)
class IPRange(ABC):
    sort_index: int = field(repr=False, init=False)
    value: int
    range_min: int
    range_max: int

    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    def clamp_range(self, input):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


@dataclass(order=True, frozen=True)
class IPRange_v4(IPRange):
    sort_index: int = field(repr=False, init=False)
    value: int
    range_min: int = IP_v4_RANGE_MIN
    range_max: int = IP_v4_RANGE_MAX

    def __init__(self, value: int):
        super().__init__(value)
        if not isinstance(value, int):
            raise TypeError("IPv4 Address can only contain numbers")
        object.__setattr__(self, 'value', self.clamp_range(value))
        object.__setattr__(self, 'sort_index', self.value)

    def clamp_range(self, value: int) -> int:
        if value < self.range_min:
            return self.range_min
        elif value > self.range_max:
            return self.range_max
        return value

    def __repr__(self) -> str:
        return str(self.value)


@dataclass(order=True, frozen=True)
class IPRange_v6(IPRange):
    sort_index: int = field(repr=False, init=False)
    value: str
    range_min: int = IP_v6_RANGE_MIN
    range_max: int = IP_v6_RANGE_MAX


    def __init__(self, value: int):
        super().__init__(value)
        if not isinstance(value, int):
            raise TypeError("Value isn't an integer")
        object.__setattr__(self, 'value', self.clamp_range(value))
        object.__setattr__(self, 'sort_index', self.value)

    def clamp_range(self, input: int):
        if input < self.range_min:
            return "0000"
        if input > self.range_max:
            return "FFFF"
        return num_to_hex(input)

    def __repr__(self) -> str:
        return str(self.value)