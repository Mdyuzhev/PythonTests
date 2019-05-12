class ContactHelper:
    def __init__(self, app):
        self.app = app

    def go_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def submit_contact(self):
        driver = self.app.driver
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        driver = self.app.driver
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)

    def add_new_contact(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
