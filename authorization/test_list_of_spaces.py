import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from create_driver import Browser


class TestSpaces:
    br = None
    t = None

    def open_page_list_of_spaces(self, browser):
        self.br = browser
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/header/div/div/div/div[1]/nav/ul/li['
                                                          '2]/button'))
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
        pattern = 'https://arina-best.teamly.ru/space/list/all'
        try:
            if WebDriverWait(self.br, 10).until(ec.url_matches(pattern)):
                answer = True
        except TimeoutException:
            answer = False
            print("Time in check_open_page_list_of_spaces")
            self.t = False
        return answer, self.t

    def create_new_space(self):
        answer = None
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/div/div['
                                                          '2]/ul/li[2]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.ID, 'create-space-popup-title'))
            )
            element.send_keys('Новое избранное пространство от автотеста')
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div['
                                                          '3]/label/span[1]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[4]/button[2]'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
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

    def delete_space(self):
        self.t = True
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div/div[2]/div['
                                                          '3]/div/div[2]/div/div/div[1]/div/ul/li[2]/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_new_spaces")
            self.t = False
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '1]/div/div/div/div/ul/li[4]/div/div/button'))
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
                ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div['
                                                          '1]/div/div/div/div/ul/li[3]/div/div/button'))
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