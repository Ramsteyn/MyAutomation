from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import pytest
#import time

@pytest.fixture()
def setfixtures():
   global driver
   path="C://Users//ramadhma//Selenium//chromedriver.exe"
   driver= Chrome(executable_path=path)
   driver.get("https://thetestingworld.com/testings")
   driver.implicitly_wait(20)




def test_Py(setfixtures):
  driver.maximize_window()
  wait= WebDriverWait(driver,30)
  wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))
  obj=Select(driver.find_element_by_id("countryId"))
  obj.select_by_visible_text("India")


  wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
  obj = Select(driver.find_element_by_id("stateId"))
  obj.select_by_visible_text("Delhi1")




