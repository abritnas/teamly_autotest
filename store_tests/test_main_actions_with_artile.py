from test_list_of_spaces import TestSpaces
from test_main_spaces import test_creation_of_new_space
# from create_driver import Browser
# from store_tests import test_authorization
from test_main_authorization import test_authorization_correct_username_correct_password
import json
from test_actions_with_article import TestActionsArticle


def test_create_space_and_article():
    [id_space, browser] = test_creation_of_new_space()
    run = TestActionsArticle()
    run.create_article(browser)

