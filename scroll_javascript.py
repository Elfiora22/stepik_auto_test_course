from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser= webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.ID, "input_value").text
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    y_input = browser.find_element(By.ID, 'answer')
    y_input.send_keys(y)
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    robot_check.click()
    robot_rule = browser.find_element(By.ID, 'robotsRule')
    robot_rule.click()
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()
    
    
    
    
    
