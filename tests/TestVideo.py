import inspect
import logging
import os
import sys
import pytest
import redis
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Connections.Rest.requests.DeleteVideo import DeleteVideo
from Connections.Rest.requests.UploadVideo import UploadVideo
from Parsers.CSV.CsvParser import CsvParser
from tests.UiPages.MyChannelPage import MyChannelPage
from MessageBrokers.Redis.RedisManager import Listener
from UI.Selenium.SeleniumOp import SeleniumOp

@pytest.mark.parametrize(
    'title,description,path', CsvParser("../tests/video_test_data.csv").GetDataDrivenFormat()
)

def test_UploadVideo(title, description, path):
    #logging.getLogger()
    logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'mylogs'), level=logging.INFO)
    logging.info("Start \"UploadVideo\" test - " + title, description, path)
    channel = 'VideoUploaded'

    logging.info("Start subscribing to \"UploadedVideo\" channel")
    r = redis.Redis()  # Connecting to localhost redis server.
    client = Listener(r, [channel])
    client.start()  # Start listening.
    logging.info("listening to \"UploadedVideo\" channel")

    logging.info("Start uploading video")

    uploadVideo = UploadVideo()
    uploadVideo.SetDescription(description)
    uploadVideo.SetFileName(path)
    uploadVideo.SetTitle(title)
    uploadVideo.Request()

    logging.info("Waiting for relevant message from redis")
    uploadedVideoIds = []
    isMsgFound = False
    relevantField = 'title'
    while isMsgFound is False:
        for msg in client.GetLastMessages():
            try:
                if relevantField in msg:
                    if msg[relevantField] == title:
                        logging.info("Video was uploaded")
                        uploadedVideoIds.append(msg["AddedVideo"])
                        isMsgFound = True
                        client.unsubscribe(channel)
                        break
            except ValueError:
                continue
    assert (isMsgFound is True, "The expected video wasn't uploaded to youtube")

    # Verify on the ui that new video was uploaded
    op = SeleniumOp(force=True)
    op.openUrl("youTubeUrl")


    videoElement = []

    currTry = 0
    while len(videoElement) == 0 and currTry < 5:
        filmPage = MyChannelPage().GoToFilmTab()
        videoElement = filmPage.IsVideoExists(title)
        currTry += 1
    assert (len(videoElement) > 0, "The uploaded video wasn't found")
    op.closeBrowser()

    logging.info("Delete the last uploaded video")
    # Delete all of the uploaded videos
    deleteVideo = DeleteVideo()
    for videoitem in uploadedVideoIds:
        deleteVideo.SetVideoId(videoitem)
        deleteVideo.Request()

    logging.info("Checking on th UI that the video was deleted")
    op = SeleniumOp(force=True)

    op.openUrl("youTubeUrl")

    currTry = 0
    filmPage = MyChannelPage().GoToFilmTab()
    videoElement = filmPage.IsVideoExists(title)
    while len(videoElement) > 0 and currTry < 5:
        filmPage = MyChannelPage().GoToFilmTab()
        videoElement = filmPage.IsVideoExists(title)
        currTry += 1
    assert (len(videoElement) == 0, "The uploaded video wasn't found")
    op.closeBrowser()