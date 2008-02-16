#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_NewProjectWindow.py
#Version: V0.1 , 16.02.2008
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

class FB_NEWPROJECTWINDOW:

    __WindowWidth = 0
    __WindowHeigth = 0
    __wTree = None
    __window = None
    __TreeView = None
    __SelFolder = ""    #selected Folder for Project
    __SelFile = ""      #selected Filename for Project


    def __init__(self):

        GUIDirPath = os.path.dirname(__file__) + os.sep
        self.__wTree = gtk.glade.XML(GUIDirPath + "freebus.glade", "New_Project")
        self.__window = self.__wTree.get_widget("New_Project")

        dic = { "on_New_Project_destroy" : self.CloseWindow ,
                "on_bCancel_clicked" : self.bCancel,
                "on_bOK_clicked" :self.bOK}

        self.__wTree.signal_autoconnect(dic)
        self.__SelFolder = ""
        self.__SelFile = ""


    def CloseWindow(self,widget):
        return True

    #Cancel Button has been pressed
    def bCancel(self,widget):
        gtk.Widget.destroy(self.__window)

    #OK Button has been pressed
    def bOK(self,widget):
        #get data from FileChooser
        w1 = self.__wTree.get_widget("FileChooser")
        w2 = self.__wTree.get_widget("editProjectName")

        self.__SelFile = w2.get_text()
        self.__SelFolder = w1.get_current_folder()
        #close Dialog
        gtk.Widget.destroy(self.__window)
