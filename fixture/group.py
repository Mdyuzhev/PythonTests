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

    def update_group(self):
        driver = self.app.driver
        driver.find_element_by_name("update").click()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value(group, "group_name", group.header)
        self.change_field_value(group, "group_header", group.header)
        self.change_field_value(group, "group_footer", group.footer)

    def change_field_value(self, group, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def add_new_group(self):
        driver = self.app.driver
        driver.find_element_by_name("new").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.select_first_group()
        driver.find_element_by_xpath("(//input[@name='delete'])[2]").click()

    def modify_first_group(self):
        driver = self.app.driver
        self.select_first_group()
        driver.find_element_by_name("edit").click()
