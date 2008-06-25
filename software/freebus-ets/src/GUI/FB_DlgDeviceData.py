#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_DlgDeviceData.py
#Version: V0.1 , 19.06.2008
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

class FB_DlgDeviceData:

    __LogObj = None
    __GladeObj = None                #general object as glade interface
    __window = None

    #objects for manufacturer handling
    __ManufacturerList = None             #widget of Manufacturer List
    __ManufacturerListStore = None        #ListModel interface
    __ManufacturerListSelection = None    #Selection of List
    __SelectedManufacturer = 0            #current selected Manufacturer

    #object for product handling
    __productList = None             #widget of product List
    __productFrameLabel = None       #widget of FrameLabel of product List
    __productListStore = None        #ListModel interface



    def __init__(self, LogObj):
    # create a new window
        self.__LogObj = LogObj


        self.__GladeObj = gtk.glade.XML(Global.GUIPath + "freebus.glade","DeviceDataWindow")
        self.__window = self.__GladeObj.get_widget("DeviceDataWindow")

        #Init ManufacturerList
        self.InitManufacturerList()
        #Init ProductList
        self.InitProductList()


        dic = { "on_bCancel_clicked" : self.Cancel,
                "on_bClose_clicked" : self.Apply(),
                "on_ListManufacturer_cursor_changed" : self.ListManufacturerChange,
                }
        self.__GladeObj.signal_autoconnect(dic)

        #fill manufacturerlist
        self.UpdateManufacturerList()


        #show window
        self.__window.show()



       #-------------------------------------------------------------------------------------
    def InitManufacturerList(self):
        #init product_list
        self.__ManufacturerList = self.__GladeObj.get_widget("ListManufacturer")
        #create ListStore object with 1xpicture and 1xstring entry
        self.__ManufacturerListStore = gtk.ListStore(gtk.gdk.Pixbuf, str,str)
        self.__ManufacturerList.set_model(self.__ManufacturerListStore)
        self.text_cell = gtk.CellRendererText()            #Text Object
        self.img_cell = gtk.CellRendererPixbuf()           #Image Object
        self.column = gtk.TreeViewColumn()
        self.column.pack_start(self.img_cell, False)
        self.column.pack_start(self.text_cell,True)
        self.column.add_attribute(self.img_cell, "pixbuf",0)
        self.column.add_attribute(self.text_cell, "text", 1)
        self.column.set_attributes(self.text_cell, markup=1)
        self.__ManufacturerList.append_column(self.column)                #add objects t ofirst line of tree


    def InitProductList(self):
        #init product_list
        self.__productList = self.__GladeObj.get_widget("ListProducts")
        #create ListStore object with 1xpicture and 1xstring entry
        self.__productListStore = gtk.ListStore(gtk.gdk.Pixbuf, str)
        self.__productList.set_model(self.__productListStore)
        self.text_cell = gtk.CellRendererText()            #Text Object
        self.img_cell = gtk.CellRendererPixbuf()           #Image Object
        self.column = gtk.TreeViewColumn()
        self.column.pack_start(self.img_cell, False)
        self.column.pack_start(self.text_cell,True)
        self.column.add_attribute(self.img_cell, "pixbuf",0)
        self.column.add_attribute(self.text_cell, "text", 1)
        self.column.set_attributes(self.text_cell, markup=1)
        self.__productList.append_column(self.column)                #add objects t ofirst line of tree

        lblProducts = self.__GladeObj.get_widget("lblProducts")
        lblProducts.set_markup(unicode("<b>Produkte</b>" ,"ISO-8859-1"))


    def UpdateManufacturerList(self):
        image=gtk.gdk.pixbuf_new_from_file(Global.ImagePath + "ManufacturerChooser.png")

        #find out all of manufacturers
        sql = "SELECT * FROM manufacturer order by MANUFACTURER_ID"
        ListIterator = None

        Cursor = Global.DatabaseConnection.cursor()
        try:
            Cursor.execute(sql)
        except:
            pass

        ManuList = Cursor.fetchall()
        if(len(ManuList) > 0):
            for i in range(len(ManuList)):
                ListIterator = self.__ManufacturerListStore.append([image,ManuList[i][1],ManuList[i][0]])

        #no items found...
        else:
            pass


    def UpdateProductList(self,ManufacturerID):


        if(ManufacturerID <= 0):
            return

        #clear complete List
        self.__productListStore.clear()

        Cursor = Global.DatabaseConnection.cursor()

        #set frame label to current manufacturer
        sql = "SELECT * from manufacturer where MANUFACTURER_ID = " + ManufacturerID
        try:
            Cursor.execute(sql)
            ProductNameList = Cursor.fetchall()
        except:
            pass

        #first element of recordset (should only be one!)
        ProductName = "<b>Produkte von: " + ProductNameList[0][1] + "</b>"

        lblProducts = self.__GladeObj.get_widget("lblProducts")
        lblProducts.set_markup(unicode(ProductName ,"ISO-8859-1"))


        image=gtk.gdk.pixbuf_new_from_file(Global.ImagePath + "ProductChooser.png")

        #find out all of manufacturers
        sql = "SELECT * FROM catalog_entry where MANUFACTURER_ID = " + ManufacturerID
        ListIterator = None


        try:
            Cursor.execute(sql)
        except:
            pass

        ProdList = Cursor.fetchall()
        #print ProdList
        if(len(ProdList) > 0):
            for i in range(len(ProdList)):
                ListIterator = self.__productListStore.append([image,unicode(ProdList[i][4],"iso-8859-1")])

        #no items found...
        else:
            pass

    #Selection has been changed...
    def ListManufacturerChange(self,widget,data=None):
        #get current selection
        self.__ManufacturerListSelection =  self.__ManufacturerList.get_selection()
        (model, iter) = self.__ManufacturerListSelection.get_selected()
        #get Manufacturer-ID (column = 2)
        self.__SelectedManufacturer = self.__ManufacturerListStore.get_value(iter, 2)
        self.UpdateProductList(self.__SelectedManufacturer)


    def Apply(self,widget, data=None):
        gtk.Widget.destroy(self.__window)

    def Cancel(self,widget, data=None):
        gtk.Widget.destroy(self.__window)