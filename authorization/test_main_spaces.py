from test_list_of_spaces import TestSpaces
from authorization import test_authorization

from test_main_authorization import test_authorization_correct_username_correct_password


# TODO придумать как быть с бразером, как его передавать, написан геттер для броузер, теперь надо придумать как его
#  вызвать

def test_open_page():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    run.open_list_of_spaces(browser)