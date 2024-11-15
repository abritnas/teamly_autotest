# import time
#
# from space import Space
from test_actions_with_space import test_creation_of_new_space
# from create_driver import Browser
# from store_tests import test_authorization
# from test_main_authorization import test_authorization_correct_username_correct_password
# import json
from database import Database


def test_create_space_and_database():
    browser = test_creation_of_new_space()
    run = Database()
    time_for_search = run.create_database(browser.get_browser())
    # time.sleep(6)
    assert time_for_search
    [status, path] = browser.get_status_and_response('/api/v1/content-database')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/content-database', "Другой путь"

