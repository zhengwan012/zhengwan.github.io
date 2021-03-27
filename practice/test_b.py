'''
1、执行用例:pytest test_b.py --alluredir=./result/b
2、直接生成并打开报告：allure serve ./result/b
3、生成报告：allure generate ./result/b -o ./report/ --clean(覆盖路径加--clean)
   打开报告：allure open -h 127.0.0.1 -p 8883 ./report/
4、pytest test_b.py --allure-features "登录模块" ，只执行登录模块
   pytest test_b.py --allure-stories "登录成功" ，只执行登录成功
'''

import pytest
import allure


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录： 测试用例， 登陆成功")

    @allure.story("登录失败")
    def test_login_fail_a(self):
        print("这是登录： 测试用例， 登陆成功")

    @allure.story("用户名缺失")
    def test_login_fail_b(self):
        print("用户名缺失")

    @allure.story("密码缺失")
    def test_login_fail_c(self):
        with allure.step("点击用户名"): # 标注测试步骤
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")

    @allure.story("登录失败")
    def test_login_fail_d(self):
        print("这是登录： 测试用例， 登录失败")


if "__name__" == "__main__":
    pytest.main()
