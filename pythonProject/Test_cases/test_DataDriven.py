from Base import InitiateDriver
#from Library import ConfigReader
from Pages import POMClass
import pytest
from Data import DataGen
import time
#def dataGenerator():
   # li= [["U1","P1"],["U2","P2"],["U3","P3"]]
   # return li

@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_Filing(data):
   driver=InitiateDriver.startBrowser()
   regis= POMClass.Registration(driver)
   regis.enter_Username(data[0])
   regis.enter_password(data[1])
   time.sleep(10)
   InitiateDriver.closeBrowser()