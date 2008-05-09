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
from Global import Global
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from GUI import FB_NewProjectWindow
from GUI import FB_OpenProjectWindow
from GUI.Tree import FB_ArchitecturalTree



class FB_MainFrame:

    __WindowWidth = 0
    __WindowHeigth = 0
    __LogObj = None
    __CurProjectObj = None
    __GladeObj = None
    __GUIPath = ""
    __ImagePath = ""
    __ProjTree = None
    __TreeIterator = None        #Iterator-Object for Tree
    treestore = None
    __ArchTree = None            #Object for Tree-Class
    __handelboxToolbar = None    #widget object of handlebox toolbar


    def __init__(self, LogObj):
    # create a new window
        self.__LogObj = LogObj
        self.__CurProjectObj = None

        #get screensize
        self.__WindowWidth = gtk.gdk.screen_width()
        self.__WindowHeigth = gtk.gdk.screen_height()

        self.__GladeObj = gtk.glade.XML(Global.GUIPath  + "freebus.glade","MainFrame")

        if(self.__GladeObj == None):
           self.__LogObj.NewLog("Error at intializing GUI-Interface (Glade-Object)",1)
           return

        #get widget of window
        self.window = self.__GladeObj.get_widget("MainFrame")

        #setting up DragNDrop of (Source) Toolbarbuttons
        #1. get widget of building button
        self.widget_building = self.__GladeObj.get_widget("button_building")
        self.widget_building.drag_source_set(gtk.gdk.BUTTON1_MASK,[('text/plain', gtk.TARGET_SAME_APP, Global.DND_BUILDING)],gtk.gdk.ACTION_COPY)
        #2. get widget of floor button
        self.widget_floor = self.__GladeObj.get_widget("button_floor")
        self.widget_floor.drag_source_set(gtk.gdk.BUTTON1_MASK,[('text/plain', gtk.TARGET_SAME_APP, Global.DND_FLOOR)],gtk.gdk.ACTION_COPY)
        #3. get widget of room button
        self.widget_room = self.__GladeObj.get_widget("button_room")
        self.widget_room.drag_source_set(gtk.gdk.BUTTON1_MASK,[('text/plain', gtk.TARGET_SAME_APP, Global.DND_ROOM)],gtk.gdk.ACTION_COPY)
        #4. get widget of junctionbox button
        self.widget_junction = self.__GladeObj.get_widget("button_junction")
        self.widget_junction.drag_source_set(gtk.gdk.BUTTON1_MASK,[('text/plain', gtk.TARGET_SAME_APP, Global.DND_JUNCTION)],gtk.gdk.ACTION_COPY)



        #get widget of handlebox_toolbar
        self.__handelboxToolbar = self.__GladeObj.get_widget("handlebox_toolbar")
        #hide control at project start
        self.__handelboxToolbar.hide()

        #get widget object of PanelLeft (Project-Tree)
        self.Tree = self.__GladeObj.get_widget("ProjectTree")
        self.__ProjTree = self.Tree

        dic = { "on_MainFrame_destroy" : gtk.main_quit ,
                "on_Quitt_activate" : gtk.main_quit,
                "on_new_project_activate" : self.MenuNewProject,
                "on_open_project_activate" : self.MenuOpenProject,
                "on_Save_activate" : self.MenuSaveProject,

                "on_button_building_drag_data_get" : self.BuildingDragDataGet,

                "on_ProjectTree_drag_data_received" : self.ProjectTreeDropData,
                "on_ProjectTree_drag_motion" : self.ProjectTreeDragMotion

                }
        self.__GladeObj.signal_autoconnect(dic)

        #create Project Tree

        self.__ArchTree = FB_ArchitecturalTree.FB_ArchitecturalTree(self.__LogObj,self.__ProjTree)


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
        #reorganize our project-tree
        if(self.__ProjTree <> None):
            self.__ArchTree.ClearTree()
            self.__ArchTree.CreateNewTree(self.__CurProjectObj)
            self.__handelboxToolbar.show()


    def BuildingDragDataGet(self,widget, drag_context, selection_data, info, time):
        pass

    #add object to tree -> drop object over treeview
    def ProjectTreeDropData(self,treeview, drag_context, x, y, selection, info, timestamp):
        drop_info = treeview.get_dest_row_at_pos(x, y)
        if drop_info:
            model = treeview.get_model()
            path, position = drop_info
            data = selection.data
            #compare info with position/path object and add building,florr,room ...
            ArchModel = self.__CurProjectObj.getArchModel
            #get ID of selected item in treeview (iter path)

            Iterator = model.get_iter(path)
            value = model.get_value(Iterator, position)
            #wenn value = project, dann darf nur Typ building eingefügt werden usw...
            print value

    def ProjectTreeDragMotion(self,widget, drag_context, x, y, time):
        pass



    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).

        gtk.main()