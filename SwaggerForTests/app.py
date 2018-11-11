#!/usr/bin/env python3
import connexion
import logging
import pytest
from gevent import os
import re

availableTests={"hits":[]}
parentFolder="../"

def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

def post_testByFile(TestFile):
    pytest.main([TestFile["fileName"]])

def post_testByMarks(Marker):
    pytest.main([Marker["fileName"],'-v','-m',Marker["marker"]])

def post_testByName(TestName):
    pytest.main([TestName["fileName"],'-k',TestName["testName"]])

def post_testByFolder(FolderName):
    _folderName=FolderName["folderName"]
    for path in absoluteFilePaths(_folderName):
        m = re.search('\\\\(Test.*.py)', path)
        if (m.group(0)!=None):
            pytest.main(_folderName+m.group(0))
    return "The test was run",200

def Get_availableTests(FolderName):
    _folderName = parentFolder + FolderName
    for path in absoluteFilePaths(_folderName):
        before, after = path.split(FolderName)
        parsedAfter = after.replace("\\", "/")
        fileName = parsedAfter.split("/")[-1]
        if (fileName.startswith("Test") and fileName.endswith("py")):
            availableTests["hits"].append(_folderName + parsedAfter)
    if availableTests["hits"] == []:
        return ('The requested folder was not found',404)
    return availableTests,200

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    #run our standalone gevent server
    app.run(port=8080, server='gevent')




