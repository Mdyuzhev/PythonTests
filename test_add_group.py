# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from group import Group


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.goTo_groups_page(driver)
        self.add_new_group(driver)
        self.fill_group_form(driver, Group(name="group", header="header", footer="footer"))
        self.submit_new_group(driver)
        self.back_to_group_page(driver)
        self.goTo_home(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.goTo_groups_page(driver)
        self.add_new_group(driver)
        self.fill_group_form(driver, Group(name="", header="", footer=""))
        self.submit_new_group(driver)
        self.back_to_group_page(driver)
        self.goTo_home(driver)
        self.logout(driver)

    def goTo_home(self, driver):
        driver.find_element_by_link_text("home").click()

    def back_to_group_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def submit_new_group(self, driver):
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, driver, group):
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def add_new_group(self, driver):
        driver.find_element_by_name("new").click()

    def goTo_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
