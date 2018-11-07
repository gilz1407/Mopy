import logging
import pytest
import redis
from Parsers.CSV.CsvParser import CsvParser
from tests.UiPages.MyChannelPage import MyChannelPage
from MessageBrokers.Redis.RedisManager import Listener
from UI.Selenium.SeleniumOp import SeleniumOp
from YouTubeDemo.Video import Video

def setup_module(module):
    global video
    video = Video()

def teardown_module(module):
    pass

@pytest.mark.parametrize(
    'title,description,path',CsvParser("./tests/video_test_data.csv").GetDataDrivenFormat()
)
def UploadVideo(title,description,path):
    logging.info("Start \"UploadVideo\" test - "+title,description,path)
    channel='VideoUploaded'

    logging.info("Start subscribing to \"UploadedVideo\" channel")
    r = redis.Redis()  # Connecting to localhost redis server.
    client = Listener(r, [channel])
    client.start()  # Start listening.
    logging.info("listening to \"UploadedVideo\" channel")

    logging.info("Start uploading video")
    video.UploadVideo({"description":description,
                       "title":title,
                       "fileName":path})

    logging.info("Waiting for relevant message from redis")
    uploadedVideoIds = []
    isMsgFound=False
    relevantField='title'
    while isMsgFound is False:
        for msg in client.GetLastMessages():
            try:
                if relevantField in msg:
                    if msg[relevantField] == "UI Automation":
                        logging.info("Video was uploaded")
                        uploadedVideoIds.append(msg["AddedVideo"])
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
    videoElement = filmPage.IsVideoExists("UI Automation")
    assert(videoElement != [],"The uploaded video wasn't found")
    op.closeBrowser()

    logging.info("Delete the last uploaded video")
    # Delete all of the uploaded videos
    for videoitem in uploadedVideoIds:
        video.videos_delete(id=videoitem)

    logging.info("Checking on th UI that the video was deleted")
    op = SeleniumOp()
    op.openUrl("youTubeUrl")
    filmPage = MyChannelPage().GoToFilmTab()
    videoElement = filmPage.IsVideoExists("UI Automation")
    assert (videoElement == [], "The uploaded video wasn't found")
    op.closeBrowser()
