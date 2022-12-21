from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    d = browser.find_element  # шобы не писать каждый раз :) мы же автоматизируем свою работу везде

    select = Select(d(By.CSS_SELECTOR, '#dropdown'))
    for i in range(100):
        select.select_by_value(str(i))
        time.sleep(0.3) # если убрато то садамия начинается ))

    d(By.CSS_SELECTOR, '.btn.btn-default').click()

finally:
    time.sleep(20)
    browser.quit()