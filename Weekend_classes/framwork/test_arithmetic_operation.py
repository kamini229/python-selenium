import pytest

def test_add():
    x = 45
    y = 50
    r = x + y
    print(r)
    assert r == 95


def testProduct():
    x = 50
    y = 50
    r = x * y
    print(r)
    assert r == 2500


def testSubtract():
    x = 45
    y = 50
    r = x - y
    print(r)
    assert r == 5
