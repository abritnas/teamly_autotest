import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


class Space:
    br = None
    t = None

    def open_page_list_of_spaces(self, browser):
        self.br = browser
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/header/div/div/div/div/nav/ul/li['
                                                          '2]/a/div'))
            )
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Time in open_page_list_of_spaces")
            self.t = False
        return self.t

    def check_open_page_list_of_spaces(self):
        answer = None
        self.t = True
        pattern = 'https://default.stage-wiki.vpool.qsoft.ru/space/list/all'
        try:
            if WebDriverWait(self.br, 10).until(ec.url_matches(pattern)):
                answer = True
        except TimeoutException:
            answer = False
            print("Time in check_open_page_list_of_spaces")
            self.t = False
        return answer, self.t

    def create_new_space(self, name_space):
        answer = None
        self.t = True
        # нажать на папку для создания пространства
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div/div[2]/div['
                                                          '2]/div/div[2]/ul/li[3]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # написать название
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.ID, 'create-space-popup-title'))
            )
            element.send_keys(name_space)
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка закрепить в списке пространств
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div['
                                                          '3]/label/span[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка продолжить после названия
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/form/div[4]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка продолжить после настроек
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/form/div[2]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка создать после выбора шаблона с нуля
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/form/div[2]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # возвращаем название пространства
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/main/div/div/div/div/div['
                                                          '1]/aside/div[2]/header/div[1]/div[2]/h3'))
            )
            answer = element
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        return answer, self.t

    # TODO надо придумать, что сделать с удалением пространства. есть 3 варианта: 1) сначала использовать поиск,
    #  потом удаление, 2) либо использовать айдт пространства, и как-то через список пространств удалять 3) удалять
    #  по айди через ссылку, и там дальше через само пространство

    # комментарий к to.do по итогу сделала удаление через страницу пространства - остаемся на странице пространства,
    # затем в настойки и затем удаляем
    def delete_space_from_space_page(self):
        # идем в настройки пространства
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div/div/div['
                                                          '1]/aside/div[2]/div/div[2]/div[1]/div['
                                                          '2]/div/div/div/ul/li[3]/a'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # ищем кнопку удалить
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div/div/div['
                                                          '2]/div[2]/div/div[1]/div/div[2]/div/div['
                                                          '2]/div/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка "подтвердить в поп-апе"
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        return self.t

    def favorite_space(self):
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[3]/div/div['
                                                          '2]/div/div/div/div/ul/li[1]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        return self.t

    def archive_space(self):
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div/div[2]/div['
                                                          '3]/div/div[2]/div/div/div/div/ul/li[2]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '1]/div/div/div/div/ul/li[3]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '2]/div/form/div/div/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div/div[3]/button[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        time.sleep(2)
        return self.t

    def get_permissions_in_space(self):
        self.t = True
        # шестеренка
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div/div[2]/div['
                                                          '3]/div/div[2]/div/div/div/div/ul/li[2]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # таба с правами
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '1]/div/div/div/div/ul/li[2]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # селект для пользователя
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '1]/div[1]/div/div[1]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # выбор пользователя
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '1]/div[1]/div/div[2]/div/div/ul/li[1]/label/span[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка "Добавить"
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '1]/div[1]/div[2]/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        # кнопка "сохранить"
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/form/div['
                                                          '2]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        return self.t
