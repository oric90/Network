#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import strftime,localtime 
import os
import socket

class Logfile(object):
    """DOCSTRING"""
    def __init__(self,filename):
        self.filename = filename
        
        try:
            if not(os.path.isfile(self.filename)):
                with open(self.filename, "w") as logfile:
                    logfile.write("Logfile created at: "+ strftime("%a, %d %b %Y %H:%M:%S", localtime()) + "\n")
        except IOError:
            if (self.filename == ""):
                raise IOError ('Logfile.filename not set')
            else:
                raise IOError ('Unexpected Error during logfile creation')

    def write(self,stringToInsert):
        if (os.path.isfile(self.filename)):
			with open(self.filename, "a") as logfile:
				logfile.write(strftime("%a, %d %b %Y %H:%M:%S", localtime()) + stringToInsert + "\n")

