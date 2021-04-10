from selenium import webdriver


class BasePage:
    def __init__(self, base_driver=None):
        """
        :param base_driver: 傳入driver实例对象
        """
        if base_driver is not None:
            self.driver = base_driver
        else:
            # 使用浏览器复用模式
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址，去掉则不复用浏览器
            # chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852051058673'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649520883, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1617896361,1617983801'}, {'domain': '.qq.com', 'expiry': 1910957882.973505, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_fd0abad8d40c0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '9bh6B2h_wGYcb8nAbwqoJ86sHynblUhiPaaDdq5v38MuW9FantcLC9RnzIREnY72bC6xOhD_xvrcIfx-3S6iJsoJDl7lBXs-RFI2Q5YXPJRTl4h09DdP9vZ8kuvcj5MPTjD4E4YZb6IOWQZXKV5HnTHMR_aERp7Vz3S1PtNREFaJP5QxnPnUwDF3I-M8zKh-GhT93V9wJtEjph27oa8yVoq-uhpXpIPgzLOkRFjJxwuahtiIsxy_GD6J8pXHbQU_AgrTHWk7wfx4jGCG0SNF6Q'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852051058673'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '7544591360'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '6554945494'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325012441609'}, {'domain': '.qq.com', 'expiry': 1618154672, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.400941817.1617983801'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'eiRVf2bTaB4590N9Jpw9OUT89LTbIHm7be10Yqj8yfN0m5H4PWR-HEyDEChoTFD8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3877730'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618096231.430944, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'prfoaq'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '27613129911460389'}, {'domain': '.qq.com', 'expiry': 1832824840, 'httpOnly': False, 'name': 'pt_sms_phone', 'path': '/', 'secure': False, 'value': '135******13'}, {'domain': '.qq.com', 'expiry': 1619416839, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1219306955@qq.com'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1910957882.973662, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649432344.445985, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1681140272, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.805138141.1585751893'}, {'domain': '.work.weixin.qq.com', 'expiry': 1620660286.671085, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483646.686775, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '073476958054c8603104245e8a94535f095e92d3c588cf4834c05d046a961e16'}, {'domain': '.qq.com', 'expiry': 2147483642.312964, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 's9iIH3sRQW'}, {'domain': '.qq.com', 'expiry': 1618068323, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}]
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，会在每次find 操作的时候，轮询查找该元素，超时报错
            self.driver.implicitly_wait(3)

    def find(self, locator):
        """
        解元组操作，如果有重复元素定位则可用
        :param locator:
        :return:
        """
        return self.driver.find_element(*locator)