import time

from Lesson3_Test_Framework.Test_Final_Pytest.conftest import user_language

link = f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"


def test_language_choose(browser):
    browser.get(link)
    browser.implicitly_wait(10)

# Объявляем переменные для assert
    card = browser.find_element_by_xpath("//button[text()='Añadir al carrito']")
    expected_text_on_the_button = "Añadir al carrito"

# Проверяем текст кнопки
    assert card
    if card == expected_text_on_the_button:
        print(f"Должна быть кнопка {expected_text_on_the_button}, но вы получили {card}")

    time.sleep(10)