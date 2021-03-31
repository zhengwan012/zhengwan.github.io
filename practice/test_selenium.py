from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        # 由于直接用driver = webdriver.Chrome()启动驱动会报如下错误
        # USB: usb_device_handle_win.cc:1056 Failed to read descriptor from node connection: 连到系统上的设备没有发挥作用
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://www.baidu.com/")
        # 隐式等待，3s内轮询查找元素，查不到则抛出异常
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, 'su').click()

        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="s_tab"]//a')) >= 1
        # 显示等待，满足wait函数的条件之后不会抛出异常，否则超过10s则会抛异常
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@id="2"]/h3/a').click()
