#coding=utf-8
import pytest


@pytest.fixture(autouse=True)
def login():
    print("哈哈登录")
    return 12


@pytest.fixture(scope='module')
def open():
    print('打开浏览器')
    yield
    print('teardown')
    print('最后关闭浏览器')