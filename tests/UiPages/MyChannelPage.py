import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.UiPages.VideoTabPage import VideoTabPage
from UI.Selenium.SeleniumOp import SeleniumOp

class MyChannelPage(SeleniumOp):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.tablist = ["HomePage", "Films", "PlayLists", "Channels", "ChannelInfo"]

    def GoToFilmTab(self):
        super().refreshPage()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.config["homePageTabContainer"])))
        homePageTabContainer = self.driver.find_element_by_xpath(self.config["homePageTabContainer"])
        tabs = homePageTabContainer.find_elements_by_xpath(self.config["homePageTabs"])
        tabs[self.tablist.index("Films")].click()
        time.sleep(2)
        return VideoTabPage()
