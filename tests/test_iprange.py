import pytest

from IPgen.IP_Partition import IP_Partition_v6, IP_Partition_v4
from IPgen.util import is_ipv4_partition, is_ipv6_partition
from IPgen.generators import random_ipv4_partition, random_ipv6_partition


# ---- IPv4 ---- #

@pytest.mark.parametrize('value, expected', [
    (255, "255"),
    (0, "0"),
    (312, "255"),  # when value is too high it will clamp to the maximum range of '255'
    (-1, "0")  # will clamp to the lowest value of '0'
])
def test_ipv4_range(value: int, expected: str):
    assert str(IP_Partition_v4(value)) == expected


@pytest.mark.parametrize('value, expected', [
    (random_ipv4_partition(), True),
    ("255", True),
    ("199", True),
    ("99", True),
    ("16", True),
    ("0", True),
    ("5", True),
    ("11", True),
    ("125", True),
    ("216", True),
    ("-1", False),
    ("256", False),
    ("300", False),
    ("355", False),
    ("F", False),
    ("FFFF", False),
    ("0000", False),
])
def test_str_is_valid_ipv4_partition(value: str, expected: bool):
    assert is_ipv4_partition(value) == expected


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

@pytest.mark.parametrize('value, expected', [
    (random_ipv6_partition(), True),
    ("FFFF", True),
    ("0000", True),
    ("0000", True),
    ("LLL", False),
    ("k", False),
    ("FFFF:", False),
])
def test_str_is_valid_ipv6_partition(value: str, expected: bool):
    assert is_ipv6_partition(value) == expected
