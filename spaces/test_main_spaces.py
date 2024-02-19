from test_list_of_spaces import TestSpaces
import os
import sys

sys.path.append(os.path.abspath('../authorization'))
import test_main_authorization
# from data import Config

# import create_driver

# sys.path.insert(1, '../../../authorization')
# import authorization.test_main_authorization
# from authorization.create_driver import Browser

data = Config()
settings = data.read_config('config.ini')
config_username = settings["Authorization"]["username_correct"]
config_password = settings["Authorization"]["password_correct"]



def test_open_page():
    run = TestSpaces()
    test_main_authorization.test_authorization_correct_username_correct_password(config_username, config_password)
