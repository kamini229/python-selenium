from framwork.arithmetic_module import ArithmeticClass
import pytest


class TestArithmeticClass:

    @pytest.mark.run(order=4)    # for ordering
    def test_add_functionality(self):
        aclass = ArithmeticClass(40, 50)
        r = aclass.add()
        assert r == 90

    @pytest.mark.run(order=1)
    def test_sub_functionality(self):
        aclass = ArithmeticClass(40, 50)
        r = aclass.sub()
        assert r == 90

    @pytest.mark.run(order=3)
    def test_mul_functionality(self):
        aclass = ArithmeticClass(40, 50)
        r = aclass.mul()
        assert r == 2000

    @pytest.mark.run(order=2)
    def test_div_functionality(self):
        aclass = ArithmeticClass(100, 50)
        r = aclass.div()
        assert r == 2