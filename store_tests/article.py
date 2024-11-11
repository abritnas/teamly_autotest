from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Article:
    br = None
    t = None
    id = None

    def open_space_with_link(self):
        pass

    def get_article_id(self):
        url = self.br.currect_url

        pass

    def create_draft(self, browser):
        self.br = browser
        self.t = True
        # кнопка создать в сайдбаре
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/div/div/div/div/div['
                                                          '1]/aside/div[2]/footer/ul/li[1]/div/div/button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_article")
            self.t = False
        # time.sleep(5)
        # выбираем новая статья в поп-апе после плюсика
        try:
            element = WebDriverWait(self.br, 15).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(6) > div > ul > li:nth-child(1) > '
                                                             'button'))
            )
            element.click()
            time.sleep(5)  # для загрузки страницы черновика
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
        return self.t

    def publication_of_article(self):
        # self.br = browser
        self.t = True
        # кнопка опубликовать
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.CSS_SELECTOR, '#app > div.layout > main > div > div > div > div > '
                                                                 'div.space-detail-page__content > div > '
                                                                 'div.segment.article-detail__content > div > '
                                                                 'div.article-header.article-content__row > '
                                                                 'div.article-header__content > '
                                                                 'div.article-toolbar.article-header__toolbar > '
                                                                 'div.article-toolbar__item.publish-button > button'))
            )
            element.click()
        except TimeoutException:
            print("Time in create_article при публикации статьи")
            self.t = False
        return self.t

    def change_title(self):
        self.t = True
        # меняем заголовок статьи
        try:
            element = WebDriverWait(self.br, 10).until(
                # ec.presence_of_element_located((By.CLASS_NAME, "article-detail-sidebar__action grow"))
                ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div['
                                                          '1]/main/div/div/div/div/div[2]/div/div/div/div['
                                                          '4]/div/div/div/div[6]/div/div[2]/div[1]/div/div['
                                                          '1]/div/div[2]/p'))
            )
            element.click()
            element.send_keys('Новая статья')
        except TimeoutException:
            print("Time in create_article при изменении заголовка")
            self.t = False
        return self.t
