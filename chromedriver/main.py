import time
from selenium import webdriver
from fake_useragent import UserAgent


useragent = UserAgent()
url = 'https://www.avito.ru/arzamas/tovary_dlya_kompyutera/komplektuyuschie/videokarty'
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")


driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(5)
    items = driver.find_elements(by='xpath', value="//div[@data-marker='item-photo']")
    items[0].click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    username = driver.find_element(by='xpath', value="//div[@data-marker='seller-info/name']")
    print(f'Имя пользователя {username.text}')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()