import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from multiprocessing import Pool
import undetected_chromedriver as uc

driver = uc.Chrome()
url = 'https://www.avito.ru/arzamas/bytovaya_elektronika?cd=1&q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE'


class AvitoParse:
    def __init__(self, url:str, items:list, count_page:int = 50):
        self.url = url
        self.items = items
        self.count_page = count_page
        # self.version_chrome = version_chrome

    def start_browser(self):
        self.driver = uc.Chrome()

    def get_url(self):
        self.driver.get(self.url)

    def paginations(self):
        while self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']") and self.count_page > 0:
            self.parse_page()
            self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']").click()
            self.count_page -= 1

    def parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='item-descriptionStep']").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute('href')
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute('content')
        print(f'{name} {description} {url} {price}')

    def parse(self):
        self.start_browser()
        self.get_url()
        self.paginations()

    # def get_message_tg(srlf):
    #     pass


if __name__ == '__main__':
    AvitoParse(url=url, count_page=1, items=['iphone']).parse()