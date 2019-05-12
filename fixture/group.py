class GroupHelper:
    def __init__(self, app):
        self.app = app

    def goTo_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def back_to_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def submit_new_group(self):
        driver = self.app.driver
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        driver = self.app.driver
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_xpath("(//input[@name='delete'])[2]").click()


    def add_new_group(self):
        driver = self.app.driver
        driver.find_element_by_name("new").click()
