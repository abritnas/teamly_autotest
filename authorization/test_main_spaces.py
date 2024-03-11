from test_list_of_spaces import TestSpaces
# from create_driver import Browser
# from authorization import test_authorization

from test_main_authorization import test_authorization_correct_username_correct_password


# TODO добавить проверку на время, потому что сейчас у меня тест проходит даже если элемент не был найден надо
#  сделать assert

def test_creation_of_new_space():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    run.open_page_list_of_spaces(browser.get_browser())
    answer = run.check_open_page_list_of_spaces()
    assert answer
    answer = run.create_new_space()
    assert answer.text == 'Новое пространство от автотеста'
    run.open_page_list_of_spaces(browser.get_browser())
    run.delete_space()
