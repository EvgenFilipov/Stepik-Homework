from selenium import webdriver
import math
import time

# функция для расчета по формуле
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# тестовый сценарий
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element_by_xpath("//img[@id]")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # поиск поля ввода и ввод
    input = browser.find_element_by_xpath("//input[@id='answer']")
    input.send_keys(y)

    # search people radio
    people_radio = browser.find_element_by_id("peopleRule")

    # ищем атрибут "checked" в элементе "people_radio"
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # альтернативный способ проверки
    # assert people_checked == "true", "People radio is not selected by default"

    # ищем радиобаттон "роботы рулят"
    robots_radio = browser.find_element_by_id("robotsRule")
    # проверяем "чекнут" ли он
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # поиск и галочка в чек-боксе
    check = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    check.click()

    # change radiobutton
    radiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radiobutton.click()

    # click on the Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
