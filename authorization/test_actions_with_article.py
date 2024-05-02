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
