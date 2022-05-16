import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    user_language = "es"
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()