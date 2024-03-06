import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


class TestSpaces:
    br = None

    def open_list_of_spaces(self, browser):
        self.br = browser
        try:
            element = WebDriverWait(self.br, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/header/div/div/div/div[1]/nav/ul/li['
                                                          '2]/button'))
            )
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")
        self.br.quit()
