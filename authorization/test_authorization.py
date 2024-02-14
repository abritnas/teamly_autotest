from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from create_driver import Browser
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from data import Config
from seleniumwire import webdriver


class TestAuthorization:
    br = None

    def open_browser(self):
        browser = Browser()
        self.br = browser.create_browser('https://app.teamly.ru/auth/sign-in')
        time.sleep(3)
        # for request in self.br.requests:
        #     if request.response:
        #         print(request.response.status_code, request.path)

    def log_in_profile(self, config_username, config_password):
        data = Config()
        settings = data.read_config('config.ini')
        # br = browser.create_browser('https://app.teamly.ru/auth/sign-up')
        # br.find_element(By.ID, 'email').send_keys('evlanova.arisha@mail.ru')
        # self.br.find_element(By.LINK_TEXT, 'https://app.teamly.ru/auth/sign-in').click()
        # time.sleep(2)
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.ID, "username"))
            )
            element.send_keys(config_username)
        except TimeoutException:
            print("Loading took too much time!")
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.ID, 'password'))
            )
            element.send_keys(settings["Authorization"]["password"])
        except TimeoutException:
            print("Loading took too much time!")
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div[1]/main/div/div/div['
                                                '2]/article/section/form/button/span'))
            )
            element.click()
            status = self.br.requests[-1].response.status_code
            return status
        except TimeoutException:
            print("Loading took too much time!1")
            # for request in self.br.requests:
            #     if request.response:
            #         print(request.response.status_code, request.path)

    def check_log_in_profile(self):
        # print()
        # print(self.br.current_url)
        # time.sleep(5)
        pattern = 'https://arina-best.teamly.ru/'
        try:
            element = WebDriverWait(self.br, 10).until(ec.url_matches(pattern))
            # print("okay")
            # print(element)
        except TimeoutException:
            print("Loading took too much time1!")
        self.br.quit()
