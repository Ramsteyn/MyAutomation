from Base import InitiateDriver


def test_regisration_Validation():
    driver=InitiateDriver.startBrowser()
    driver.find_element_by_name("fld_username").send_keys("Ramsteyn")