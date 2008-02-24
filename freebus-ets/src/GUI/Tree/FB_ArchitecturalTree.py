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
pygtk.require("2.0")
import gtk
import gtk.glade

##general class for creating/intializing our project-tree
class FB_ArchitecturalTree:

    __LogObj = None
    __ArchModel = None
    __ImagePath = None
    __treestore = None
    __TreeObj = None
    __CurProjectObj = None


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

        self.__ImagePath = os.getcwd() + os.sep + "Image" + os.sep

        #create data structure/model
        self.__treestore = gtk.TreeStore(gtk.gdk.Pixbuf,str)

        self.__TreeObj.set_model(self.__treestore)

        image=gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "New.gif")

        self.__TreeIterator = self.__treestore.append(None, [image, "  kein Projekt aktiv"])

        #get TreePath for TreeRowReference
        TreePath = self.__treestore.get_path(self.__TreeIterator)
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

        # Allow drag and drop reordering of rows
        TreeObj.set_reorderable(True)

    #build the project tree, every time you create a new project or open an existing project
    def CreateNewTree(self, ProjectObj):
        #set current project object
        self.__CurProjectObj = ProjectObj
        #object of our achrchitect
        self.__ArchModel = self.__CurProjectObj.getArchModel()

        #set iterator to first position
        Iter = self.__treestore.get_iter_first()
        #get root node
        Node = self.__ArchModel.getDataRootNode(self.__ArchModel.getRootID())

        self.__treestore.set_value(Iter,1,self.__CurProjectObj.getProjectName())

        Index = 2 #2 = buildings
        Prefix = self.__ArchModel.getPrefix(Index)
        #get count of each part

        IDList = self.__ArchModel.getIDList(Node,Prefix)
        print IDList
        #getNode with given ID from IDList
        Obj = self.__ArchModel.getDOMObj()
        NodeList = Obj.getElementsByTagName(Prefix)[0].attributes
        Attr =  NodeList.getNamedItem("id").nodeValue
        #get node back to current ID
        if(Attr == IDList[0]):
            Node = Obj.getElementsByTagName(Prefix)[0]
            childs =  Node.childNodes
            #get element
            #name of Node
            print childs[1].nodeName
            #add Object to tree and get back new iteration object


            image = self.getImage(Prefix)
            iter =  self.__treestore.append(Iter, [image, childs[1].firstChild.data])

            #value of Node
            print childs[1].childNodes[0].nodeValue
            #check if existing sub nodes (floors, rooms ...)
            if(Node.hasChildNodes() == True):
                print "FLOOR"


    def getImage(self,Prefix):
        #get back buidling image
        print Prefix
        if(Prefix == 'building'):
            return gtk.gdk.pixbuf_new_from_file(self.__ImagePath + "building.png")


    #creates a new node at the project-tree under a given Parent-ID
    def NewTreeNode(self,NodePrefix,ParentID):
        #get node with given ID
        Obj = self.__ArchModel.getDOMObj()
        NodeList = Obj.getElementsByTagName(NodePrefix)

        if(len(NodeList) > 0):
            for i in range(len(NodeList)):
                childs = NodeList[i].childNodes
                #print childs.item(i).getAttribute("id")
                #for j in range(len(childs)):
                #print childs[2].

