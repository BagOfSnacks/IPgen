import pytest
from urllib.request import urlopen

from IPgen.ipinfo import APIRequest
from IPgen.generators import random_ipv4_address, random_ipv6_address


@pytest.fixture
def random_ipv4() -> str:
    return str(random_ipv4_address())


@pytest.fixture
def random_ipv6() -> str:
    return str(random_ipv6_address())


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


@pytest.fixture
def API_call_invalid_v4(API_caller):
    response = API_caller.send_API_request("-1.-1.-1.-1")
    return response


@pytest.fixture
def API_call_invalid_v6(API_caller):
    response = API_caller.send_API_request("-1.-1.-1.-1")
    return response

try:
    urlopen('https://www.google.com/', timeout=10)
except:
    pytest.skip(reason="No internet connection, API calls cannot be made", allow_module_level=True)


def test_API_call_successfull_v4(API_call_v4):
    print(API_call_v4)


def test_API_call_successfull_v6(API_call_v6):
    print(API_call_v6)


def test_API_call_fail_v4(API_call_invalid_v4):
    assert API_call_invalid_v4['status'] == 'fail'


def test_API_call_fail_v6(API_call_invalid_v6):
    assert API_call_invalid_v6['status'] == 'fail'
