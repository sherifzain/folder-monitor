#!/usr/bin/python
import os
import pyinotify
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        print "Comment  :", data

parser = MyHTMLParser()

FOLDER_PATH = '/tmp'

wm = pyinotify.WatchManager()
mask = pyinotify.IN_MODIFY | pyinotify.IN_CREATE

class FilesMonitor(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        print "Created: %s " % event.name
        fileext = event.name.split('.')[1]
        if  fileext == 'html' or fileext == 'htm':
            path = '%s/%s' % (event.path, event.name)
            self._processHtmlFile(path=path)

    def _processHtmlFile(self, path):
        print 'Path: %s' % path
        with open(path) as fo:
            data = fo.read()
            parser.handle_comment(data)
            parser.close()

    def process_IN_MODIFY(self, event):
        print "Delete: %s " % os.path.join(event.path, event.name)


notifier = pyinotify.Notifier(wm, FilesMonitor())
wdd = wm.add_watch(FOLDER_PATH, mask)

notifier.loop()