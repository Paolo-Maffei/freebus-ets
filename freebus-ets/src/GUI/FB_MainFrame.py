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
from GUI import FB_NewProjectWindow
from GUI import FB_OpenProjectWindow


class FB_MainFrame:

    __WindowWidth = 0
    __WindowHeigth = 0
    __LogObj = None
    __CurProjectObj = None

    def __init__(self, LogObj):
    # create a new window
        self.__LogObj = LogObj
        self.__CurProjectObj = None

        #get screensize
        self.__WindowWidth = gtk.gdk.screen_width()
        self.__WindowHeigth = gtk.gdk.screen_height()

        GUIDirPath = os.path.dirname(__file__) + os.sep
        self.wTree = gtk.glade.XML(GUIDirPath + "freebus.glade", "MainFrame")
        self.window = self.wTree.get_widget

        dic = { "on_MainFrame_destroy" : gtk.main_quit ,
                "on_Quitt_activate" : gtk.main_quit,
                "on_new_project_activate" : self.MenuNewProject,
                "on_open_project_activate" : self.MenuOpenProject,
                "on_Save_activate" : self.MenuSaveProject }
        self.wTree.signal_autoconnect(dic)

    #create a new project
    def MenuNewProject(self,widget, data=None):
        newProjectWin = FB_NewProjectWindow.FB_NEWPROJECTWINDOW(self.__LogObj,self)

    #open an existing project
    def MenuOpenProject(self,widget, data=None):
        openProjectWin = FB_OpenProjectWindow.FB_OPENPROJECTWINDOW(self.__LogObj, self)

    #save project data
    def MenuSaveProject(self,widget, data=None):
        if(self.__CurProjectObj <> None):

            self.__CurProjectObj.SaveProject()
        else:
            print "Fehler save "
            self.__LogObj.NewLog("Error at saving Projectdata -> CurProjectObj is Nonetype",1)


    #set current project object
    def SetCurrProject(self, ProjObj):
        self.__CurProjectObj = ProjObj
        self.__CurProjectObj.setPrefferedBusSystem("FREEBUS-EIB")

    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
        gtk.main()