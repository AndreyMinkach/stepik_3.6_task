import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    country_short = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr',
                     'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']
    country_full = ['العربيّة', 'català', 'česky', 'dansk', 'Deutsch', 'British', 'Ελληνικά', 'español', 'suomi',
                    'français', 'italiano', '한국어', 'Nederlands', 'polski', 'Português', 'Português', 'Română', 'Русский',
                    'Slovensky', 'Українська', '简体中文']
    for i in range(len(country_short)):
        print(country_full[i], country_short[i])
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=r"C:\geckodriver\geckodriver.exe", firefox_profile=fp)
    else:
        raise pytest.UsageError("--language should be from the list")
    yield browser
    print("\nquit browser..")
    #browser.quit()
