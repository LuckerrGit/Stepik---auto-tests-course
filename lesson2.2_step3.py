import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text_elt1 = browser.find_element_by_css_selector("#num1")
    x = text_elt1.text
    text_elt2 = browser.find_element_by_css_selector("#num2")
    y = text_elt2.text
    num1 = int(x)
    num2 = int(y)
    sum_el = str(str(num1+num2))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum_el)
    
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()