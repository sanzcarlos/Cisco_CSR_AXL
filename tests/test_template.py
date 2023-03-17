# content of test_sample.py
import pytest

def func(a,b):
    return a + b

@pytest.fixture()
def cucmserver():
    return cucm(
        cucmserver="192.168.80.230",
        username="ccmadministrator",
        password="NTTvoip2020.",
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