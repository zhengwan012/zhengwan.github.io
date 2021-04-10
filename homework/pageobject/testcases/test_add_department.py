import pytest
from homework.pageobject.page.main_page import MainPage

"""
实现企业微信自动登录功能，添加部门，校验
前置条件：
复用浏览器：1、找到chrome浏览器位置，添加至环境变量
    2、确定命令启动前是否已将chrome进程都关闭
        在通过命令启动远程调试的chrome之前，需要关闭chrome有关的进程，除了chrome浏览器之外，还有chrome后台进程、浏览器插件等
        chrome设置-高级里有一项设置可以关闭掉再试一下，能解决不少后台进程问题【高级->系统->关闭Google Chrome后台继续运行后台应用】
    3、在终端执行chrome --remote-debugging-port=9222命令，会启动chrome浏览器，扫码登录企业微信即可（执行前将所有退出浏览器）
    4、启动浏览器时需要加上chrome_arg.debugger_address = '127.0.0.1:9222'，详见basepage.py
    5、调试模式启动浏览器后，通过浏览器访问127.0.0.1:9222(9222为端口号,对应之前启动命令中配置的端口号),如果页面没有报错，那么说明调试模式的浏览器启动成功
"""
class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()
        self.driver = self.main.driver

    @pytest.mark.parametrize("name", ["质量组", "qa"])
    def test_add_department(self, name):
        """
        用来测试添加部门功能
        1、跳转到通讯录页面 2、添加部门 3、获取部门列表，做断言验证
        :return:
        """
        name_list = self.main.goto_content().goto_add_department().add_department(name)
        print('name_list:', name_list)
        # 左补齐空格
        assert name.rjust(len(name)+1) in name_list

    def teardown_class(self):
        self.driver.quit()
