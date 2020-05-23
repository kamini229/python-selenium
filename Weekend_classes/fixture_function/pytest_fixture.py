import pytest

class TestSample:

    @pytest.fixture() # we have to add fixture
    def setUp(self):  # this particular function will execute for each testcase
        print("Initializing x =10 and y =20")  # before each testcase
        yield   # this will execute after each test case
        print("Operation successfully!!")

    def test_add(self, setUp):
        print("Test  add functionality")

    def test_sub(self, setUp):
        print("Test  sub functionality")

    def test_mul(self, setUp):
        print("Test  mul functionality")

    def test_div(self, setUp):
        print("Test  div functionality")