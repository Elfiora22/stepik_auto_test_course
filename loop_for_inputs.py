from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #element1 = browser.find_element(By.CSS_SELECTOR, 'input.first:required')# каждый элемент напрямую
    #element1.send_keys("Ivan")
    #element2 =  browser.find_element(By.CSS_SELECTOR, 'input.second:required')
    #element2.send_keys("Petrov")
    #element3 =  browser.find_element(By.CSS_SELECTOR, 'input.third:required')
    #element3.send_keys("email@ema.il")
    labels = browser.find_elements(By.TAG_NAME, 'label') # Список лэйблов над текстовыми полями
    inputs = browser.find_elements(By.TAG_NAME, 'input') #
    for i, label in enumerate(labels):          # Если последний символ
        if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Обязалово!')
    
    button = browser.find_element(By.CSS_SELECTOR,'button.btn')
    #button.click()
    #time.sleep(30)
    #welcoming_element = browser.find_element(By.TAG_NAME, 'h1')
    #welcome_text = welcoming_element
    
    

finally:
    time.sleep(10)
    browser.quit()
    
    
#     .first_block .form-control.first селекторы по классам div + input
#     .first_block .form-control.second
#     .form-group .form-control.third - email
#     .third_class .form-control.third -вот почему даются 2 наименования класса! Можно любое)

#     
    
    
    