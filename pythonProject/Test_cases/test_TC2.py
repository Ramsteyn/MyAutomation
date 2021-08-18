from Base import InitiateDriver
#from Library import ConfigReader
from Pages import POMClass


def test_Filing():
   driver=InitiateDriver.startBrowser()
   regis= POMClass.Registration(driver)
   regis.enter_Username("Ramsteyn")
   #driver.find_element_by_name(ConfigReader.fetchElement("Registration","userName")).send_keys("Ramsteyn")
   driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("ramsteyn420@gmail.com")
   regis.enter_password("Ramsteyn8$")
   #driver.find_element_by_name(ConfigReader.fetchElement("Registration","passWord")).send_keys("Ramsteyn8$")
   driver.find_element_by_css_selector("input[name='fld_cpassword']").send_keys("Ramsteyn8$")
   driver.find_element_by_name("fld_username").clear()
   driver.find_element_by_name("fld_username").send_keys("Dalesteyn")