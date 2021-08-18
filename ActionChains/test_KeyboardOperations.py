from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test_keyboardOp():
  # Set Connection Between chrome and python code
  path="C://Users//ramadhma//Selenium//chromedriver.exe"
  # Chrome class object creation
  driver= Chrome(executable_path=path)
  driver.get("https://thetestingworld.com/testings/")
  driver.find_element_by_name("fld_username").send_keys("HelloWorld")

  act=ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
#act.key_down(Keys.CONTROL).send_keys("Ramadhas").perform()

#Using multiple keys
  act.key_down(Keys.CONTROL).send_keys("a").perform()
  time.sleep(10)
  act.send_keys(Keys.DELETE).perform()
#act.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.DELETE).perform()



