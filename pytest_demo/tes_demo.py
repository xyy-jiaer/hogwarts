import pytest


def setup_module():
    print('module')

def setup_function():
    print('hh')

@pytest.mark.happypytw
def test_demo_1():
    print('fg')

def test_demo_2():
    print('ff')


class TestClass:
    def test_demo_3(self):
        print('haha')

    def test_zero(self):
        with pytest.raises(ZeroDivisionError):
            print(1/1)