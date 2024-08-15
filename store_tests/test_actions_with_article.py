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

    def create_article(self, browser):
        self.br = browser
        self.t = True
        # кнопка создать в сайдбаре
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[1]/aside/div['
                                                          '2]/footer/ul/li[1]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_article")
            self.t = False
        # button spacing-medium create-dropdown__actions-item create-dropdown__actions-item
