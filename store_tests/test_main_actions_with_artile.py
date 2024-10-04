import time

from test_list_of_spaces import Space
from test_main_spaces import test_creation_of_new_space
# from create_driver import Browser
# from store_tests import test_authorization
from test_main_authorization import test_authorization_correct_username_correct_password
import json
from test_actions_with_article import Article


def test_create_space_and_article_and_publish():
    [id_space, browser] = test_creation_of_new_space()
    run = Article()
    time_for_search = run.create_draft(browser.get_browser())
    # time.sleep(6)
    assert time_for_search
    time_for_search = run.publication_of_article()
    assert time_for_search
    time.sleep(4)


def test_create_space_and_article_and_change_title_and_publish():
    [id_space, browser] = test_creation_of_new_space()
    run = Article()
    time_for_search = run.create_draft(browser.get_browser())
    # time.sleep(6)
    assert time_for_search
    time_for_search = run.change_title()
    assert time_for_search
    time.sleep(4)
    time_for_search = run.publication_of_article()
    [status, path, body] = browser.get_status_and_response('/publish')
    assert status == 200, "Ошибка"
    assert path == '/publish', "Другой путь"
    assert time_for_search


