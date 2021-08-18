from selenium.webdriver import Chrome
# Set Connection Between chrome and python code
path="C://Users//ramadhma//Selenium//chromedriver.exe"
# Chrome class object creation
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Setting values to the text box using element locators
driver.find_element_by_name("fld_username").send_keys("Ramsteyn")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("ramsteyn420@gmail.com")
driver.find_element_by_name("fld_password").send_keys("Ramsteyn8$")
driver.find_element_by_css_selector("input[name='fld_cpassword']").send_keys("Ramsteyn8$")
# Clearing the value in Previous text box
driver.find_element_by_name("fld_username").clear()
driver.find_element_by_name("fld_username").send_keys("Dalesteyn")

# Clicking on Radio and Check boxs
driver.find_element_by_xpath("//input[@value='office']").click()
driver.find_element_by_xpath("//input[@value='home']").click()
driver.find_element_by_xpath("//input[@name='terms']").click()
# sign up button clicking

driver.find_element_by_xpath("//input[@type='submit']").click()

# Clicking on the link
driver.find_element_by_link_text("Read Detail").click()

# Closing the driver
driver.close()