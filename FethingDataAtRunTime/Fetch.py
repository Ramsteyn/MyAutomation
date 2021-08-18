from selenium.webdriver import Chrome
# Set Connection Between chrome and python code
path="C://Users//ramadhma//Selenium//chromedriver.exe"
# Chrome class object creation
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Fetching page title
print(driver.title)

#Fetching Page URL
print(driver.current_url)

# Fetching HTML of the Page
print(driver.page_source)