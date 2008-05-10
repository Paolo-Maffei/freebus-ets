#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ArchitecturalTree.py
#Version: V0.1 , 24.02.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

import os
import pygtk
from Global import Global
pygtk.require("2.0")
import gtk
import gtk.glade

##general class for creating/intializing our project-tree
class FB_ArchitecturalTree:

    __LogObj = None
    __ImagePath = None
    __treestore = None
    __TreeObj = None
    __CurProjectObj = None

    ArchModel = None

       #tree-structure:
        #Project-Name                    (1)
        #    Building(s)                 (2)
        #        Floor(s)                (3)
        #            Room(s)             (4)
        #                Junction(s)     (5)
        #                Bus-Device(s)


    ##Constructor
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param PrjObj: Project Object
    def __init__(self,LogObj, TreeObj):
        self.__LogObj = LogObj
        self.__TreeObj = TreeObj

        #self.__ImagePath = os.getcwd() + os.sep + "Image" + os.sep
        self.__ImagePath = Global.ImagePath

        #create data structure/model

        self.__treestore = gtk.TreeStore(gtk.gdk.Pixbuf,str,str)
        self.__TreeObj.set_model(self.__treestore)
        image=gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "New.gif")
        self.__TreeIterator = self.__treestore.append(None, [image, "  kein Projekt aktiv", "OK"])

        #get TreePath for TreeRowReference
        #TreePath = self.__treestore.get_path(self.__TreeIterator)
        #for later use with gtk 2.4 or higher
        #treerowref = TreeRowReference(TreeObj.get_model(), TreePath)

        text_cell = gtk.CellRendererText()            #Text Object
        img_cell = gtk.CellRendererPixbuf()           #Image Object
        column = gtk.TreeViewColumn()
        column.pack_start(img_cell, False)
        column.pack_start(text_cell,True)
        column.add_attribute(img_cell, "pixbuf",0)
        column.add_attribute(text_cell, "text", 1)
        column.set_attributes(text_cell, markup=1)
        self.__TreeObj.append_column(column)                #add objects t ofirst line of tree
        self.__TreeObj.expand_all()

        # Allow drag and drop reordering of rows
        #TreeObj.set_reorderable(True)
        self.__TreeObj.enable_model_drag_dest([('text/plain', 0,Global.DND_BUILDING)],gtk.gdk.ACTION_COPY)

    def ClearTree(self):
        self.__treestore.clear()
        self.__TreeObj.set_model(self.__treestore)
        image=gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "New.gif")
        self.__TreeIterator = self.__treestore.append(None, [image, "  kein Projekt aktiv", "OK"])

    #build the project tree, every time you create a new project or open an existing project
    #should be developed a better solution.... ;-)
    def CreateNewTree(self, ProjectObj):


        #set current project object
        self.__CurProjectObj = ProjectObj
        #object of our achrchitect
        self.ArchModel = self.__CurProjectObj.getArchModel()

        #set iterator to first position
        BuildingIter = self.__treestore.get_iter_first()

        #get root node
        Node = self.ArchModel.getDataRootNode(self.ArchModel.getRootID())

        #Column 1
        self.__treestore.set_value(BuildingIter,1,self.__CurProjectObj.getProjectName())
        #Column 2
        self.__treestore.set_value(BuildingIter,2,self.ArchModel.getRootID())

        Obj = self.ArchModel.getDOMObj()

        #get all buildings
        BuildingPrefix = self.ArchModel.getPrefix(Global.DND_BUILDING)

        #get List of ID of given Prefix (building-1,building-2,...)
        IDList = self.ArchModel.getIDList(Node,BuildingPrefix)

        #for all buildings....
        for buildings in range(len(IDList)):
            LastBuildingIter = self.CreateTreeNode(IDList[buildings],BuildingIter,BuildingPrefix)

            #get all floors of given building
            FloorNode = self.ArchModel.getDataRootNode(IDList[buildings])
            FloorPrefix = self.ArchModel.getPrefix(Global.DND_FLOOR)
            FloorList = self.ArchModel.getIDList(FloorNode,FloorPrefix)
            #save last Iter
            FloorIter = LastBuildingIter
            #for all floors in current building
            for floors in range(len(FloorList)):
                LastFloorIter = self.CreateTreeNode(FloorList[floors],FloorIter,FloorPrefix)

                #get all rooms of given floor
                RoomNode = self.ArchModel.getDataRootNode(FloorList[floors])
                RoomPrefix = self.ArchModel.getPrefix(Global.DND_ROOM)
                RoomList = self.ArchModel.getIDList(RoomNode,RoomPrefix)
                #save last Iter
                RoomIter = LastFloorIter
                #for all rooms in current floor
                for rooms in range(len(RoomList)):
                    LastRoomIter = self.CreateTreeNode(RoomList[rooms],RoomIter,RoomPrefix)
                    #get all junctions of given room
                    JunctionNode = self.ArchModel.getDataRootNode(RoomList[rooms])
                    JunctionPrefix = self.ArchModel.getPrefix(Global.DND_JUNCTION)
                    JunctionList = self.ArchModel.getIDList(JunctionNode,JunctionPrefix)
                    #save last Iter
                    JunctionIter = LastRoomIter
                    #for all junctions in current room
                    for junction in range(len(JunctionList)):
                        LastJunctionIter = self.CreateTreeNode(JunctionList[junction],JunctionIter,JunctionPrefix)

        self.__TreeObj.expand_all()


    def CreateTreeNode(self,ID,Iterator,Prefix):
        BuildingNode = self.ArchModel.getDataRootNode(ID)
        #attr. will be saved in tree without visibilty
        Attr = self.ArchModel.getChildID(BuildingNode)
        Value = self.ArchModel.readDOMNodeValue(BuildingNode,"name")
        image = self.getImage(Prefix)
        iter =  self.__treestore.append(Iterator, [image, unicode(Value,"ISO-8859-1"), Attr])

        return iter


    def getImage(self,Prefix):
        #get back buidling image

        if(Prefix == 'building'):
            return gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "building.png")
        elif(Prefix == 'floor'):
            return gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "floor.png")
        elif(Prefix == 'room'):
            return gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "room.png")
        elif(Prefix == 'junctionbox'):
            return gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "junctionbox.png")

    #gets the iterator of a given path ( comes from a drop action)
    def getIterator(self,path):
        return self.__treestore.get_iter(path)

    def getTreeValue(self,Iterator, position):
        return self.__treestore.get_value(Iterator, position)