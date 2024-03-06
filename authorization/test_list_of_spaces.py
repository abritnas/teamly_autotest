import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


class TestSpaces:
    br = None

    def open_list_of_spaces(self):
        pass