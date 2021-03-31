import allure
import pytest
from selenium import webdriver
import time

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


@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        # 由于直接用driver = webdriver.Chrome()启动驱动会报如下错误
        # USB: usb_device_handle_win.cc:1056 Failed to read descriptor from node connection: 连到系统上的设备没有发挥作用
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(options=option)
        driver.get("http://www.baidu.com")

    with allure.step(f"输入搜索词: {test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("截图"):
        driver.save_screenshot(f"./result/{test_data1}.png")
        driver.quit()
