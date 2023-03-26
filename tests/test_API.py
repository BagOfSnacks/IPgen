import pytest
from urllib.request import urlopen

from IPgen.ipinfo import APIRequest
from IPgen.generators import random_ipv4_address, random_ipv6_address


try:
    urlopen('https://www.google.com/', timeout=10)
except:
    pytest.skip(reason="No internet connection, API calls cannot be made", allow_module_level=True)


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


def test_API_call_successfull_v4(API_call_v4):
    assert API_call_v4['status'] == 'success'


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
