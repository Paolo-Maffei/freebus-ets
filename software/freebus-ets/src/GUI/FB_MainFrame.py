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
import time
from Global import Global
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from GUI import FB_NewProjectWindow
from GUI import FB_OpenProjectWindow
from GUI.Tree import FB_ArchitecturalTree
from FB_PROJECT import FB_ArchitecturalDataModel




class FB_MainFrame:

    __WindowWidth = 0
    __WindowHeigth = 0
    __LogObj = None
    __CurProjectObj = None         #Project object
    __CurArchObj = None            #architectural model of current project
    __GladeObj = None
    __GUIPath = ""
    __ImagePath = ""
    __ProjTree = None
    __TreeIterator = None        #Iterator-Object for Tree
    __ArchTree = None            #Object for Tree-Class
    __handelboxToolbar = None    #widget object of handlebox toolbar
    __mnuPopup = None            #Object for popup menu

    treestore = None
    curDragDataType = 0            #the current Type of draged data (builidng,floor,rooms---)

    def __init__(self, LogObj):
    # create a new window
        self.__LogObj = LogObj
        self.__CurProjectObj = None

        #get screensize
        self.__WindowWidth = gtk.gdk.screen_width()
        self.__WindowHeigth = gtk.gdk.screen_height()

        self.__GladeObj = gtk.glade.XML(Global.GUIPath  + "freebus.glade","MainFrame")

        if(self.__GladeObj == None):
           self.__LogObj.NewLog("Error at intializing GUI-Interface (Glade-Object-MainFrame)",1)
           return

        #-------------------------------------------------------------------------------------

        #popupmenu init
        PopupGlade = gtk.glade.XML(Global.GUIPath  + "freebus.glade","mnuPopupTree")
        self.__mnuPopup =  PopupGlade.get_widget("mnuPopupTree")

        if(self.__mnuPopup == None):
           self.__LogObj.NewLog("Error at intializing GUI-Interface (Glade-Object-Popup Menu)",1)
           return

        pop = {
                #Popupmenu
                "on_mnuChangeName_activate": self.PopupChangeName,
                "on_mnuDeleteGroup_activate": self.PopupDelete,
                "on_mnuPropertyGroup_activate":self.PopupProperty
                }

        PopupGlade.signal_autoconnect(pop)


       #-------------------------------------------------------------------------------------

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
                "on_Quitt_activate" : self.QuittApp,
                "on_new_project_activate" : self.MenuNewProject,
                "on_open_project_activate" : self.MenuOpenProject,
                "on_Save_activate" : self.MenuSaveProject,
                "on_button_drag_data_get" : self.DragDataGet,

                #ProjectTree
                "on_ProjectTree_drag_data_received" : self.ProjectTreeDropData,
                "on_ProjectTree_drag_motion" : self.ProjectTreeDragMotion,
                "on_ProjectTree_button_press_event": self.TreeButtonPress


                }
        self.__GladeObj.signal_autoconnect(dic)

       #-------------------------------------------------------------------------------------


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
            #print "Fehler save "
            self.__LogObj.NewLog("Error at saving Projectdata -> CurProjectObj is Nonetype",1)

    #set current project object
    def SetCurrProject(self, ProjObj):
        self.__CurProjectObj = ProjObj
        self.__CurArchObj = self.__CurProjectObj.getArchModel

        #reorganize our project-tree
        if(self.__ProjTree <> None):
            self.__ArchTree.ClearTree()
            self.__ArchTree.CreateNewTree(self.__CurProjectObj)
            self.__handelboxToolbar.show()


    #get the type of the draged data
    def DragDataGet(self,widget, drag_context, selection, targetID, time):
        self.curDragDataType = targetID

    #add object to tree -> drop object over treeview
    def ProjectTreeDropData(self,treeview, drag_context, x, y, selection, targetID, timestamp):
        drop_info = treeview.get_dest_row_at_pos(x, y)
        if drop_info:
            model = treeview.get_model()
            path, position = drop_info

            #compare info with position/path object and add building,florr,room ...
            #get ID of selected item in treeview (iter path)
            Iterator = model.get_iter(path)
            #position is always 2 (column) to idendifiy the type of node
            #child-element (ex: project-1,building-1 ...
            Attr = model.get_value(Iterator, 2)
            #selected ID (ex:project, building,room, floor...
            SelID = self.__ArchTree.ArchModel.getPrefix(self.curDragDataType-1)

            #remove last part (-1 ..)
            end = Attr.find('-')
            if(end <> -1):
                Type = Attr[0: end]
            else:
                Type = Attr

            #wenn value = project, dann darf nur Typ building eingefügt werden usw...
            #thats why -> targetID - 1 (building -> project; floor->building ...)
            if (SelID == Type):
                #open dialog to give a new name
                #AddStructureElement = FB_AddStructureElement.FB_AddStructureElement(self.__LogObj, self,"Reserve")
                GladeObj = gtk.glade.XML(Global.GUIPath + "freebus.glade","DlgAddStructureElement")

                window = GladeObj.get_widget("DlgAddStructureElement")
                txtElementName = GladeObj.get_widget("txtElementName")
                #wait for closing dialog
                response = window.run()

                if(response == gtk.RESPONSE_OK):
                    #Default Name
                    Name = txtElementName.get_text()
                    window.destroy()
                    #add object
                    ID = self.__ArchTree.ArchModel.addChild(Attr)
                    self.__ArchTree.ArchModel.setName(ID,Name)
                    self.__ArchTree.CreateTreeNode(ID, Iterator, self.__ArchTree.ArchModel.getPrefix(self.curDragDataType))
                else:
                    window.destroy()

    #check if type ok for drop position (cursorlayout!)
    #currently not completed --- for later use ti optimize
    def ProjectTreeDragMotion(self,treeview, drag_context, x, y, time):
        drop_info = treeview.get_dest_row_at_pos(x, y)
        if drop_info:
            model = treeview.get_model()
            path, position = drop_info
            #compare info with position/path object and add building,florr,room ...
            #get ID of selected item in treeview (iter path)
            Iterator = model.get_iter(path)
            #position is always 2 (column) to idendifiy the type of node
            value = model.get_value(Iterator, 2)

            #wenn value = project, dann darf nur Typ building eingefügt werden usw...
            #thats why -> targetID - 1 (building -> project; floor->building ...)
            if (value == self.__ArchTree.ArchModel.getPrefix(self.curDragDataType-1)):
                pass

    #general event handler to handle button events
    def TreeButtonPress(self,widget, event):
        #Ignore double-clicks and triple-clicks  -> do right click to show popup menu
        if (event.button == 3 and event.type == gtk.gdk.BUTTON_PRESS):
            self.__mnuPopup.popup(None,None,None,event.button,event.time)


    #Popup activity
    def PopupChangeName(self,widget, data=None):
        #change to editmode
        self.__ArchTree.text_cell.set_property('editable', True)
        #find current selected position at treeview
        path,column = self.__ProjTree.get_cursor()
        self.__ProjTree.set_cursor( path,column ,True )
        model = self.__ProjTree.get_model()
        self.__ArchTree.text_cell.connect('edited', self.CellChanged, model)

    #will be called if a item has been changed (name of node...)
    def CellChanged(self,cell, path, new_text, user_data):
        #get treeview object from context (user_data)
        treeview = user_data
        #write new text to tree at column 1
        treeview[path][1] = new_text
        #get Iterator of given path (selected item)
        Iterator = treeview.get_iter(path)
        #find ID from cloumn 2 (building-2 etc.)
        ID = treeview.get_value(Iterator, 2)
        #write new text to architectural model (internal data)
        self.__ArchTree.ArchModel.setName(ID,new_text)
        #reset editable property of tree
        self.__ArchTree.text_cell.set_property('editable', False)
        self.__CurProjectObj.isChanged = True


    def PopupDelete(self,widget, data=None):
        #get the selected item
        treeselection = self.Tree.get_selection()
        treestore, Iterator = treeselection.get_selected()
        #get ID of selected item
        Attr = treestore.get_value(Iterator, 2)

        end = Attr.find('-')
        if(end <> -1):
            Type = Attr[0: end]
        else:
            Type = Attr

        if(Type <> self.__ArchTree.ArchModel.getPrefix(Global.DND_PROJECT)):
            #finaly:
            #delete treeobjects
            treestore.remove(Iterator)
            #delete internal data
            self.__ArchTree.ArchModel.removeData(Attr)
            self.__CurProjectObj.isChanged = True

    def PopupProperty(self,widget, data=None):
        print "Prop"




    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).

        gtk.main()

    #quitt Application
    def QuittApp(self,widget, data=None):
        if(self.__CurProjectObj <> None):
            if(self.__CurProjectObj.isChanged == True):
                msgbox = gtk.MessageDialog(parent = self.window, buttons = gtk.BUTTONS_YES_NO,
                                           flags = gtk.DIALOG_MODAL, type = gtk.MESSAGE_QUESTION,
                                           message_format = Global.QUITTWITHOUTSAVE )

                msgbox.set_title(Global.QUITMSGTITLE)
                result = msgbox.run()
                msgbox.destroy()
                if result == gtk.RESPONSE_YES:
                    pass
                else:
                    #Quitt without saving
                    gtk.main_quit()
            else:
                gtk.main_quit()
        else:
            gtk.main_quit()
