from selenium.webdriver import Chrome
path="C://Users//ramadhma//Selenium//chromedriver.exe"
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings")
driver.execute_script("window.scrollTo(0,400);")