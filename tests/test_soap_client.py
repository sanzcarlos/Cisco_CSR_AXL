"""
Soap test case.

Test for create a SOAP object.
"""
import pytest
import sys


@pytest.fixture()
def example():
    return "a"


def cucmserver():
    return cucm(
        cucmserver="192.168.80.230",
        username="ccmadministrator",
        password="NTTvoip2020.",
        version="12.5",
    )


@pytest.mark.detail
def test_sample(example):
    assert True
