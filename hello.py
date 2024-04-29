
# https://velog.io/@kimdy0915/Selenium%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%A7%80%EB%8F%84-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://google.com')

print(driver.page_source)
driver.quit()