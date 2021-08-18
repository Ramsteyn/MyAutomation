from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def setFixture():
    global driver
    path = "C://Users//ramadhma//Selenium//chromedriver.exe"
    driver = Chrome(executable_path=path)
    # Anything after yield will execute after all the test cases executed.
    yield
    driver.close()
def test_Selenium(setFixture):
    driver.get("https://www.facebook.com/")


def test_Selenium1(setFixture):
    driver.get("https://www.facebook.com/")


def test_Selenium2(setFixture):
    driver.get("https://www.facebook.com/")



