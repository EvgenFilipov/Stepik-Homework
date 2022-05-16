import pytest
import time
import math

from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('ID', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_search_message_in_feedback(browser, ID):
    print("\nstart math def")
    answer = str(math.log(int(time.time())))
    link = f"https://stepik.org/lesson/{ID}/step/1/"
    browser.get(link)
    browser.implicitly_wait(10)
    searchPlaceholder = browser.find_element_by_class_name("textarea")
    searchPlaceholder.send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission") #//button[@class='submit-submission']
    button.click()
    browser.implicitly_wait(10)
    searchFeedback = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" in searchFeedback.text



