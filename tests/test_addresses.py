from IPgen.__main__ import random_ipv4_address
from IPgen.util import is_ipv4_address


# IPv4

# ---- Correct Values ---- #

def test_generate_valid_ip_address():
    address = str(random_ipv4_address())
    assert is_ipv4_address(address) is True


# ---- Invalid Values ---- #

def test_generate_invalid_ip_address():
    address = str("256.256.256.256")
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_negative():
    address = str("-1.256.256.256")
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_short():
    address = str("255.255.255")
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_dotend():
    address = str("255.255.255.")
    assert is_ipv4_address(address) is False


def test_generate_invalid_ip_address_dotstart():
    address = str(".255.255.255")
    assert is_ipv4_address(address) is False
