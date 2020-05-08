# coding=utf-8
import pytest


# @pytest.fixture(autouse=True)
# def login():
#     print("哈哈登录")
#     return 12


def test_case1(login):
    print("case1 需要登录")
    print(login)


def test_case2():
    print("case2 不需要登录")
    # print(login)


def test_search1():
    print('test_search1')


def test_search2():
    print('test_search2')


if __name__ == '__main__':
    pytest.main(['-s', 'test_pytest_fixture.py'])