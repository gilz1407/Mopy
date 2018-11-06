import pytest
import redis

from E2ETests.UiPages.MyChannelPage import MyChannelPage
from MessageBrokers.Redis.RedisManager import Listener
from UI.Selenium.SeleniumOp import SeleniumOp
from YouTubeDemo.Video import Video

def UploadVideo():
    channel='VideoUploaded'
    r = redis.Redis()  # Connecting to localhost redis server.
    client = Listener(r, [channel])
    client.start()  # Start listening.

    video=Video()
    video.UploadVideo({"description":"My First Video",
                       "title":"DataBases",
                       "fileName":"C:/Users/GILTZ/Desktop/VideosToUpload/DataBases.mp4"})
    video.UploadVideo({"description": "My First Video",
                       "title": "MessageBrokers",
                       "fileName": "C:/Users/GILTZ/Desktop/VideosToUpload/MessageBrokers.mp4"})
    video.UploadVideo({"description": "My First Video",
                       "title": "parsers",
                       "fileName": "C:/Users/GILTZ/Desktop/VideosToUpload/parsers.mp4"})
    video.UploadVideo({"description": "My First Video",
                       "title": "UI Automation",
                       "fileName": "C:/Users/GILTZ/Desktop/VideosToUpload/UI Automation.mp4"})
    video.UploadVideo({"description": "My First Video",
                       "title": "MyFirstMovie",
                       "fileName": "C:/Users/GILTZ/Desktop/VideosToUpload/MyFirstMovie.mp4"})
    video.UploadVideo({"description": "My First Video",
                       "title": "mop",
                       "fileName": "C:/Users/GILTZ/Desktop/VideosToUpload/mop.mp4"})

    isMsgFound=False
    while isMsgFound is False:
        for msg in client.GetLastMessages():
            try:
                if 'title' in msg:
                    if msg["title"] == "UI Automation":
                        isMsgFound = True
                        client.unsubscribe(channel)
                        break
            except ValueError:
                continue
    assert(isMsgFound is True, "The expected video wasn't uploaded to youtube")

# Verify on the ui that new video was uploaded
op = SeleniumOp()
op.openUrl("youTubeUrl")
filmPage=MyChannelPage().GoToFilmTab()
filmPage.IsVideoExists("UI Automation")

#UploadVideo()

