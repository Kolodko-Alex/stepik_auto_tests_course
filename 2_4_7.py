from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5[id="price"]'), "100")
    )
    button =  browser.find_element(By.CSS_SELECTOR, 'button[id="book"]')
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    number = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = number.text

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(calc(x))

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
