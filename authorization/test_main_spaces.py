from test_list_of_spaces import TestSpaces
# from create_driver import Browser
# from authorization import test_authorization
from test_main_authorization import test_authorization_correct_username_correct_password
import json


def test_creation_of_new_space():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    [answer, time] = run.check_open_page_list_of_spaces()
    assert answer
    assert time
    [answer, time] = run.create_new_space()
    assert answer.text == 'Новое пространство от автотеста'
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/wiki/ql/space')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/wiki/ql/space', "Другой путь"
    body = body.decode().replace("'", '"')
    data = json.loads(body)
    data = data["query"]
    data = data["__filter"]
    id_article = data["id"]
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    time = run.delete_space()
    assert time
    path_path = '/api/v1/space/' + id_article
    [status, path, body] = browser.get_status_and_response(str(path_path))
    assert status == 200, "Ошибка"
    assert path == path_path, "Другой путь"
