from selenium.webdriver import Chrome
import pytest

@pytest.mark.skip
def test_Selenium():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
    assert driver.title== "Facebook login"


def test_Selenium1():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
    assert driver.current_url== "https://www.facebook.com/"


