from Library import ConfigReader
class Registration:
    def __init__(self,obj):
        global driver
        driver=obj
    def enter_Username(self,username):
        driver.find_element_by_name(ConfigReader.fetchElement("Registration", "userName")).send_keys(username)
    def enter_password(self,password):
        driver.find_element_by_css_selector("input[name='fld_cpassword']").send_keys(password)