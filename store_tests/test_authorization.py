from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestAuthorization:
    status = None
    path = None
    body = None

    def log_in_profile(self, config_username, config_password, browser):
        try:
            element = WebDriverWait(browser, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div['
                                                          '2]/article/section/div[1]/button'))
            )
            element.click()
        except TimeoutException:
            print("Loading took too much time! сотрудник компании")
        try:
            element = WebDriverWait(browser, 10).until(
                ec.presence_of_element_located((By.ID, "username"))
            )
            element.send_keys(config_username)
        except TimeoutException:
            print("Loading took too much time!")
        try:
            element = WebDriverWait(browser, 10).until(
                ec.presence_of_element_located((By.ID, 'password'))
            )
            element.send_keys(config_password)
        except TimeoutException:
            print("Loading took too much time!")
        try:
            element = WebDriverWait(browser, 10).until(
                ec.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div[1]/main/div/div/div['
                                                '2]/article/section/form/button/span'))
            )
            element.click()
            time.sleep(2)
        except TimeoutException:
            print("Loading took too much time!")

    def check_log_in_profile(self, browser):
        answer = None
        pattern = 'https://arina-best.teamly.ru/'
        try:
            if WebDriverWait(browser, 10).until(ec.url_matches(pattern)):
                answer = True
        except TimeoutException:
            answer = False
            if self.status != 200:
                print("Статус не 200")
            else:
                print("Loading took too much time!")
        return answer
