from selenium.webdriver import Chrome
import ScreenFunction
path="C://Users//ramadhma//Selenium//chromedriver.exe"
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings")
#driver.get_screenshot_as_file("C:/Users/ramadhma/PycharmProjects/AdvancedConcept/Screenshot.png")
ScreenFunction.take_screenshot(driver,"FirstShot")
   