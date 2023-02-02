from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_image = browser.find_element(By.ID, "treasure")
    x = x_image.get_attribute("valuex")
    
    import math
    def calc(x):
         return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    y_input = browser.find_element(By.ID, 'answer')
    y_input.send_keys(y)
    
    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    robot_check.click()
    robot_rule = browser.find_element(By.ID, 'robotsRule')
    robot_rule.click()
    
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

finally:
    time.sleep(30)
    browser.quit()    
    
    
    
    
    
    
    
    
