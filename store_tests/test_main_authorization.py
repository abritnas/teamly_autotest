from authorization import Authorization
from config import Config
from browser import Browser
import time
import json

data = Config()
settings = data.read_config('config_production.ini')
# config_username_correct = settings["Authorization"]["username_correct"]
# config_password_correct = settings["Authorization"]["password_correct"]
config_link = settings["Authorization"]["link_authorization"]


def test_authorization_correct_username_correct_password():
    run = Authorization()
    browser = Browser()
    browser.create_browser(config_link)
    time.sleep(3)
    run.log_in_profile(settings["Authorization"]["username_correct"],
                       settings["Authorization"]["password_correct"], browser.get_browser())
    [status, path] = browser.get_status_and_response('/api/v1/auth/user/login')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"
    # browser.get_cookies()
    # browser.add_cookies()
    # time.sleep(3)
    return browser


def test_authorization_incorrect_username_correct_password():
    run = Authorization()
    browser = Browser()
    browser.create_browser(config_link)
    time.sleep(3)
    run.log_in_profile(settings["Authorization"]["username_incorrect"],
                       settings["Authorization"]["password_correct"], browser.get_browser())
    [status, path] = browser.get_status_and_response('/api/v1/auth/user/login')
    assert status == 401, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"


def test_authorization_correct_username_incorrect_password():
    run = Authorization()
    browser = Browser()
    browser.create_browser(config_link)
    time.sleep(3)
    run.log_in_profile(settings["Authorization"]["username_correct"],
                       settings["Authorization"]["password_incorrect"], browser.get_browser())
    [status, path] = browser.get_status_and_response('/api/v1/auth/user/login')
    assert status == 401, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"
