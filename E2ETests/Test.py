import pytest
import redis

from Configurations.cm import Cm
from MessageBrokers.Redis.RedisManager import Listener
from YouTubeDemo.Video import Video
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def UploadVideo():
    r = redis.Redis()  # Connecting to localhost redis server.
    client = Listener(r, ['VideoUploaded'])
    client.start()  # Start listening.

    video=Video()
    video.UploadVideo({"description":"My First Video","title":"gil","fileName":"C:/Users/GILTZ/Desktop/VideosToUpload/POWERofWakingUpEarly.mp4"})
    isMsgFound=False
    while (isMsgFound is False):
        for msg in client.GetLastMessages():
            if "title" in msg:
                if msg["title"]=="gil":
                    isMsgFound = True
                    break
    assert(isMsgFound is True, "The expected video wasn't uploaded to youtube")

    driver = webdriver.Chrome
    driver.get(Cm().config['ElasticSearch'])

UploadVideo()

