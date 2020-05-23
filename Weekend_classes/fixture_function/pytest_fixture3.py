import pytest


@pytest.mark.usefixtures("setUpBeforeAll")
class TestSampleThree:

    # @pytest.fixture(scope="class")
    # def setUpBeforeAll(self):
    #     print("I will be in same file and execute before all test cases")
    #     yield
    #     print("I will be in same file and execute after all test cases")

    @pytest.fixture()
    def setUp(self):
        print("Intializing x = 10 and y = 20")
        yield
        print("Operation successfully!!")

    def test_add(self, setUp):
        print("Test add functionslity")

    def test_sub(self, setUp):
        print("Test sub functionslity")

    def test_mul(self, setUp):
        print("Test mul functionslity")

    def test_div(self, setUp):
        print("Test div functionslity")