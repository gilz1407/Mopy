from Configurations.cm import Cm
from selenium import webdriver

class SeleniumOp():
    def __init__(self,):
        self.conf = Cm().config['UiTesting']
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def resizeBrowserWindow(self,width,hight):
        self.driver.set_window_size(width,hight)

    def openUrl(self,urlName):
        self.driver.get(self.conf[urlName])
        
