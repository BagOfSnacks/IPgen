import pytest

from IPgen.IP_Partition import IP_Partition_v6, IP_Partition_v4


# ---- IPv4 ---- #

@pytest.mark.parametrize('value, expected', [
    (255, "255"),
    (0, "0"),
    (312, "255"),  # when value is too high it will clamp to the maximum range of '255'
    (-1, "0")  # will clamp to the lowest value of '0'
])
def test_ipv4_range(value: int, expected: str):
    assert str(IP_Partition_v4(value)) == expected


def test_raises_exception_when_input_is_a_string():
    with pytest.raises(TypeError):
        IP_Partition_v4("a")


# ---- IPv6 ---- #

@pytest.mark.parametrize('value, expected', [
    (255, "FF"),
    (0, "0"),
    (65535, "FFFF"),
    (70000, "FFFF"),  # when value is too high it will clamp to the maximum range of 'FFFF'
    (-1, "0000")  # will clamp to the lowest value of '0000'
])
def test_ipv6_range(value: int, expected: str):
    assert str(IP_Partition_v6(value)) == expected


def test_raises_exception_when_input_is_not_int():
    with pytest.raises(TypeError):
        IP_Partition_v6("b")
