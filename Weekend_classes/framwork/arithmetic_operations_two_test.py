import pytest


def test_add():
    x = 45;
    y = 50;
    r = x + y
    assert r == 96


def test_product():
    x = 50;
    y = 50;
    r = x * y
    assert r == 2500


def subtract():
    x = 45;
    y = 50;
    r = x - y
    assert r == -5


# o = add()
# if (o == 95):
#     print("Its pass")
# else:
#     print("its fail")
#
# o = product()
# if (o == 1500):
#     print("Its pass")
# else:
#     print("its fail")
#
# o = subtract()
# if (o == 5):
#     print("Its pass")
# else:
#     print("its fail")