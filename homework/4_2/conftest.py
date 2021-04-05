"""
__author__ = 'zhengwan'
__time__ = '2021/4/5 21:30 晚上'
"""
import pytest

from calculator import Calculator


@pytest.fixture()
def calculate():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")