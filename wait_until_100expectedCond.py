from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button1 = browser.find_element(By.ID, "book")
    price100 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))   
    button1.click()

    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_input = browser.find_element(By.ID, "answer")
    y_input.send_keys(y)
    
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    
    
finally:
    time.sleep(30)
    browser.quit()
    



