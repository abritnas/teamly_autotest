from test_authorization import Authorization
from config import Config
from browser import Browser
import time
import json

data = Config()
settings = data.read_config('config_production.ini')
config_username = settings["Authorization"]["username_correct"]
config_password = settings["Authorization"]["password_correct"]
config_link = settings["Authorization"]["link_authorization"]

run = Authorization()
browser = Browser()
browser.create_browser(config_link)
time.sleep(3)
run.log_in_profile(settings["Authorization"]["username_correct"],
                   settings["Authorization"]["password_correct"], browser.get_browser())
[status, path, body] = browser.get_status_and_response('/api/v1/auth/user/login')
# assert status == 200, "Ошибка"
# assert path == '/api/v1/auth/user/login', "Другой путь"
cook = browser.get_cookies()
# print(cook)
with open('cookies.json', 'w') as file:
    json.dump(cook, file)
