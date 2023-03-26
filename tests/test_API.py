import pytest
import ipaddress

from urllib.request import urlopen

from IPgen.ipinfo import APIRequest
from IPgen.generators import random_ipv4_address, random_ipv6_address
from IPgen.util import is_ipv4_address, is_ipv6_address


try:
    urlopen('https://www.google.com/', timeout=10)
except:
    pytest.skip(reason="No internet connection, API calls cannot be made", allow_module_level=True)


def is_private_ip(ip_str: str):
    if is_ipv4_address(ip_str):
        ip = ipaddress.IPv4Address(ip_str)
        return ip.is_private

    if is_ipv6_address(ip_str):
        ip = ipaddress.IPv6Address(ip_str)
        return ip.is_private


def skip_if_private_ip(ip_str: str):
    if is_private_ip(ip_str):
        pytest.skip(reason="Skipping test for private IP address")


@pytest.fixture
def random_ipv4() -> str:
    address = str(random_ipv4_address())
    skip_if_private_ip(address)
    return address


@pytest.fixture
def random_ipv6() -> str:
    address = str(random_ipv6_address())
    skip_if_private_ip(address)
    return address


@pytest.fixture
def private_ipv4() -> str:
    return "192.168.1.1"


@pytest.fixture
def API_caller():
    return APIRequest()


@pytest.fixture
def API_call_v4(random_ipv4, API_caller):
    response = API_caller.send_API_request(random_ipv4)
    return response


@pytest.fixture
def API_call_v6(random_ipv4, API_caller):
    response = API_caller.send_API_request(random_ipv4)
    return response


def test_API_call_successfull_v4(API_call_v4):
    assert API_call_v4['status'] == 'success'


# This test should be considered as 'passed' if it successfully skips
def test_API_call_skip_on_private_ip(private_ipv4):
    skip_if_private_ip(private_ipv4)


def test_API_call_successfull_v6(API_call_v6):

    assert API_call_v6['status'] == 'success'


def test_API_call_fail_v4(API_caller):
    response = API_caller.send_API_request('192.168.1.1')
    assert response['status'] == 'fail'


def test_API_call_fail_v6(API_caller):
    response = API_caller.send_API_request('FD13:0FB5:4E00:46D3:FFFF:FFFF:FFFF:FFFF')
    assert response['status'] == 'fail'


def test_API_call_v4_invalid_address(API_caller):
    with pytest.raises(Exception):
        API_caller.send_API_request('-1.-1.-1.-1')


def test_API_call_v6_invalid_address(API_caller):
    with pytest.raises(Exception):
        API_caller.send_API_request('M:M:M:M:M:M:M:M')


def test_API_call_raise_exception(API_caller):
    with pytest.raises(Exception):
        API_caller.send_API_request('')
