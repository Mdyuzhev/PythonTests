

def test_add_group(app):

    app.group.goTo_groups_page()
    app.group.delete_first_group()
    app.group.back_to_group_page()
    app.goTo_home()

