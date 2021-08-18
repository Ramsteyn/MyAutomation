from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def before():
    global driver
    path="C://Users//ramadhma//Selenium//chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

def test_All(before):
    driver.get("https://thetestingworld.com/testings/")
    driver.maximize_window()

    driver.find_element_by_name("fld_username").send_keys("Ramsteyn")
    driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("ramsteyn420@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("Ramsteyn8$")
    driver.find_element_by_css_selector("input[name='fld_cpassword']").send_keys("Ramsteyn8$")
    driver.find_element_by_name("fld_username").clear()
    driver.find_element_by_name("fld_username").send_keys("Dalesteyn")


    driver.find_element_by_xpath("//input[@value='office']").click()
    driver.find_element_by_xpath("//input[@value='home']").click()
    driver.find_element_by_xpath("//input[@name='terms']").click()


    driver.find_element_by_xpath("//input[@type='submit']").click()

# Clicking on the link
    driver.find_element_by_link_text("Read Detail").click()
    assert driver.title=="Login and sign up"
# Closing the driver
#   driver.close()
