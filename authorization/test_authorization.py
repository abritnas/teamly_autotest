from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestAuthorization:
    status = None
    path = None

    def log_in_profile(self, config_username, config_password, browser):
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
            # [self.status, self.path] = browser.get_status_and_response('/api/v1/auth/user/login')
            # for request in browser.requests:
            #     if request.response:
            #         if request.path == '/api/v1/auth/user/login':
            #             # print(request.response.status_code)
            #             # print(request.path)
            #             self.status = request.response.status_code
            #             self.path = request.path
            #         # print(request.response.status_code, request.path)
            # # print(len(self.br.requests))
            # # self.status = self.br.requests[-1].response.status_code
            # # self.path = self.br.requests[-1].path
            return self.status, self.path
        except TimeoutException:
            print("Loading took too much time!")
        # try:
        #     element = WebDriverWait(self.br, 10).until(
        #         ec.presence_of_element_located((By.XPATH,
        #                                         '/html/body/div/div[1]/div/div/div/div/ul/li[1]/a/div'))
        #     )
        #     print('True')
        #     element.click()
        # except TimeoutException:
        #     print("Loading took too much time!")

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
