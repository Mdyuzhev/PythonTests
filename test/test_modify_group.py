# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.modify_first_group()
    app.group.fill_group_form(Group(name="new group"))
    app.group.update_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()


def test_modify_group_header(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.modify_first_group()
    app.group.fill_group_form(Group(header="new header"))
    app.group.update_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()


def test_modify_group_footer(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.modify_first_group()
    app.group.fill_group_form(Group(footer="new footer"))
    app.group.update_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()


def test_modify_all_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.modify_first_group()
    app.group.fill_group_form(Group(name="new group1", header="new header1", footer="new footer1"))
    app.group.update_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()
