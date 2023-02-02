from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_input = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_input.send_keys("Ivan")
    second_input = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    second_input.send_keys("Petrov")
    third_input = browser.find_element(By.CSS_SELECTOR,'input[name="email"]')
    third_input.send_keys("fff@ff.fu")
    
    elemento = browser.find_element(By.CSS_SELECTOR, "#file")
    directory = "/Users/elenafostachuk/selenium_course/"
    file_name = "file_example.txt"
    file_path = os.path.join(directory, file_name)
    elemento.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()
    
    
    