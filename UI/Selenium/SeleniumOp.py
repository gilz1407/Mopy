from Configurations.cm import Cm
from selenium import webdriver

class SeleniumOp():
    def __init__(self,):
        self.conf = Cm().config['UiTesting']
        self.driver = webdriver.Chrome

    def openUrl(self,urlName):
        self.driver.get(self.conf[urlName])