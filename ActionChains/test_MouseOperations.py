from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
def test_MouseOp():
# Set Connection Between chrome and python code
  path="C://Users//ramadhma//Selenium//chromedriver.exe"
# Chrome class object creation
  driver= Chrome(executable_path=path)
  driver.get("https://thetestingworld.com")

  act=ActionChains(driver)
# Left Clicking the Mouse
#act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Right clicking the Mouse
#act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Double clicking the Element
  act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

#moving Cursor to the point
#act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'VIDEOS')]")).perform()
