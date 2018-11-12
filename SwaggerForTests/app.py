#!/usr/bin/env python3
import connexion
import logging
import pytest
from gevent import os
import re

availableTests = {"hits":[]}
parentFolder = "../"

def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

def post_testByFile(TestFile):
    pytest.main([TestFile["fileName"],'-v','--log-file',TestFile["fileName"]+'.log'])

def post_testByMarks(Marker):
    pytest.main([Marker["fileName"],'-v','-m',Marker["marker"]])

def post_testByName(TestName):
    pytest.main([TestName["fileName"],'-k',TestName["testName"]])

def post_testByFolder(FolderName):
    _folderName=FolderName["folderName"]
    for path in absoluteFilePaths(_folderName):
        path=path.replace("\\","/")
        m = re.search('(Test[a-z,A-Z,1-9]*.py)', path)
        if (m!=None):
            pytest.main([_folderName+"/"+m.group(0),'--log-file','../Logs/'+m.group(0)+'.log'])
    return "The test was run",200

def Get_availableTests(FolderName):
    _folderName = parentFolder + FolderName
    for path in absoluteFilePaths(_folderName):
        path = path.replace("\\", "/")
        m = re.search('(Test[a-z,A-Z,1-9]*.py)', path)
        if m is not None:
            availableTests["hits"].append(_folderName+"/"+m.group(0))
    if not availableTests["hits"]:
        return 'The requested folder was not found', 404
    return availableTests, 200

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='gevent')




