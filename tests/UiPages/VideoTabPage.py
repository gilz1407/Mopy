from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from UI.Selenium.SeleniumOp import SeleniumOp
from selenium.webdriver.support import expected_conditions as EC
class VideoTabPage(SeleniumOp):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    def IsVideoExists(self, videoTitlename):

        videoContainer = self.driver.find_element_by_xpath(self.config["videoContainer"])

        videoContainer = videoContainer.find_element_by_xpath(self.config["videoSubContainer"])

        videoElements = videoContainer.find_elements_by_xpath(self.config["videoElement"])

        videoElement = []
        for ve in videoElements:
            details = ve.find_element_by_xpath(self.config["videoDetails"])
            title=details.find_element_by_xpath(self.config["videoTitle"])
            if title.text == videoTitlename:
                videoElement.append(title)
                videoElement.append(details)
        return videoElement

