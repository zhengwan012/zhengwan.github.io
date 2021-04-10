from selenium.webdriver.common.by import By
from time import sleep
from homework.pageobject.page.basepage import BasePage


class AddDepartmentPage(BasePage):
    def add_department(self, name):
        self.driver.find_element(By.CSS_SELECTOR, '[name=name]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688852051058674_anchor']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id=__dialog__MNDialog__] div>div>a:nth-child(1)").click()
        sleep(3)
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-node.js_editable.jstree-leaf")
        name_list = [i.text for i in ele_list]
        return name_list
