from homework.pageobject.page.basepage import BasePage
from homework.pageobject.page.content_page import ContentPage


class MainPage(BasePage):
    def goto_content(self):
        self.driver.find_element_by_id("menu_contacts").click()
        return ContentPage(self.driver)