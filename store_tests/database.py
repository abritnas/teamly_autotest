import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver


class Database:
    browser = None
    t = None
    id = None
    title = None

    def create_database(self, browser):
        self.browser = browser
        self.t = True
        # нажать на кнопку для создания тбд - кнопка "Создать" внизу сайдбара
        try:
            element = WebDriverWait(self.browser, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '1]/aside/div[2]/footer/ul/li[1]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        time.sleep(3)
        # нажать на кнопку "Умная таблица"
        try:
            element = WebDriverWait(self.browser, 15).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(6) > div > ul > li:nth-child(2) > '
                                                             'button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_database")
            self.t = False
        time.sleep(3)
        return self.t

    def change_title_database(self, browser, title):
        self.browser = browser
        self.t = True
        self.title = title
        try:
            element = WebDriverWait(self.browser, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '2]/div/div[2]/div/div[1]/div/div/p'))
            )
            element.click()
            element.send_keys(self.title)
            time.sleep(3)
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        return self.t

    def create_nested(self):
        self.t = True
        # клик для создания новой строки
        try:
            element = WebDriverWait(self.browser, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '2]/div/div[2]/div/div[2]/div[2]/div[1]/div['
                                                          '2]/div/div/div/div/div/div[3]/button[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_nested поиск клика для создания новой строки")
            self.t = False
        # написать название новой строки
        try:
            element = WebDriverWait(self.browser, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '2]/div/div[2]/div/div[2]/div[2]/div[1]/div['
                                                          '2]/div/div/div/div/div/div[3]/div/div[1]'))
            )
            element.click()
            element.send_keys("новая строка тбд")
        except TimeoutException:
            print("Time in create_nested поиск места куда вводить название новой строки")
            self.t = False
        # нажать добавить
        try:
            element = WebDriverWait(self.browser, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '2]/div/div[2]/div/div[2]/div[2]/div[1]/div['
                                                          '2]/div/div/div/div/div/div[3]/div/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_nested поиск кнопки добавить")
            self.t = False
        # нажать escape
        webdriver.ActionChains(self.browser).send_keys(Keys.ESCAPE).perform()
        time.sleep(3)
        return self.t
