import pytest

from IPgen.__main__ import random_ipv4_address, random_ipv6_address
from IPgen.IPAddress import IPAddressV4, IPAddressV6


@pytest.fixture()
def random_IPv4_adresses(n: int) -> [IPAddressV4]:
    return [random_ipv4_address() for _ in range(n)]

@pytest.fixture
def random_IPv6_adresses(n: int) -> [IPAddressV6]:
    return [random_ipv6_address() for _ in range(n)]