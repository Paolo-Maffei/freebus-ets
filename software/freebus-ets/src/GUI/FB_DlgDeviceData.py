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
    __productListSelection = None    #Selection of List
    __SelectedProduct = 0            #current selected Product

    #object for Application handling
    __appList = None             #widget of Application List
    __lblApps = None             #widget of FrameLabel ao App-box
    __lblApplicationName = None  #widget of Info Label Application-Name
    __lblProgramVersion = None   #widget of Info Label Program Version
    __lblPEI = None              #widget of Info Label PEI
    __appsListStore = None       #ListModel interface
    __appListSelection = None    #Selection of List
    __SelectedApplication = 0    #current selected Application (ListRow)
    __ApplicationNameList = []   #Application of Database Content


    def __init__(self, LogObj):
    # create a new window
        self.__LogObj = LogObj


        self.__GladeObj = gtk.glade.XML(Global.GUIPath + "freebus.glade","DeviceDataWindow")
        self.__window = self.__GladeObj.get_widget("DeviceDataWindow")

        #Init ManufacturerList
        self.InitManufacturerList()
        #Init ProductList
        self.InitProductList()
        #Init Application List
        self.InitAppList()


        dic = { "on_bCancel_clicked" : self.Cancel,
                "on_bClose_clicked" : self.Apply,
                "on_ListManufacturer_cursor_changed" : self.ListManufacturerChange,
                "on_ListProducts_cursor_changed" : self.ListProductsChange,
                "on_ListApps_cursor_changed" : self.ListAppsChange,
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
        #create ListStore object with 1xpicture and 1xstring entry and 1xstring ProductID
        self.__productListStore = gtk.ListStore(gtk.gdk.Pixbuf, str,str)
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

    def InitAppList(self):
        #init app-List
        self.__appList = self.__GladeObj.get_widget("ListApps")
        #create ListStore object with 1xpicture and 1xstring AppName and 1xstring ProgramID
        self.__appsListStore = gtk.ListStore(gtk.gdk.Pixbuf, str,str)
        self.__appList.set_model(self.__appsListStore)
        self.text_cell = gtk.CellRendererText()            #Text Object
        self.img_cell = gtk.CellRendererPixbuf()           #Image Object
        self.column = gtk.TreeViewColumn()
        self.column.pack_start(self.img_cell, False)
        self.column.pack_start(self.text_cell,True)
        self.column.add_attribute(self.img_cell, "pixbuf",0)
        self.column.add_attribute(self.text_cell, "text", 1)
        self.column.set_attributes(self.text_cell, markup=1)
        self.__appList.append_column(self.column)                #add objects t ofirst line of tree

        #Frame Label
        self.__lblApps = self.__GladeObj.get_widget("lblApps")
        self.__lblApps.set_markup(unicode("<b>Applikationen</b>" ,"ISO-8859-1"))
        #Info Label...
        self.__lblApplicationName = self.__GladeObj.get_widget("lblApplicationName")
        self.__lblProgramVersion = self.__GladeObj.get_widget("lblProgramVersion")
        self.__lblPEI = self.__GladeObj.get_widget("lblPEI")

        self.__lblApplicationName.set_text("")
        self.__lblProgramVersion.set_text("")
        self.__lblPEI.set_text("")

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
        #clear InformationLIst of Applications
        self.UpdateAppInformation(-1)

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
                ListIterator = self.__productListStore.append([image,unicode(ProdList[i][4],"iso-8859-1"),ProdList[i][1]])

        #no items found...
        else:
            pass

    def UpdateAppList(self,ProductID):
        if(ProductID <= 0):
            return

        self.__ApplicationNameList = []

        #clear complete List
        self.__appsListStore.clear()
        #clear InformationLIst of Applications
        self.UpdateAppInformation(-1)

        Cursor = Global.DatabaseConnection.cursor()

        #first: get program_id of given product_id:
        sql = "SELECT PRODUCT_ID,PROGRAM_ID from product_to_program where PRODUCT_ID = " + ProductID

        try:
            Cursor.execute(sql)
            ProdProgrList = Cursor.fetchall()
        except:
            pass

        #second: create Application List
        for i in range(len(ProdProgrList)):

            sql = "SELECT * from application_program where PROGRAM_ID = " + str(ProdProgrList[i][1])
            try:
                Cursor.execute(sql)
                TempList = Cursor.fetchall()
                #no zero-item ?
                if(len(TempList) > 0):
                    self.__ApplicationNameList.append(TempList)

            except:
                pass

        image=gtk.gdk.pixbuf_new_from_file(Global.ImagePath + "AppsChooser.png")

        #third: show Application List
        if(len(self.__ApplicationNameList) > 0):
            for i in range(len(self.__ApplicationNameList)):
                ListIterator = self.__appsListStore.append([image,unicode(self.__ApplicationNameList[i][0][3],"iso-8859-1"),self.__ApplicationNameList[i][0][0]])

        #no items found...
        else:
            pass

        #write frame Label to current Product
        sql = "SELECT * FROM catalog_entry where PRODUCT_ID = " + ProductID
        try:
            Cursor.execute(sql)
            AppList = Cursor.fetchall()
        except:
            pass

        #

        AppName = "<b>Applikationen von: " + AppList[0][4] + "</b>"
        self.__lblApps.set_markup(unicode(AppName ,"ISO-8859-1"))



        #UpdateApp-Information Line
    def UpdateAppInformation(self, ListRow):

        if(ListRow >= 0):
            #Info Label: App-Name
            self.__lblApplicationName.set_text(unicode("Applikation: " + self.__ApplicationNameList[ListRow][0][3]  ,"ISO-8859-1"))
            #Info Label: Program Version
            VersionHex = str(self.__ApplicationNameList[ListRow][0][4])
            Version = "%X" % int(VersionHex)
            Version = float(Version) / 10.0
            self.__lblProgramVersion.set_text("Program-Version: " + str(Version))
            #Info Label PEI Prog
            #self.__lblPEI
        else:
            self.__lblApplicationName.set_text("")
            self.__lblProgramVersion.set_text("")


    #Selection of ManufacturerList has been changed...
    def ListManufacturerChange(self,widget,data=None):
        #get current selection
        self.__ManufacturerListSelection =  self.__ManufacturerList.get_selection()
        (model, iter) = self.__ManufacturerListSelection.get_selected()
        #get Manufacturer-ID (column = 2)
        self.__SelectedManufacturer = self.__ManufacturerListStore.get_value(iter, 2)
        #return Manufacturer ID
        self.UpdateProductList(self.__SelectedManufacturer)

    #Selection of Products has been changed
    def ListProductsChange(self, widget, data=None):
         #get current selection
        self.__productListSelection =  self.__productList.get_selection()
        (model, iter) = self.__productListSelection.get_selected()
        #get Product-ID (column = 2)
        self.__SelectedProduct = self.__productListStore.get_value(iter, 2)
        #return Product ID
        self.UpdateAppList(self.__SelectedProduct)

    #selection of Application has been changed
    def ListAppsChange(self, widget, data=None):
        #get current selection
        self.__appListSelection =  self.__appList.get_selection()
        (model, iter) = self.__appListSelection.get_selected()
        path = self.__appsListStore.get_path(iter)
        #return item-number in listcontrol
        self.__SelectedApplication = path[0]
        self.UpdateAppInformation(self.__SelectedApplication)


    def Apply(self,widget, data=None):
        gtk.Widget.destroy(self.__window)

    def Cancel(self,widget, data=None):
        gtk.Widget.destroy(self.__window)