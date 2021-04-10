from selenium.webdriver.common.by import By
from page.add_department_page import AddDepartmentPage
from page.basepage import BasePage


class ContentPage(BasePage):
    def goto_add_department(self):
        self.driver.find_element(By.XPATH, '//*[@class="member_colLeft_top_addBtn"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartmentPage(self.driver)

