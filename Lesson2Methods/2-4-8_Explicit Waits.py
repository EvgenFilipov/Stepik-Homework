from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет равной 100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()


    # проверяем появление формулы
    message = browser.find_element_by_id("simple_text")
    assert "Math is real magic!" in message.text

    # получаем значение и присваиваем в переменную
    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
    # считаем
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # input data
    input = browser.find_element_by_xpath("//input[@class='form-control']")
    input.send_keys(y)

    # инициализируем кнопку
    button2 = browser.find_element_by_id("solve")
    # zhmyak
    button2.click()

finally:
    # смотрим
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

