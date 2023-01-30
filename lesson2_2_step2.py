from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(a,b):
  return str(int(a) + int(b))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")
    a = a_element.text
    b = b_element.text
    y = calc(a,b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)
    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла