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
import thread
import Queue
import threading
import thread


from Global import Global
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from GUI import FB_NewProjectWindow
from GUI import FB_OpenProjectWindow
from GUI import FB_DlgDeviceData
from GUI.Tree import FB_ArchitecturalTree
from GUI.Tree import FB_TopologyTree
from DATABASE import FB_DlgDatabase

from FB_PROJECT import FB_ArchitecturalDataModel
from XML import FB_XMLConverter
from XML import FB_XML_PRODUCT



import sqlite3

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
    __TopologyTree = None        #widget of topology treeview
    __PopUpGlade = None

    __popupNewHandlerID = 0      #signale Hander ID for popupMenu "New Item" button
    __popupEditHandlerID = 0     #signal handler ID for popupMenu "Change Name" button

    treestore = None
    curDragDataType = 0            #the current Type of draged data (builidng,floor,rooms---)

    tmpCounter = 0

    def __init__(self, LogObj):
    # create a new window
        self.__LogObj = LogObj
        self.__CurProjectObj = None

        #get screensize
        self.__WindowWidth = gtk.gdk.screen_width()
        self.__WindowHeigth = gtk.gdk.screen_height()

        self.__GladeObj = gtk.glade.XML(Global.GUIPath  + "freebus.glade","MainFrame")
        #get widget of window
        self.window = self.__GladeObj.get_widget("MainFrame")
        self.window.fullscreen()

        if(self.__GladeObj == None):
           self.__LogObj.NewLog("Error at intializing GUI-Interface (Glade-Object-MainFrame)",1)
           return

        #-------------------------------------------------------------------------------------

        #popupmenu init
        self.__PopUpGlade = gtk.glade.XML(Global.GUIPath  + "freebus.glade","mnuPopupTree")
        self.__mnuPopup =  self.__PopUpGlade.get_widget("mnuPopupTree")

        if(self.__mnuPopup == None):
           self.__LogObj.NewLog("Error at intializing GUI-Interface (Glade-Object-Popup Menu)",1)
           return

        pop = {
                #Popupmenu
               # "on_mnuNewItem_activate": self.PopupNew,
                "on_mnuChangeName_activate": self.PopupChangeName,
                "on_mnuDeleteGroup_activate": self.PopupDelete,
                "on_mnuPropertyGroup_activate":self.PopupProperty

                }

        self.__PopUpGlade.signal_autoconnect(pop)


       #-------------------------------------------------------------------------------------

       #popupmenu Topology

       #-------------------------------------------------------------------------------------

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

        #get widget object of Topology Tree
        self.__TopologyTreeWidget = self.__GladeObj.get_widget("TopologyTree")

        dic = { "on_MainFrame_destroy" : gtk.main_quit ,
                "on_Quitt_activate" : self.QuittApp,
                #Menu items
                "on_new_project_activate" : self.MenuNewProject,
                "on_open_project_activate" : self.MenuOpenProject,
                "on_Save_activate" : self.MenuSaveProject,
                "on_button_drag_data_get" : self.DragDataGet,
                "on_ConvertDeviceData_activate":self.Converter,
                "on_ImportDeviceData_activate":self.ImportProductData,
                "on_ShowDeviceData_activate":self.ShowDeviceData,
                "on_DlgDatabase_activate":self.DatabaseSetting,

                #ProjectTree
                "on_ProjectTree_drag_data_received" : self.ProjectTreeDropData,
                "on_ProjectTree_drag_motion" : self.ProjectTreeDragMotion,
                "on_ProjectTree_button_press_event": self.ProjectTreeButtonPress,

                #TopologyTree
                "on_TopologyTree_button_release_event":self.TopologyTreeButtonPress

                #GroupAddressTree

                }
        self.__GladeObj.signal_autoconnect(dic)

       #-------------------------------------------------------------------------------------


        #create Project Tree
        self.__ArchTree = FB_ArchitecturalTree.FB_ArchitecturalTree(self.__LogObj,self.__ProjTree)
        self.__TopologyTree = FB_TopologyTree.FB_TopologyTree(self.__LogObj,self.__TopologyTreeWidget)



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

    #show Database-settings-Dialog
    def DatabaseSetting(self, widget, data=None):
        FB_DlgDatabase.FB_DlgDatabase(self.__LogObj)

    #show dlg device data
    def ShowDeviceData(self,widget, data=None):
        FB_DlgDeviceData.FB_DlgDeviceData(self.__LogObj)
    #start the converter dialog
    def Converter(self,widget, data=None):
        XML = FB_XMLConverter.FB_XMLConverter(self.__LogObj)

    def ConverterThread(self, XMLConverter):
        XMLConverter()

    #start Import to SQL Dialog
    def ImportProductData(self,widget, data=None):
        FBProductData = FB_XML_PRODUCT.FB_XML_PRODUCT(self.__LogObj)

    #set current project object
    def SetCurrProject(self, ProjObj):
        self.__CurProjectObj = ProjObj
        self.__CurArchObj = self.__CurProjectObj.getArchModel

        #reorganize our project-tree
        if(self.__ProjTree <> None):
            self.__ArchTree.ClearTree()
            self.__ArchTree.CreateNewTree(self.__CurProjectObj)

            self.__TopologyTree.ClearTree()
            self.__TopologyTree.CreateNewTree(self.__CurProjectObj)

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
            #parent-element (ex: project-1,building-1 ...
            ParentID = model.get_value(Iterator, 2)
            #selected ID (ex:project, building,room, floor...
            SelID = self.__ArchTree.ArchModel.getPrefix(self.curDragDataType-1)

            #remove last part (-1 ..)
            end = ParentID.find('-')
            if(end <> -1):
                Type = ParentID[0: end]
            else:
                Type = ParentID

            #wenn value = project, dann darf nur Typ building eingefügt werden usw...
            #thats why -> targetID - 1 (building -> project; floor->building ...)
            if (SelID == Type):
                PicturePrefix = self.__ArchTree.ArchModel.getPrefix(self.curDragDataType)
                self.OpenDlgNewStructureElement(ParentID, Iterator,self.__ArchTree, PicturePrefix)


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

    #handles the general dialog to add any structure element
    def OpenDlgNewStructureElement(self, ParentID, TreeIterator, TreeObject, PicturePrefix):
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

            #add object and gets the new ID (topology-1 ...)
            ID = self.__ArchTree.ArchModel.addChild(ParentID)

            if(Name == ""):
                Name = ID

            if(ID <> None):
              #  print "neue ID " + ID + " ; Name: " + Name + " ; ParentID = " + ParentID
                self.__ArchTree.ArchModel.setName(ID,Name)
                TreeObject.CreateTreeNode(ID, TreeIterator, PicturePrefix)

            window.destroy()
        else:
            window.destroy()

    #callback of detach menu to popup
    def PopupDetach(self,menu, widget):
        pass
        #print "Detach"

    #general event handler to handle button events
    def ProjectTreeButtonPress(self,widget, event):
        #attach treeview "ProjectTree" to popup
        if(self.__mnuPopup.get_attach_widget() <> None):
            self.__mnuPopup.detach()
        self.__mnuPopup.attach_to_widget(widget,self.PopupDetach)
        #Ignore double-clicks and triple-clicks  -> do right click to show popup menu
        if (event.button == 3 and event.type == gtk.gdk.BUTTON_PRESS and self.__CurProjectObj <> None):
            #get New-Button Widget and unvisible it, only used in topology/group address tree

            NewButtonWidget = self.__PopUpGlade.get_widget("mnuNewItem")
            NewButtonWidget.hide()
            self.__mnuPopup.popup(None,None,None,event.button,event.time)

    def TopologyTreeButtonPress(self,widget,event):
        #attach treeview "TopologyTree" to popup
        if(self.__mnuPopup.get_attach_widget() <> None):
            self.__mnuPopup.detach()
        self.__mnuPopup.attach_to_widget(widget,self.PopupDetach)

        #Ignore double-clicks and triple-clicks  -> do right click to show popup menu
        if (event.button ==  3 and event.type == gtk.gdk.BUTTON_RELEASE and self.__CurProjectObj <> None ):
            #init Datafield
            Data = [0,0,0,0]

            #check which item has been clicked (area, line)
            #1. get treeview
            treeselection = self.__TopologyTreeWidget.get_selection()
            #Iterator = model.get_iter(path)
            (model, iter) = treeselection.get_selected()
            #get the widget object of the menuitem "new"
            NewButtonWidget = self.__PopUpGlade.get_widget("mnuNewItem")

            #in case of root element -> iter will be None-Type
            #check for root-selection
            #print model.iter_parent(iter)

            if(model.iter_parent(iter) == None):
                ParentID = self.__ArchTree.ArchModel.TOPOLOGY_ROOT_ID

                PicturePrefix = 20    #to idendiy the right picture for tree visualisation
                Data[0] = 1
                Data[1] = ParentID
                Data[2] = iter
                Data[3] = PicturePrefix
                #NewButtonWidget.connect("activate",self.PopupNew,(1,ParentID,iter,PicturePrefix))
                label = NewButtonWidget.child
                label.set_text("Neuen Bereich anlegen")


            #sub node selected (lines are possible)
            else:
                #get the ID (=ParentID) of the selected object -> thats the parent for our new line
                #we need the child ID (ID of the seletced object)

                ParentID =  model.get_value(iter,2) #get value of Column 2 = Attributevalue = ID (Column 0 = picture, 1 = Name)
                #check prefix (in case of line is selected -> only device can be added)
                #get the nodename and compare it with the prefix to know if line or area or whatever was selected
                ParentNodeName = self.__ArchTree.ArchModel.getNodeName(ParentID)

                if(ParentNodeName == self.__ArchTree.ArchModel.TOPOLOGY_AREA):
                    PicturePrefix = 21
                    Data[0] = 2
                    Data[1] = ParentID
                    Data[2] = iter
                    Data[3] = PicturePrefix
                    #NewButtonWidget.connect("activate",self.PopupNew,(2,ParentID,iter,PicturePrefix))
                    label = NewButtonWidget.child
                    label.set_text("Neue Linie anlegen")
                elif(ParentNodeName == self.__ArchTree.ArchModel.TOPOLOGY_LINE):
                    PicturePrefix = 22
                    Data[0] = 3
                    Data[1] = ParentID
                    Data[2] = iter
                    Data[3] = PicturePrefix
                    #NewButtonWidget.connect("activate",self.PopupNew,(3,ParentID,iter,PicturePrefix))
                    label = NewButtonWidget.child
                    label.set_text(unicode("Neues Gerät einfügen","ISO-8859-1"))


            NewButtonWidget.show()
            self.__popupNewHandlerID = NewButtonWidget.connect("activate",self.PopupNew,(Data[0],Data[1],Data[2],Data[3]))
            #show popup
            #popup menu: (parent_menu_shell : the menu shell containing the triggering menu item or None.
            #             parent_menu_item : the menu item whose activation triggered the popup or None.
            #             func : a user supplied function used to position the menu or None.
            #             button : the mouse button which was pressed to initiate the event.
            #             activate_time : the time at which the activation event occurred.
            #             data :  optional data to be passed to func
            self.__mnuPopup.popup(None,None,None,event.button,event.time)


    #popup menu -> New item
    def PopupNew(self,widget, data):
        #date structure:
            #[0] = type (1 = new Area of topology ; 2 ) new line in area of topology
            #[1] = Parent-ID of DOM-Node (in case of new area -> parent = topology-1,
            #[2] = iterator of tree
            #[3] = PicturePrefix for tree (building, floor, area, line ...)=

        type = data[0]
        ParentID = data[1]
        iter = data[2]
        PicPrefix = data[3]

        if(type == 1 or type == 2):
            #new area should be created or  #new line should be created
            self.OpenDlgNewStructureElement(ParentID,iter, self.__TopologyTree, self.__ArchTree.ArchModel.getPrefix(PicPrefix))
            #important to disconnect this event!
            widget.disconnect(self.__popupNewHandlerID)
            #new device should be created
        elif(type == 3):
            pass
        else:
            pass

    #Popup activity ;
    #edit item name
    def PopupChangeName(self,widget, data=None):
        try:
            menuParent = widget.parent.get_attach_widget()
            self.__mnuPopup.detach()

            #depending on widget which is attached to the popup do different things...
            #in case of "ProjectTree"
            if(menuParent.get_name() == self.__ProjTree.get_name()):
                #first get the right widget which was initiator
                #change to editmode
                self.__ArchTree.text_cell.set_property('editable', True)
                #find current selected position at treeview
                path,column = self.__ProjTree.get_cursor()
                self.__ProjTree.set_cursor( path,column ,True )
                model = self.__ProjTree.get_model()
                self.__ArchTree.text_cell.connect('edited', self.CellChanged, model)

            elif(menuParent.get_name() == self.__TopologyTreeWidget.get_name()):
                #first get the right widget which was initiator
                #change to editmode
                self.__TopologyTree.text_cell.set_property('editable', True)
                #find current selected position at treeview
                path,column = self.__TopologyTreeWidget.get_cursor()
                self.__TopologyTreeWidget.set_cursor( path,column ,True )
                model = self.__TopologyTreeWidget.get_model()
                self.__TopologyTree.text_cell.connect('edited', self.CellChanged, model)


        except:
            pass

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
        #ArchTree is OK; we dont nedd the TopologyTree here, because internal the ArchModel is the one and only
        #in the project (belongs in every xxTree-module)
        self.__ArchTree.ArchModel.setName(ID,new_text)
        #reset editable property of tree
        self.__ArchTree.text_cell.set_property('editable', False)
        self.__TopologyTree.text_cell.set_property('editable', False)

        self.__CurProjectObj.isChanged = True


    #popup acitivity -> delete item
    def PopupDelete(self,widget, data=None):

        try:
            menuParent = widget.parent.get_attach_widget()
            self.__mnuPopup.detach()

            #depending on widget which is attached to the popup do different things...
            #in case of "ProjectTree"
            if(menuParent.get_name() == self.__ProjTree.get_name()):
                #get the selected item
                treeselection = self.__ProjTree.get_selection()
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
            #Topology Tree
            elif(menuParent.get_name() == self.__TopologyTreeWidget.get_name()):
                #get the selected item
                treeselection = self.__TopologyTreeWidget.get_selection()
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
                    self.__TopologyTree.ArchModel.removeData(Attr)
                    self.__CurProjectObj.isChanged = True

        except:
            pass

    #popup activity -> show propertys
    def PopupProperty(self,widget, data=None):
        print "Prop"




    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
      #  gtk.gdk.threads_init()
        gtk.main()

    #quitt Application
    def QuittApp(self,widget, data=None):

        Global.DatabaseConnection.close()

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
