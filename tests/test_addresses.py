from IPgen.__main__ import random_IPv4_Adress
from IPgen.util import is_IPv4_adress

#
# IPv4
#
# ---- Correct Values ---- #

def test_generate_valid_ip_adress():
    address = str(random_IPv4_Adress())
    assert is_IPv4_adress(address) is True

# ---- Invalid Values ---- #

def test_generate_invalid_ip_adress():
    address = str("256.256.256.256")
    assert is_IPv4_adress(address) is False

def test_generate_invalid_ip_adress_negative():
    address = str("-1.256.256.256")
    assert is_IPv4_adress(address) is False

def test_generate_invalid_ip_adress_short():
    address = str("255.255.255")
    assert is_IPv4_adress(address) is False

def test_generate_invalid_ip_adress_dotend():
    address = str("255.255.255.")
    assert is_IPv4_adress(address) is False

def test_generate_invalid_ip_adress_dotstart():
    address = str(".255.255.255")
    assert is_IPv4_adress(address) is False