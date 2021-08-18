from selenium.webdriver import Chrome
# Set Connection Between chrome and python code
path="C://Users//ramadhma//Selenium//chromedriver.exe"
# Chrome class object creation
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Fetching text of the Element
print(driver.find_element_by_class_name("displayPopup").text)

# Fetching the value of attribute
print(driver.find_element_by_xpath("//input[@type='submit']").get_attribute("value"))