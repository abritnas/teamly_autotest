from test_authorization import TestAuthorization
from data import Config
from create_driver import Browser
import time

data = Config()
settings = data.read_config('config.ini')
config_username = settings["Authorization"]["username_correct"]
config_password = settings["Authorization"]["password_correct"]


def test_authorization_correct_username_correct_password():
    run = TestAuthorization()
    browser = Browser()
    browser.create_browser('https://app.teamly.ru/auth/sign-in')
    time.sleep(3)
    run.log_in_profile(settings["Authorization"]["username_correct"],
                       settings["Authorization"]["password_correct"], browser.get_browser())
    [status, path, body] = browser.get_status_and_response('/api/v1/auth/user/login')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"
    return browser


def test_authorization_incorrect_username_correct_password():
    run = TestAuthorization()
    browser = Browser()
    browser.create_browser('https://app.teamly.ru/auth/sign-in')
    time.sleep(3)
    run.log_in_profile(settings["Authorization"]["username_incorrect"],
                       settings["Authorization"]["password_correct"], browser.get_browser())
    [status, path, body] = browser.get_status_and_response('/api/v1/auth/user/login')
    assert status == 401, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"


def test_authorization_correct_username_incorrect_password():
    run = TestAuthorization()
    browser = Browser()
    browser.create_browser('https://app.teamly.ru/auth/sign-in')
    time.sleep(3)
    run.log_in_profile(settings["Authorization"]["username_correct"],
                       settings["Authorization"]["password_incorrect"], browser.get_browser())
    [status, path, body] = browser.get_status_and_response('/api/v1/auth/user/login')
    assert status == 401, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"
