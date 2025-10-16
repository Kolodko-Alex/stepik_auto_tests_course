from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    start = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    start.click()

    confirm = browser.switch_to.alert
    confirm.accept()

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

