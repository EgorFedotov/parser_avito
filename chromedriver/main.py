# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent
# from multiprocessing import Pool


# useragent = UserAgent()
# url = 'https://www.avito.ru/arzamas/tovary_dlya_kompyutera/komplektuyuschie/videokarty'
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.random}")
# url_list = ["https://www.avito.ru/arzamas/tovary_dlya_kompyutera/komplektuyuschie/videokarty", "https://www.avito.ru/arzamas/transport", "https://www.avito.ru/arzamas/telefony?cd=1"]



# def get_dara(url):
#     try:
#         driver = webdriver.Chrome(options=options)
#         driver.get(url=url)
#         driver.implicitly_wait(5)
#         driver.get_screenshot_as_file(f"media/{url.split('/')[2]}.png")
#         items = driver.find_elements(by='xpath', value="//div[@data-marker='item-photo']")
#         items[0].click()
#         driver.implicitly_wait(5)
#         driver.switch_to.window(driver.window_handles[1])
#         username = driver.find_element(by='xpath', value="//div[@data-marker='seller-info/name']")
#         price = driver.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
#         print(f'Имя пользователя {username.text} цена {price}')
#         driver.implicitly_wait(5)
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
#         items[1].click()
#         driver.implicitly_wait(5)
#         driver.switch_to.window(driver.window_handles[1])
#         data = driver.find_element(by='xpath', value="//span[@data-marker='item-view/item-date']")
#         print(f'Дата публикации: {data.text}')
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()

# if __name__ == '__main__':
#     p = Pool(processes=3)
#     p.map(get_dara, url_list)