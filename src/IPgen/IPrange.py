from dataclasses import dataclass, field
from IPgen.const import IP_v4_RANGE_MIN, IP_v4_RANGE_MAX


@dataclass(order=True, frozen=True)
class IPRange:
    sort_index: int = field(repr=False, init=False)
    range: int = 0
    range_min: int = IP_v4_RANGE_MIN
    range_max: int = IP_v4_RANGE_MAX

    def __init__(self, range: int):
        if not isinstance(range, int):
            raise TypeError("IP Address can only contain numbers")
        object.__setattr__(self, 'range', self.clamp_range(range))
        object.__setattr__(self, 'sort_index', self.range)

    def clamp_range(self, range: int) -> int:
        if range < self.range_min:
            return self.range_min
        elif range > self.range_max:
            return self.range_max
        else:
            return range

    def __repr__(self) -> str:
        return str(self.range)
