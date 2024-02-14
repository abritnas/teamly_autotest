
from seleniumwire import webdriver


class Browser:
    browser = None

    def create_browser(self, link):
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        return self.browser
