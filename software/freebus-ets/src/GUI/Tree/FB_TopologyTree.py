#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_TopologyTree.py
#Version: V0.1 , 12.05.2009
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
class FB_TopologyTree:

    __LogObj = None
    __ImagePath = None
    __treestore = None
    __TreeObj = None
    __CurProjectObj = None
    text_cell = None            #public object for treeview -> textcellrenderer
    img_cell = None             #public object for treeview -> cellrenderer
    column = None               #public object for treeview -> treeview column

    ArchModel = None

       #tree-structure:



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
        image=gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "building.png")
        self.__TreeIterator = self.__treestore.append(None, [image, "  kein Projekt aktiv", "OK"])

        #get TreePath for TreeRowReference
        #TreePath = self.__treestore.get_path(self.__TreeIterator)
        #for later use with gtk 2.4 or higher
        #treerowref = TreeRowReference(TreeObj.get_model(), TreePath)

        self.text_cell = gtk.CellRendererText()            #Text Object
        self.img_cell = gtk.CellRendererPixbuf()           #Image Object
        self.column = gtk.TreeViewColumn()
        self.column.pack_start(self.img_cell, False)
        self.column.pack_start(self.text_cell,True)
        self.column.add_attribute(self.img_cell, "pixbuf",0)
        self.column.add_attribute(self.text_cell, "text", 1)
        self.column.set_attributes(self.text_cell, markup=1)
        self.__TreeObj.append_column(self.column)                #add objects t ofirst line of tree
        self.__TreeObj.expand_all()
        #text_cell.set_property("editable",True)
        # Allow drag and drop reordering of rows
        #TreeObj.set_reorderable(True)
        self.__TreeObj.enable_model_drag_dest([('text/plain', 0,Global.DND_BUILDING)],gtk.gdk.ACTION_COPY)

    def ClearTree(self):
        self.__treestore.clear()
        self.__TreeObj.set_model(self.__treestore)
        image = gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "building.png")
        self.__TreeIterator = self.__treestore.append(None, [image, "  kein Projekt aktiv", "OK"])

    #build the project tree, every time you create a new project or open an existing project
    #should be developed a better solution.... ;-)
    def CreateNewTree(self, ProjectObj):

        #set current project object
        self.__CurProjectObj = ProjectObj
        #object of our achrchitect
        self.ArchModel = self.__CurProjectObj.getArchModel()

        #set iterator to first position
        TopologyIter = self.__treestore.get_iter_first()

        #get root node
        Node = self.ArchModel.getDataRootNode("Topology")

        #Column 1
        self.__treestore.set_value(TopologyIter,1,self.__CurProjectObj.getProjectName())
        #Column 2
        #self.__treestore.set_value(BuildingIter,2,self.ArchModel.getRootID())

        Obj = self.ArchModel.getDOMObj()

        #get all buildings
       # BuildingPrefix = self.ArchModel.getPrefix(Global.DND_BUILDING)

        #get List of ID of given Prefix (building-1,building-2,...)
        #IDList = self.ArchModel.getIDList(Node,BuildingPrefix)


        self.__TreeObj.expand_all()


    def CreateTreeNode(self,ID,Iterator,Prefix):
        BuildingNode = self.ArchModel.getDataRootNode(ID)
        #attr. will be saved in tree without visibilty
        Attr = self.ArchModel.getChildID(BuildingNode)
        Value = self.ArchModel.readDOMNodeValue(BuildingNode,"name")
        image = self.getImage(Prefix)
        iter =  self.__treestore.append(Iterator, [image, unicode(Value,"ISO-8859-1"), Attr])
        path = self.__treestore.get_path(Iterator)

        self.__TreeObj.expand_row(path, True)
        self.__CurProjectObj.isChanged = True
        return iter




    #gets the iterator of a given path ( comes from a drop action)
    def getIterator(self,path):
        return self.__treestore.get_iter(path)

    def getTreeValue(self,Iterator, position):
        return self.__treestore.get_value(Iterator, position)