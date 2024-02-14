from test_authorization import TestAuthorization
from data import Config

data = Config()
settings = data.read_config('config.ini')


def test_authorization_correct_username_correct_password():
    run = TestAuthorization()
    run.open_browser()
    status = run.log_in_profile(settings["Authorization"]["username_correct"],
                                settings["Authorization"]["password_correct"])
    assert status == 200, "Ошибка"
    # print("Hello")
    run.check_log_in_profile()


def test_authorization_incorrect_username_correct_password():
    run = TestAuthorization()
    run.open_browser()
    status = run.log_in_profile(settings["Authorization"]["username_incorrect"],
                                settings["Authorization"]["password_correct"])
    assert status == 401, "Ошибка"
    # print("Hello")
    run.check_log_in_profile()


def test_authorization_correct_username_incorrect_password():
    run = TestAuthorization()
    run.open_browser()
    status = run.log_in_profile(settings["Authorization"]["username_correct"],
                                settings["Authorization"]["password_incorrect"])
    assert status == 401, "Ошибка"
    # print("Hello")
    run.check_log_in_profile()
