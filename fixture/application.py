from selenium import webdriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def goTo_home(self):
        driver = self.driver
        driver.find_element_by_link_text("home").click()



    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
