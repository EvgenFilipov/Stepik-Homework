from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    int1 = browser.find_element_by_xpath("//span[@id='num1']").text
    # a = int1.text
    int2 = browser.find_element_by_xpath("//span[@id='num2']").text
    # b = int2.text
    c = int(int1) + int(int2)

    # search dropdown using "select"
    select_object = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    select_object.select_by_visible_text(str(c))

    # click button
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()