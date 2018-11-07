from gevent import os

# install allure
def installallure(folderPath):
    old_path = os.environ['PATH']
    try:
        os.environ['PATH'] = "{}{}{}".format(folderPath, os.pathsep, old_path)
    finally:
        os.environ['PATH'] = old_path