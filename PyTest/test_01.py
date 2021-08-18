from selenium.webdriver import Chrome
import pytest
a=101
@pytest.mark.skip("Don't want to execute this one")
def test_Selenium():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")

@pytest.mark.skipif(a>100, reason="Don't want to execute this one")
def test_Selenium1():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
#test_Selenium()

def test_Selenium2():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")

@pytest.mark.Smoke
def test_Selenium():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")

@pytest.mark.Sanity
def test_Selenium1():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
#test_Selenium()

@pytest.mark.Smoke
def test_Selenium2():
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")