from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

link = "example.com"
caps = DesiredCapabilities.CHROME
browser = webdriver.Chrome(desired_capabilities=caps)
caps["pageLoadStrategy"] = "none"
browser.get(link)
# ждем загрузку элемента:
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".example_selector"))) 
# стопаем загрузку сайта:
browser.execute_script("window.stop();")