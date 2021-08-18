from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader
def startBrowser():
    global driver
    if (ConfigReader.readConfig('Brow','Browser')=="Chrome"):
       #path="C://Users//ramadhma//Selenium//chromedriver.exe"
       path = "../Driver/chromedriver.exe"
       driver= Chrome(executable_path=path)
    elif (ConfigReader.readConfig('Brow','Browser')=="firefox"):
       #path="C://Users//ramadhma//Selenium//geckodriver.exe"
       path = "../Driver/geckodriver.exe"
       driver= Firefox(executable_path=path)
    else:
        path = "C://Users//ramadhma//Selenium//chromedriver.exe"
        driver = Chrome(executable_path=path)

    driver.get(ConfigReader.readConfig('Brow','Application_URL'))
    driver.maximize_window()
    return(driver)

def closeBrowser():
    driver.close()
