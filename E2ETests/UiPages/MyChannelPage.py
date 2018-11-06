from E2ETests.UiPages.VideoTabPage import VideoTabPage
from UI.Selenium.SeleniumOp import SeleniumOp

class MyChannelPage(SeleniumOp):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.tablist = ["HomePage", "Films", "PlayLists", "Channels", "ChannelInfo"]

    def GoToFilmTab(self):
        homePageTabContainer = self.driver.find_element_by_xpath(self.config["homePageTabContainer"])
        tabs = homePageTabContainer.find_elements_by_xpath(self.config["homePageTabs"])
        tabs[self.tablist.index("Films")].click()
        return VideoTabPage()
