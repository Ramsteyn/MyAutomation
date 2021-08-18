from selenium.webdriver import Firefox

# Set Connection Between chrome and python code
path="C://Users//ramadhma//Selenium//geckodriver.exe"
# Chrome class object creation
driver= Firefox(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Setting values to the text box using element locators
driver.find_element_by_name("fld_username").send_keys("Ramsteyn")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("ramsteyn420@gmail.com")
driver.find_element_by_name("fld_password").send_keys("Ramsteyn8$")
driver.find_element_by_css_selector("input[name='fld_cpassword']").send_keys("Ramsteyn8$")