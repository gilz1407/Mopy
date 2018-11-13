from gevent import time

from Configurations.cm import Cm
from selenium import webdriver

class SeleniumOp():
    driver=None

    def __init__(self,pageName='UiTesting',force=False):
        if SeleniumOp.driver is None or force==True:
            driverConfig=Cm().config["ChromeDriver"]
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir="+driverConfig["userDataDir"])
            if driverConfig["path"] == "":
                self.driver = webdriver.Chrome(options=options)
            else:
                self.driver = webdriver.Chrome(driverConfig["path"],options=options)
            SeleniumOp.driver = self.driver
            self.driver.maximize_window()
        self.config = Cm("Xpathmapping.ini").config[pageName]

    def resizeBrowserWindow(self,width,hight):
        self.driver.set_window_size(width,hight)

    def openUrl(self,urlName):
        time.sleep(2)
        self.driver.get(self.config[urlName])

    def closeBrowser(self):
        self.driver.quit()

    def refreshPage(self):
        self.driver.refresh()


