# content of test_sample.py
import pytest

def func(x):
    return x + 1

@pytest.fixture(scope='module')
def cucmserver():
    return cucm(
        cucmserver="192.168.80.230",
        username="ccmadministrator",
        password="NTTvoip2020.",
        version="12.5",

    )

def test_sample():
    assert func(1) == 2
