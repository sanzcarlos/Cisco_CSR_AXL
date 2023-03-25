"""
Soap test case.

Test for create a SOAP object.
"""
import pytest
import sys

from dotenv import dotenv_values


@pytest.fixture()
def cucmserver():
    settings = dotenv_values()
    print(settings)
    return settings


@pytest.mark.detail
def test_sample(cucmserver):
    assert cucmserver['CUCM_SERVER'] == '192.168.80.230'
