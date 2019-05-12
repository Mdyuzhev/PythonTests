# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.add_new_group()
    app.group.fill_group_form(Group(name="group", header="header", footer="footer"))
    app.group.submit_new_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.add_new_group()
    app.group.fill_group_form(Group(name="", header="", footer=""))
    app.group.submit_new_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()
