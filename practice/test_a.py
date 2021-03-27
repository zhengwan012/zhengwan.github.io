import pytest
import yaml


def func(x):
    return x+1


'''
直接参数化解析yaml文件
参数化的变量可以为字符串'a,b'、列表['a', 'b']、元组('a', 'b')
'''


@pytest.mark.parametrize('a,b', yaml.safe_load(open('data.yaml')))
def test_answer(a, b):
    assert func(a) == b


'''
被指定为pytest.fixture的函数可以被其它函数直接作为参数引用，
并且将通过该函数名返回该函数需要返回的值
'''


@pytest.fixture()
def login():
    print('登录操作')
    username = 'nicky'
    return username


class TestDemo:
    def test_a(self, login):
        print(f'test_a username = {login}')

    def test_b(self):
        print('test_b')

    def test_c(self, login):
        print('test_c username = {login}')


if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo', '-v'])
