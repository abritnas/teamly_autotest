import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import json


class Space:
    browser = None
    time_for_search = None
    name = None
    id = None

    def get_space_id(self, browser1):
        self.browser = browser1
        body = self.browser.body.decode().replace("'", '"')
        data = json.loads(body)
        data = data["query"]
        data = data["__filter"]
        self.id = data["id"]
        return self.id

    def open_page_list_of_spaces(self, browser1):
        self.browser = browser1
        self.time_for_search = True
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/header/div/div/div/div/nav/ul/li['
                                                          '2]/a/div'))
            )
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Time in open_page_list_of_spaces")
            self.time_for_search = False
        return self.time_for_search

    def check_open_page_list_of_spaces(self):
        answer = None
        self.time_for_search = True
        pattern = 'https://default.stage-wiki.vpool.qsoft.ru/space/list/all'
        try:
            if WebDriverWait(self.browser, 10).until(ec.url_matches(pattern)):
                answer = True
        except TimeoutException:
            answer = False
            print("Time in check_open_page_list_of_spaces")
            self.time_for_search = False
        return answer, self.time_for_search

    def create_new_space(self, name_space):
        self.name = name_space
        answer = None
        self.time_for_search = True
        # нажать на папку для создания пространства
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div[2]/div['
                                                          '2]/div/div[2]/ul/li[3]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # написать название
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.ID, 'create-space-popup-title'))
            )
            element.send_keys(self.name)
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # кнопка закрепить в списке пространств
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div['
                                                          '3]/label/span[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # кнопка продолжить после названия
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/form/div[4]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # отключаем автопубликацию
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[1]/label[6]/span[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces в отключении автопубликации")
            self.time_for_search = False
        # кнопка продолжить после настроек
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/form/div[2]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # кнопка создать после выбора шаблона с нуля
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/form/div[2]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # возвращаем название пространства = проверка что пространство создалось с правильным названием
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div/div[4]/div/div/div/div[6]/div/div[2]/div['
                                                          '1]/div/div[1]/div/div[2]'))
            )
            answer = element
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        return answer, self.time_for_search

    # TODO надо придумать, что сделать с удалением пространства. есть 3 варианта: 1) сначала использовать поиск,
    #  потом удаление, 2) либо использовать айдт пространства, и как-то через список пространств удалять 3) удалять
    #  по айди через ссылку, и там дальше через само пространство

    # комментарий к to.do по итогу сделала удаление через страницу пространства - остаемся на странице пространства,
    # затем в настройки и затем удаляем
    def delete_space_from_space_page(self):
        # идем в настройки пространства
        self.time_for_search = True
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div/div/div['
                                                          '1]/aside/div[2]/div/div[2]/div[1]/div['
                                                          '2]/div/div/div/ul/li[3]/a'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # ищем кнопку удалить
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div/div/div['
                                                          '2]/div[2]/div/div[1]/div/div[2]/div/div['
                                                          '2]/div/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # кнопка "подтвердить в поп-апе"
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        return self.time_for_search

    def favorite_space(self):
        self.time_for_search = True
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[3]/div/div['
                                                          '2]/div/div/div/div/ul/li[1]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        return self.time_for_search

    def archive_space(self):
        self.time_for_search = True
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div/div[2]/div['
                                                          '3]/div/div[2]/div/div/div/div/ul/li[2]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '1]/div/div/div/div/ul/li[3]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '2]/div/form/div/div/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div[3]/button[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        time.sleep(2)
        return self.time_for_search

    def get_permissions_in_space(self):
        self.time_for_search = True
        # шестеренка
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div/div[2]/div['
                                                          '3]/div/div[2]/div/div/div/div/ul/li[2]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # таба с правами
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '1]/div/div/div/div/ul/li[2]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # селект для пользователя
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '1]/div[1]/div/div[1]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # выбор пользователя
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '1]/div[1]/div/div[2]/div/div/ul/li[1]/label/span[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # кнопка "Добавить"
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '1]/div[1]/div[2]/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        # кнопка "сохранить"
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '2]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.time_for_search = False
        return self.time_for_search
