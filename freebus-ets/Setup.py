#!/usr/bin/python

from distutils.core import setup
import py2exe
import glob
import sys

sys.path.append(r'J:/Elektronik/Projekte/Python Workspace/FB ETS/src')
sys.path.append(r'J:/Elektronik/PyGTK/GTK/lib')
import os

data_files = []

opts = {"py2exe": {
                            "compressed": 0,
                            "optimize": 2,
                            "excludes": "",
                            "includes": ["cairo", "pango", "pangocairo" ,"atk", "gobject"],
				
                            "packages" : ["encodings"]
                        }} 


setup(windows=[{"script" : 'src/Freebus-ETS.py'}],options=opts,data_files=data_files)               