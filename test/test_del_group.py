

def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.goTo_groups_page()
    app.group.delete_first_group()
    app.group.back_to_group_page()
    app.goTo_home()
    app.session.logout()