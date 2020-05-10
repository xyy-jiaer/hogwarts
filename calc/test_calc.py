import pytest

from calc.calc import Calc


@pytest.fixture(scope='function', autouse=True)
def chu():
    calc = Calc()
    print('setup')
    return calc


class TestCal:
    @pytest.mark.parametrize('a, b, res', [(1, 3, 4), (2, 0, 2)])
    def test_add1(self, a, b, res, chu):
        print('\nhh')
        print(chu)
        assert chu.add(a, b) == res

    @pytest.mark.parametrize('a, b, res', [(1, 1, 1), (2, 1, 2)])
    def test_div(self, chu, a, b, res):
        print('\nha')
        assert chu.div(a, b) == res
