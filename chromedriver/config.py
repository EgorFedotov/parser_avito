from selenium.webdriver.common.by import By

class TagAvito:
    NEXT_PAGE = (By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']")
    TITLES = (By.CSS_SELECTOR, "[data-marker='item']")
    NAME = (By.CSS_SELECTOR, "[itemprop='name']")
    DESCRIPTIONS = (By.CSS_SELECTOR, "[class*='item-descriptionStep']")
    URL = (By.CSS_SELECTOR, "[data-marker='item-title']")
    PRICE = (By.CSS_SELECTOR, "[itemprop='price']")
