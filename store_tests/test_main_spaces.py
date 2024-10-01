from test_list_of_spaces import TestSpaces
# from create_driver import Browser
# from store_tests import test_authorization
from test_main_authorization import test_authorization_correct_username_correct_password
import json


def test_creation_of_new_space():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    # [answer, time] = run.check_open_page_list_of_spaces()
    # assert answer
    # assert time
    [answer, time] = run.create_new_space('Новое пространство от автотеста для работы в редакторе')
    assert answer.text == 'Новое пространство от автотеста для работы в редакторе'
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/wiki/ql/space')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/wiki/ql/space', "Другой путь"
    body = body.decode().replace("'", '"')
    data = json.loads(body)
    data = data["query"]
    data = data["__filter"]
    id_space = data["id"]
    return id_space, browser


def test_creation_of_new_space_and_delete_after_creation():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    # [answer, time] = run.check_open_page_list_of_spaces()
    # assert answer
    # assert time
    [answer, time] = run.create_new_space('Новое пространство от автотеста')
    assert answer.text == 'Новое пространство от автотеста'
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/wiki/ql/space')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/wiki/ql/space', "Другой путь"
    body = body.decode().replace("'", '"')
    data = json.loads(body)
    data = data["query"]
    data = data["__filter"]
    space_id = data["id"]
    time = run.delete_space_from_space_page()
    assert time
    # path_path = '/api/v1/space/' + space_id
    # проверка что вернулись на страницу "Список пространств"
    path_path = '/api/v1/wiki/ql/spaces'
    [status, path, body] = browser.get_status_and_response(str(path_path))
    # print(path)
    # print(path_path)
    assert path == path_path, "Другой путь"
    assert status == 200, "Удаление прошло некорректно "


def test_creation_and_make_favorites():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    [answer, time] = run.check_open_page_list_of_spaces()
    assert answer
    assert time
    [answer, time] = run.create_new_space('Новое избранное пространство от автотеста')
    assert answer.text == 'Новое избранное пространство от автотеста'
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/wiki/ql/space')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/wiki/ql/space', "Другой путь"
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    # Todo тут надо переделать функцию по добавлению пространства в избранные, потому что сейчас код ищет первое
    #  пространство в списке и его не находит, поэтому тест падает

    time = run.favorite_space()
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/favorites')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/favorites', "Другой путь"


def test_creation_of_new_space_and_archive():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    [answer, time] = run.check_open_page_list_of_spaces()
    assert answer
    assert time
    [answer, time] = run.create_new_space('Новое архивированное пространство от автотетста')
    assert answer.text == 'Новое архивированное пространство от автотетста'
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
    time = run.archive_space()
    assert time
    path_path = '/api/v1/space/' + id_article + '/archive'
    [status, path, body] = browser.get_status_and_response(path_path)
    assert status == 200, "Ошибка"
    assert path == path_path, "Другой путь"


def test_creation_of_new_space_and_get_permissions():
    run = TestSpaces()
    browser = test_authorization_correct_username_correct_password()
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    [answer, time] = run.check_open_page_list_of_spaces()
    assert answer
    assert time
    [answer, time] = run.create_new_space('Новое пространство от автотетста')
    assert answer.text == 'Новое пространство от автотетста'
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/wiki/ql/space')
    assert status == 200, "Ошибка"
    assert path == '/api/v1/wiki/ql/space', "Другой путь"
    time = run.open_page_list_of_spaces(browser.get_browser())
    assert time
    time = run.get_permissions_in_space()
    assert time
    [status, path, body] = browser.get_status_and_response('/api/v1/wiki/ql/permissions')
    assert status == 200, status
    assert path == '/api/v1/wiki/ql/permissions', "Другой путь"
