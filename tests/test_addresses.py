import pytest

from IPgen.__main__ import random_ipv4_address, random_ipv6_address
from IPgen.util import is_ipv4_address, is_ipv6_address
from IPgen.IPrange import IPRange
from IPgen.IPAddress import IPAddressV4


# ---- IPv4 ----

# Value checks

def test_generate_random_valid_ipv4_address():
    address = str(random_ipv4_address())
    assert is_ipv4_address(address) is True


@pytest.mark.parametrize('address, expected', [
    ("256.256.256.256", False),
    ("-1.256.256.256", False),
    ("255.255.255", False),
    ("255.255.255.", False),
    (".255.255.255", False),
    ("a.a.a.a", False),
])

def test_generate_invalid_ip_address(address, expected):
    assert is_ipv4_address(address) is expected


# ---- IPv6 ----

# Value checks

def test_generate_random_valid_ipv6_address():
    address = str(random_ipv6_address())
    assert is_ipv6_address(address) is True

@pytest.mark.parametrize('address, expected', [
    ('0000:0000:0000:0000:0000:0000:0000:0000', True),
    ('FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF', True),
    ('F:F:F:F:F:F:F:F', True),
    ('0:0:0:0:0:0:0:0', True),
])

def test_ipv6_address(address, expected):
    assert is_ipv6_address(address) is expected


# Exceptions

def test_address_creation_without_exception():
    IPAddressV4((1, 12, 125, 256))


def test_raises_exception_when_ip_address_is_invalid():
    with pytest.raises(Exception):
        IPAddressV4(("a", "2", "a", "1"))


def test_raises_exception_when_input_is_a_string():
    with pytest.raises(TypeError):
        IPRange("a")


# Comparisons

def test_address_comparison_works():
    """Compare each address by their first number"""
    a = IPAddressV4((54, 12, 125, 256))
    b = IPAddressV4((28, 12, 125, 256))
    assert a > b


def test_address_comparison_when_equal():
    a = IPAddressV4((128, 12, 125, 256))
    b = IPAddressV4((128, 12, 125, 256))
    assert a == b


def test_address_comparison_when_all_equal():
    a = IPAddressV4((1, 1, 1, 1))
    b = IPAddressV4((1, 1, 1, 1))
    assert a == b


def test_address_comparison_when_mostly_equal():
    a = IPAddressV4((1, 1, 1, 1))
    b = IPAddressV4((1, 1, 2, 1))
    assert a < b


# Sorting

def test_address_sorting_works():
    """Check if addresses are sorted properly"""
    a = IPAddressV4((1, 2, 38, 1))
    b = IPAddressV4((5, 2, 3, 4))
    c = IPAddressV4((3, 128, 13, 256))

    expected = [a, c, b]
    addresses = [a, b, c]

    assert sorted(addresses) == expected


def test_address_sorting_with_close_ranges():
    a = IPAddressV4((1, 2, 3, 6))
    b = IPAddressV4((1, 2, 3, 5))

    expected = [b, a]
    addresses = [a, b]

    assert sorted(addresses) == expected
