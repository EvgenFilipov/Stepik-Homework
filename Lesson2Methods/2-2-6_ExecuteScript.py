from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # присваиваем значение в переменную
    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)

    # считаем
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # input data
    input = browser.find_element_by_xpath("//input[@class='form-control']")
    input.send_keys(y)

    # поиск и галочка в чек-боксе
    check = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    check.click()

    # change radiobutton
    radiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']")
    # scrolling
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # инициализируем кнопку
    button = browser.find_element_by_tag_name("button")
    # scrolling
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # zhmyak
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()