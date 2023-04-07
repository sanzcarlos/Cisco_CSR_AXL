"""
Soap test case.

Test for create a SOAP object.
"""
import pytest
import sys
import ipaddress
import socket

from dotenv import dotenv_values


def check_ipaddress(ip):
    try:
        ipaddress.ip_address(socket.gethostbyname(ip))
        return True
    except ValueError as err:
        return False


@pytest.fixture()
def cucmserver():
    settings = dotenv_values()
    print(settings)
    return settings


@pytest.mark.detail
def test_env_CUCM_SERVER(cucmserver):
    assert check_ipaddress(cucmserver['CUCM_SERVER'])
