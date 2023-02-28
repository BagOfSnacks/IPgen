import pytest

from IPgen.__main__ import random_ipv4_address
from IPgen.util import is_ipv4_address
from IPgen.IPrange import IPRange
from IPgen.IPAddress import IPAddressV4


# IPv4

def test_generate_valid_ip_address():
    address = str(random_ipv4_address())
    assert is_ipv4_address(address) is True


def test_generate_invalid_ip_address():
    address = "256.256.256.256"
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_negative():
    address = "-1.256.256.256"
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_short():
    address = "255.255.255"
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_dotend():
    address = "255.255.255."
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_dotstart():
    address = ".255.255.255"
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_string():
    address = "a.a.a.a"
    assert is_ipv4_address(address) is False


def test_raises_exception_when_ip_address_is_invalid():
    with pytest.raises(Exception):
        IPAddressV4(("a", "2", "a", "1"))


def test_raises_exception_when_input_is_a_string():
    with pytest.raises(TypeError):
        IPRange("a")
