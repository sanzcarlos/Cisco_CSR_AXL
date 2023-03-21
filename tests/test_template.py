# content of test_sample.py
import pytest
import sys

def func(a,b):
    return a + b

@pytest.fixture()
def cucmserver():
    return cucm(
        cucmserver="ip_address",
        username="username",
        password="password",
        version="12.5",
    )

@pytest.mark.test
@pytest.mark.parametrize("a,b,expected_result",[(1,2,3),(5,6,11)])
def test_sample(a,b,expected_result):
    assert func(a,b) == expected_result

@pytest.mark.slow
@pytest.mark.parametrize("a,expected_result",[(1,2),(5,6)])
def test_sample2(a,expected_result):
    assert func(a,1) == expected_result

@pytest.mark.skipif(
        sys.version_info < (3,11),
        reason="requires python 3.11 or higher"
        )
def test_sample3():
    assert True
