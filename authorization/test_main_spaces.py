from test_list_of_spaces import TestSpaces

from test_main_authorization import test_authorization_correct_username_correct_password


def open_page():
    run = TestSpaces()
    test_authorization_correct_username_correct_password()
