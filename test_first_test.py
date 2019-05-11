# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_app_dynamics_job(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.add_new_contact(driver)
        self.fill_contact_form(driver, "first", "middle")
        self.submit_contact(driver)
        self.go_to_home_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def go_to_home_page(self, driver):
        driver.find_element_by_link_text("home page").click()

    def submit_contact(self, driver):
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, driver, firstname, middlename):
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(middlename)

    def add_new_contact(self, driver):
        driver.find_element_by_link_text("add new").click()

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
