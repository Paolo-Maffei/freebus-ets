#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_MainFrame.py
#Version: V0.1 , 09.02.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

import os
import sys
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from GUI import *

class FB_MainFrame:

    __WindowWidth = 0
    __WindowHeigth = 0

    def __init__(self):
    # create a new window
        #get screensize
        self.__WindowWidth = gtk.gdk.screen_width()
        self.__WindowHeigth = gtk.gdk.screen_height()

        GUIDirPath = os.path.dirname(__file__) + os.sep
        self.wTree = gtk.glade.XML(GUIDirPath + "freebus.glade")
        self.window = self.wTree.get_widget

        dic = { "on_MainFrame_destroy" : gtk.main_quit ,
                "on_Quitt_activate" : gtk.main_quit }
        self.wTree.signal_autoconnect(dic)

    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
        gtk.main()