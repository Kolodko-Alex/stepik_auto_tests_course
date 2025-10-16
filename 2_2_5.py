from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = number.text

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    input1.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    checkbox.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    
    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()
    

finally:
    time.sleep(15)
    browser.quit()