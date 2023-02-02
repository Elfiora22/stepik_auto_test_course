from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    troll_button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    troll_button.click()
    redirect = browser.switch_to.window(browser.window_handles[1])
    
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
    