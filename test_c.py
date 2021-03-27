import allure

@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")


@allure.testcase("http://github.com", "登录用例")
def test_with_testcase():
    print("这是一条测试用例的链接，链接到测试用例")


# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}，执行命令时加上，则会将issue链接到该链接
@allure.issue("140", "这是一个issue")
def test_with_issue():
    print("这是一个issue")