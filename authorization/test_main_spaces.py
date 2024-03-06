from test_list_of_spaces import TestSpaces
from authorization import test_authorization
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../../../authorization'))
from test_main_authorization import test_authorization_correct_username_correct_password


def test_open_page():
    run = TestSpaces()
    test_authorization_correct_username_correct_password()
