from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    
    y_input = browser.find_element(By.ID, 'answer')
    y_input.send_keys(y)
    
    button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button2.click()
    
finally:
    time.sleep(30)
    browser.quit()
    
    
    
    
    
    
    
    
    
    
