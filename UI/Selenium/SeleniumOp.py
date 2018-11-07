from Configurations.cm import Cm
from selenium import webdriver

class SeleniumOp():
    driver=None
    def __init__(self,pageName='UiTesting'):
        if SeleniumOp.driver is None:
            self.driver = webdriver.Chrome()
            SeleniumOp.driver=self.driver
            self.driver.maximize_window()
        self.config = Cm("Xpathmapping.ini").config[pageName]

    def resizeBrowserWindow(self,width,hight):
        self.driver.set_window_size(width,hight)

    def openUrl(self,urlName):
        self.driver.get(self.config[urlName])

    def closeBrowser(self):
        self.driver.quit()


