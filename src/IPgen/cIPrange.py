from const import IP_RANGE_MIN, IP_RANGE_MAX


class IPRange:
    range_min: int = IP_RANGE_MIN
    range_max: int = IP_RANGE_MAX

    def __init__(self, range: int):
        self.range: int = self.clamp_range(range)

    def clamp_range(self, range: int) -> int:
        if range < self.range_min:
            return self.range_min
        elif range > self.range_max:
            return self.range_min
        else:
            return range

    def __repr__(self) -> str:
        return str(self.range)