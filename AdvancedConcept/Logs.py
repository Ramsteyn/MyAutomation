from selenium.webdriver import Chrome
# Step1
import logging

path="C://Users//ramadhma//Selenium//chromedriver.exe"

# Step2
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#Step3
warn= logging.FileHandler("Warning_logs.txt")
warn.setLevel(logging.WARNING)

info= logging.FileHandler("Info_logs.txt")
info.setLevel(logging.INFO)

# Step4 creating log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
warn.setFormatter(formatter)
info.setFormatter(formatter)

#Step 5
driver= Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings")
log.info("My url is opened")
log.warning("There is delay in opening of browser")