from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Authorization:
    status = None
    path = None
    body = None
    browser = None
    time_for_search = None

    def log_in_profile(self, config_username, config_password, browser):
        self.time_for_search = True
        self.browser = browser
        # try:
        #     element = WebDriverWait(browser, 10).until(
        #         ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/main/div/div/div['
        #                                                   '2]/article/section/div[1]/button'))
        #     )
        #     element.click()
        # except TimeoutException:
        #     print("Loading took too much time! сотрудник компании")
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.ID, "username"))
            )
            element.send_keys(config_username)
        except TimeoutException:
            print("Loading took too much time! in login")
            self.time_for_search = False
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.ID, 'password'))
            )
            element.send_keys(config_password)
        except TimeoutException:
            print("Loading took too much time! in password")
            self.time_for_search = False
        try:
            element = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located((By.XPATH,
                                                '//*[@id="app"]/div[1]/main/div/div/div['
                                                '2]/article/section/form/button/span'))
            )
            element.click()
            time.sleep(2)
        except TimeoutException:
            print("Loading took too much time! search button войти")
            self.time_for_search = False
        return self.time_for_search

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
