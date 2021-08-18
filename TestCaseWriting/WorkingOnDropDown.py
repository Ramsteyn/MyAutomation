from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
# Set Connection Between chrome and python code
path="C://Users//ramadhma//Selenium//chromedriver.exe"
# Chrome class object creation
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

### Selecting a Drop down
obj=Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")
#obj.select_by_index(1)
#obj.select_by_value("2")

# Closing the driver
#driver.close()