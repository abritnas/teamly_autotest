from test_authorization import TestAuthorization
from data import Config

data = Config()
settings = data.read_config('config.ini')
config_username = settings["Authorization"]["username_correct"]
config_password = settings["Authorization"]["password_correct"]


def test_authorization_correct_username_correct_password(config_username, config_password):
    # settings = data.read_config('config.ini')
    #  print(settings)
    #print(settings["Authorization"]["username_correct"])
    run = TestAuthorization()
    run.open_browser()
    [status, path] = run.log_in_profile(config_username, config_password)
    assert status == 200, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"
    answer = run.check_log_in_profile()
    assert answer


def test_authorization_incorrect_username_correct_password():
    run = TestAuthorization()
    run.open_browser()
    [status, path] = run.log_in_profile(settings["Authorization"]["username_incorrect"],
                                        settings["Authorization"]["password_correct"])
    assert status == 401, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"


def test_authorization_correct_username_incorrect_password():
    run = TestAuthorization()
    run.open_browser()
    [status, path] = run.log_in_profile(settings["Authorization"]["username_correct"],
                                        settings["Authorization"]["password_incorrect"])
    assert status == 401, "Ошибка"
    assert path == '/api/v1/auth/user/login', "Другой путь"
