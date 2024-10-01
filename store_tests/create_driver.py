import requests
import json
from seleniumwire import webdriver


class Browser:
    browser = None

    def create_browser(self, link):
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        self.browser.set_window_size(1920, 1080)
        return self.browser

    def get_browser(self):
        return self.browser

    def get_status_and_response(self, path):
        path_from_browser = None
        status_from_browser = None
        body_from_browser = None
        for request in self.browser.requests:
            if request.response:
                # print(request.path) для вывода всех запросов
                if request.path == path:
                    status_from_browser = request.response.status_code
                    path_from_browser = request.path
                    body_from_browser = request.body
        return status_from_browser, path_from_browser, body_from_browser

    def get_cookies(self):
        cookies = self.browser.get_cookies()
        return cookies

    def add_cookies(self):
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                self.browser.add_cookie(cookie)
        self.browser.refresh()
