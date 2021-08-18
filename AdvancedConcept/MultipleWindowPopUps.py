from selenium.webdriver import Chrome
path="C://Users//ramadhma//Selenium//chromedriver.exe"
driver= Chrome(executable_path=path)
driver.get("https://naukri.com")
main=""
All_window= driver.window_handles
#print(All_window)
for i in All_window:
    driver.switch_to.window(i)
#Closing Mutiple windows
    if (driver.current_url=="https://naukri.com/"):
        print("This is may main window")
        main= i
    else:
        driver.close()
driver.switch_to.window(main)
print(driver.current_url)
