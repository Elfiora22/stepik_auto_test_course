from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    element1 = browser.find_element(By.XPATH, '//*[@name="first_name"]')
    element1.send_keys("Ivan")
    element2 =  browser.find_element(By.XPATH, '//*[@name="last_name"]')
    element2.send_keys("Petrov")
    element3 =  browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    element3.send_keys("Saratov")
    element4 = browser.find_element(By.XPATH, '//input[@id="country"]')
    element4.send_keys("Russia")
    
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    
    
    
    
    
        
    
    


    