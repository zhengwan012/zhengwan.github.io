
"""
__author__ = 'zhengwan'
__time__ = '2021/4/5 21:30 晚上'
"""
import allure
import pytest
import yaml
import subprocess
import os


# pip install pyyaml
def get_datas():
    path = os.path.dirname(os.path.dirname(__file__))
    yaml_path = '/'.join(path.split('\\')) + '/data/calc.yml'
    with open(yaml_path) as f:
        datas = yaml.safe_load(f)
    print('datas:', datas)
    return datas


@allure.feature("测试计算器")
class TestCal:

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'])
    @allure.story("测试相加功能--整数")
    def test_add_int(self, calculate, a, b, expect):
        assert expect == calculate.add(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'])
    @allure.story("测试相加功能--浮点数")
    def test_add_float(self, calculate, a, b, expect):
        assert expect == round(calculate.add(a, b), 2)

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_character']['datas'])
    @allure.story("测试相加功能--字符")
    def test_add_character(self, calculate, a, b, expect):
        assert expect == calculate.add(a, b)

    @allure.story("测试相除功能--除数不能为0")
    def test_div(self, calculate):
        # try:
        #     cal.div(1, 0)
        # except ZeroDivisionError:
        #     print("除数为0")
        with pytest.raises(ZeroDivisionError):
            calculate.div(1, 0)

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_int']['datas'])
    @allure.story("测试相除功能--整数")
    def test_div_int(self, calculate, a, b, expect):
        assert expect == calculate.div(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_float']['datas'])
    @allure.story("测试相除功能--浮点数")
    def test_div_float(self, calculate, a, b, expect):
        assert expect == round(calculate.div(a, b), 2)