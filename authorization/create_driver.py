import requests
import json
from seleniumwire import webdriver


class Browser:
    browser = None

    def create_browser(self, link):
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        return self.browser

    def get_browser(self):
        return self.browser

    def get_status_and_response(self, path):
        path_from_browser = None
        status_from_browser = None
        for request in self.browser.requests:
            if request.response:
                if request.path == path:
                    # print(request.response.status_code)
                    # print(request.path)
                    status_from_browser = request.response.status_code
                    path_from_browser = request.path
                # print(request.response.status_code, request.path)
        # print(len(self.br.requests))
        # self.status = self.br.requests[-1].response.status_code
        # self.path = self.br.requests[-1].path
        return status_from_browser, path_from_browser



