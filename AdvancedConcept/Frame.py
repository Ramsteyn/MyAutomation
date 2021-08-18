from selenium.webdriver import Chrome
path="C://Users//ramadhma//Selenium//chromedriver.exe"
driver= Chrome(executable_path=path)
driver.get("https://toolsqa.com/i-frame-practice-page/")
#Swtiching Into frame
driver.switch_to.frame("iframe2")
driver.find_element_by_xpath("//a[contains(text(),'Read more')]").click()
#returning back to Frame
driver.switch_to.default_content()
driver.find_element_by_xpath("//span[text()='VIDEOS']").click()
