#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ProgramFrame.py
#Version: V0.1 , 29.08.2009
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

import os
import sys
import time
#import thread
#import Queue
#import threading
#import thread
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import pickle

from Global import Global
from GUI import FB_DlgConnectionManager

class FB_ProgramFrame(object):

    __curProject = None            #project object
    __cbConnections = None         #widget combo connections

    __parentClass = None            #object of its own class

    def __init__(self,curProject):

        self.__parentClass = self
        self.__curProject = curProject

        GladeObj = gtk.glade.XML(Global.GUIPath + Global.GladeFile,"winProgramming")

        dic = { "on_bConnectionConfig_clicked":self.ShowConnectionManager ,
                "on_bTestConnection_clicked":self.ClickTestConnection,
                "on_bConnect_toggled":self.ToggleConnect,

               }
        GladeObj.signal_autoconnect(dic)

        self.__cbConnections = GladeObj.get_widget("cbConnections")
        liststore = gtk.ListStore(str,str)    #just one string at first..., 2nd string for GUID
        self.__cbConnections.set_model(liststore)
        self.text_cell = gtk.CellRendererText()
        self.__cbConnections.pack_start(self.text_cell,True)
        self.__cbConnections.add_attribute(self.text_cell, "text", 0)

        self.LoadConnectionFromDB()
        self.UpdateUserConnections()
        winProgramming = GladeObj.get_widget("winProgramming")
        winProgramming.show()



    #Dialog: Connection-Manager
    def ShowConnectionManager(self,widget, data=None):
       FB_DlgConnectionManager.FB_DlgConnectionManager(self.__curProject, self.__parentClass)

    #button: Test-Connection
    #open the current connection and test it...
    def ClickTestConnection(self,widget, data=None):
        #get the connection object of the selected connection
        model = self.__cbConnections.get_model()
        iter = self.__cbConnections.get_active_iter()
        id = model.get_value(iter,1)
        con = self.getEIBConnection(id)
        con.doConnect()

    def ToggleConnect(self,widget, data=None):
        pass

    #gets the instance of a FB_EIBConnection with the given id
    def getEIBConnection(self,id):
        RValue = None

        if self.__curProject <> None:
            if self.__curProject.eibConnectionList <> None:
                for i in range(len(self.__curProject.eibConnectionList)):
                    if id == self.__curProject.eibConnectionList[i].getID():
                        RValue = self.__curProject.eibConnectionList[i]
                        break
        return RValue

    ##function to update the combobox in parentframe to show/select for user
    #@param cbConnections: widget of the combobox in parentframe which should be loaded
    def UpdateUserConnections(self):

        try:
            #copy list in combo connections in program_Frame (parent)
            if(self.__curProject <> None):# and self._MyConnection <> None):
                model = self.__cbConnections.get_model()
                #save id of the current connection / which is currently selected
                curIter = self.__cbConnections.get_active_iter()
                if curIter <> None:
                    idsaved = model.get_value(curIter,1)    #column 1 = id
                else:
                    idsaved = 0

                model.clear()

                IterSaved = None        #init Iterator

                for i in range(len(self.__curProject.eibConnectionList)):
                    Name = self.__curProject.eibConnectionList[i].getName()
                    typeID = self.__curProject.eibConnectionList[i].getType()
                    Type = str(Global.ConTypesText[typeID])

                    id = self.__curProject.eibConnectionList[i].getID()

                    tmp = Name + " mit '" + Type + "'"
                    iter = model.append([tmp, id])
                    #look if saved id is still in list and set this item to the active item
                    if idsaved == id:
                        IterSaved = iter

                #connection still existing...
                if IterSaved <> None:
                    self.__cbConnections.set_active_iter(IterSaved)
                else:
                    if len(self.__curProject.eibConnectionList) > 0:
                        self.__cbConnections.set_active(0)

            else:
                #no connections in list or no valid project is loaded
                model = self.__cbConnections.get_model()
                model.clear()
        except:
            pass

    def LoadConnectionFromDB(self):
        #try:
            cursor = Global.DatabaseConnection.cursor()
            cursor.execute("SELECT * FROM Connections")

            del self.__curProject.eibConnectionList[0:len(self.__curProject.eibConnectionList)]
            for row in cursor:
                tmpCon = pickle.loads(row[2])    #column 2 contains class data
                self.__curProject.eibConnectionList.append(tmpCon)
       #except:
           # pass