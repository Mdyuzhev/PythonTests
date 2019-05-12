# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.add_new_contact()
    app.contact.fill_contact_form(Contact(firstname="first", middlename="middle"))
    app.contact.submit_contact()
    app.contact.go_to_home_page()
    app.session.logout()



