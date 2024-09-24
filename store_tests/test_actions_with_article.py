from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestActionsArticle:
    br = None
    t = None

    def open_space_with_link(self):
        pass

    def open_space_in_list_of_spaces(self):
        pass

    def create_draft(self, browser):
        self.br = browser
        self.t = True
        # кнопка создать в сайдбаре
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div/div/div['
                                                          '1]/aside/div[2]/footer/ul/li[1]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_article")
            self.t = False
        time.sleep(5)
        # выбираем новая статья в  поп-апе после плюсика
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.CSS_SELECTOR, 'body>div:nth-child(13)>div>ul>li:nth-child(1)>button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_article выбираем новая статья в  поп-апе после плюсика")
            self.t = False
        # # кнопка создать в сайдбаре
        # try:
        #     element = WebDriverWait(self.br, 10).until(
        #         # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
        #         ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div/div/div['
        #                                                   '1]/aside/div[2]/div/div[2]/div[1]/div['
        #                                                   '2]/div/div/div/div/div[2]/div/div/button'))
        #     )
        #     element.click()
        # except TimeoutException:
        #     print("Time in create_article")
        #     self.t = False

    def publication_of_article(self):
        self.t = True
        # кнопка создать в сайдбаре
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '2]/div/div/div/div[3]/div[3]/div[3]/div[1]/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_article")
            self.t = False
