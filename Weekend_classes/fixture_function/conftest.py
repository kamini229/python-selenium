import pytest


@pytest.fixture(scope="module")
def setUpBeforeAllTC():
    print("I will be executing before all test cases")
    yield
    print("I will be executing after all test cases")


@pytest.fixture(scope="class")
def setUpBeforeAll():
    print("I will be in same file and execute before all test cases")
    yield
    print("I will be in same file and execute after all test cases")