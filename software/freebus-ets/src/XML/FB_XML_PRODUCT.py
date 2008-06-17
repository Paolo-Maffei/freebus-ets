#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_XML_PRODUCT.py
#Version: V0.1 , 10.11.2007
#Version: V0.2 , 23.05.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

import codecs
import xml.sax.handler
from Global import Global

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import threading
import thread

from xml.dom import minidom

from xml.dom.minidom import *
from XML.FB_XML_HANDLER import FB_XMLHandler
from XML.FB_XML_HANDLER import FB_ProductXMLHandler
from XML.FB_XML_HANDLER import FB_AppXMLHandler
from XML.FB_XML_HANDLER import FB_CommXMLHandler
from XML.FB_XML_HANDLER import FB_Prod2ProgrXMLHandler
from XML.FB_XML_HANDLER import FB_MaskXMLHandler
from XML.FB_XML_HANDLER import FB_ParameterXMLHandler
from FB_DATA import FB_Constants

from pysqlite2 import dbapi2 as sqlite2

##This class contains all Methods to work with the FB-XML Files
#For each xml-product file you have to create an instance of "FB_XML"
#in this version the sax-parser will be used
class FB_XML_PRODUCT:

    __LogObj = None
    __DOMObj = None
    __xml_file = ""
    __handler = -1     #instance of XML-handler
    __ProductList = []    #List of instances of read Products
    __AppList = []        #List of instances of read Applications
    __ManufactList = []   #List of instances of read Manufacturers
    __CommObjList = []    #List of instances of read Communication Objects
    __Prod2ProgrList = [] #List of instances of read Product to Program
    __MaskList = []       #List of instances of read Mask
    __ParamList = []      #List of instances of read Paramter
    __ParamTypeList = []  #List of instances of read ParamterType
    __ParamListVList = [] #List of instances of read ParamterList of Values
    Finisch = False

    lblManufacturer = None
    lblProducts = None
    lblApps = None
    lblComObj = None
    lblParam = None



    ##Constructor
    #for each product file you have to create an instance of FB_XML
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param file: Path and Filename of the xml-data-file
    def __init__(self,LogObj):
        self.__LogObj = LogObj

        self.DlgImportGlade = gtk.glade.XML(Global.GUIPath  + "freebus.glade","DlgImportFromXML")
        self.ImportDlg = self.DlgImportGlade.get_widget("DlgImportFromXML")

        #get widgets of textfields
        self.__txtSourceFile = self.DlgImportGlade.get_widget("txtSourceFile")
        self.__progress = self.DlgImportGlade.get_widget("ImportProgress")

        self.lblManufacturer = self.DlgImportGlade.get_widget("ManufacturerCount")
        self.lblProducts = self.DlgImportGlade.get_widget("Product_Count")
        self.lblApps = self.DlgImportGlade.get_widget("App_Count")
        self.lblComObj = self.DlgImportGlade.get_widget("Com_Count")
        self.lblParam = self.DlgImportGlade.get_widget("Param_Count")

        Value = "0 Stück"

        self.lblManufacturer.set_text(unicode(Value,"ISO-8859-1"))
        self.lblProducts.set_text(unicode(Value,"ISO-8859-1"))
        self.lblApps.set_text(unicode(Value,"ISO-8859-1"))
        self.lblComObj.set_text(unicode(Value,"ISO-8859-1"))
        self.lblParam.set_text(unicode(Value,"ISO-8859-1"))


        self.__SelFolder = ""
        self.__SelFile = ""
        self.Finisch = False

        dic = {"on_bSelect_clicked": self.FileChooser,
               "on_bCancel_clicked": self.bCancel,
               "on_bImport_clicked": self.bImport }

        self.DlgImportGlade.signal_autoconnect(dic)


        self.ImportDlg.show()

    #open FileChooser
    def FileChooser(self, widget, data=None):

        DlgFileChooserGlade = gtk.glade.XML(Global.GUIPath  + "freebus.glade","DlgFileChooser")
        DlgFileChooser = DlgFileChooserGlade.get_widget("DlgFileChooser")

        #create file-filter
        filter = gtk.FileFilter()
        filter.add_pattern("*.xml")
        filter.set_name("XML Produktdaten")
        DlgFileChooser.add_filter(filter)

        response = DlgFileChooser.run()

        if(response == gtk.RESPONSE_OK):
            self.__SelFolder = DlgFileChooser.get_current_folder()
            FileFolder = DlgFileChooser.get_filename()

            #split SelFile (get_filename return complete path + filename)
            List = FileFolder.split("\\")
            tFileName = List[len(List)-1]
            tFileName = tFileName.split(".")

            #Folder and Filename complete
            self.__xml_file = FileFolder
            self.__txtSourceFile.set_text(self.__xml_file)

            DlgFileChooser.destroy()
        else:
            DlgFileChooser.destroy()

    #close dialog
    def bCancel(self,widget, data=None):
        self.response = gtk.RESPONSE_CANCEL
        self.ImportDlg.destroy()


    #start convert
    def bImport(self,widget, data=None):

        self.response = gtk.RESPONSE_OK

        productList = []
        appList = []
        ManufactList = []
        paramList = []

        Value = "0 Stück"

        self.lblManufacturer.set_text(unicode(Value,"ISO-8859-1"))
        self.lblProducts.set_text(unicode(Value,"ISO-8859-1"))
        self.lblApps.set_text(unicode(Value,"ISO-8859-1"))
        self.lblComObj.set_text(unicode(Value,"ISO-8859-1"))
        self.lblParam.set_text(unicode(Value,"ISO-8859-1"))

        #thread.start_new(self.worker_thread, (self.parseXMLFile(),))
        XMLHandler = self.parseXMLFile()

        if(XMLHandler != -1):
            con = sqlite2.connect(Global.Database)
            if(con <> None):

                #--------------- Products --------------------------
                productList = self.getProducts(XMLHandler)
                Value = str(len(productList)) + " Stück"
                self.lblProducts.set_text(unicode(Value,"ISO-8859-1"))
                self.WriteToSQL(con, productList, "hw_product")
                #--------------- Applications / Manufacturer -------
                [appList, ManufactList] = self.getApplications(XMLHandler)
                Value = str(len(appList)) + " Stück"
                self.lblApps.set_text(unicode(Value,"ISO-8859-1"))
                Value = str(len(ManufactList)) + " Stück"
                self.lblManufacturer.set_text(unicode(Value,"ISO-8859-1"))
                self.WriteToSQL(con, appList, "application_program")
                self.WriteToSQL(con, ManufactList, "manufacturer")
                #--------------- Communication Objects --------------
                commList  = self.getCommunicationObjects(XMLHandler)
                Value = str(len(commList)) + " Stück"
                self.lblComObj.set_text(unicode(Value,"ISO-8859-1"))
                self.WriteToSQL(con, commList, "communication_object")
                #-------------------- Mask --------------------------
                maskList = self.getMask(XMLHandler)
                self.WriteToSQL(con, maskList, "mask")
                #-------------------- Product to Program-------------
                ProdProgList = self.getProd2Progr(XMLHandler)
                self.WriteToSQL(con, ProdProgList, "product_to_program")
                #-------------------- Parameter ---------------------
                paramList = self.getParameter(XMLHandler)
                Value = str(len(paramList)) + " Stück"
                self.lblParam.set_text(unicode(Value,"ISO-8859-1"))
                self.WriteToSQL(con, paramList, "parameter")
                #-------------------- ParameterType ---------------------
                paramTypeList  = self.getParameterType(XMLHandler)
                self.WriteToSQL(con, paramTypeList, "parameter_type")
                #-------------------- Parameter List of Values ----------
                paramListV  = self.getParameterListV(XMLHandler)
                self.WriteToSQL(con, paramListV, "parameter_list_of_values")


                con.close()

    def worker_thread(self, process_import):

        # hier wird gearbeitet
        if(process_import <> None):
            XMLHandler = process_import()
            if(XMLHandler != -1):
                print "OK"

    def WriteToSQL(self,Connection,List,Table):
        #create a cursor
        cur = Connection.cursor()

        #iterate throuch List

        for j in range(len(List)):

            sql = "INSERT INTO " + Table + " ("

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #Product found...
            if(Table == "hw_product"):
                ColumnList = FB_Constants.ProductNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
               # print sql
                #check if Product is already existing...
                sqlExist = "SELECT PRODUCT_ID FROM hw_product WHERE PRODUCT_ID = " + str(List[j].getProductID())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    #do something else
                    print sql
                    self.__LogObj.NewLog("Doppeltes Produkt: " + sql,0)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #Application found
            elif(Table == "application_program"):
                ColumnList = FB_Constants.AppNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
               # print sql
                #check if Product is already existing...
                sqlExist = "SELECT PROGRAM_ID FROM application_program WHERE PROGRAM_ID = " + str(List[j].getProgramID())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:

                    print sql
                    self.__LogObj.NewLog("Doppelte Applikation: " + sql,0)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #Manufacturer found
            elif(Table == "manufacturer"):
                ColumnList = FB_Constants.ManufacturerNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql
                #check if Product is already existing...
                sqlExist = "SELECT MANUFACTURER_ID FROM manufacturer WHERE MANUFACTURER_ID = " + str(List[j].getManufactID())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    print sql
                    self.__LogObj.NewLog("Doppelter Hersteller: " + sql,0)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #Communication Object found
            elif(Table == "communication_object"):
                ColumnList = FB_Constants.CommObjNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql

                #check if Product is already existing...
                sqlExist = "SELECT OBJECT_ID,OBJECT_UNIQUE_NUMBER FROM communication_object WHERE OBJECT_ID = " + str(List[j].getObjID()) + " AND OBJECT_UNIQUE_NUMBER = " + str(List[j].getObjUniqueNo())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    #do something else
                    #print str(List[j].getObjUniqueNo())

                    print sql
                    self.__LogObj.NewLog("Doppeltes Kommunikations-Object: " + sql,0)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #Mask Object found
            elif(Table == "mask"):
                ColumnList = FB_Constants.MaskNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql

                #check if Product is already existing...
                sqlExist = "SELECT MASK_ID FROM mask WHERE MASK_ID = " + str(List[j].getMaskID())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    print sql
                    self.__LogObj.NewLog("Doppelte Maske: " + sql,0)
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #product to program Object found
            elif(Table == "product_to_program"):
                ColumnList = FB_Constants.Prod2ProgrNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql

                #check if Product is already existing...
                sqlExist = "SELECT PROD2PROG_ID FROM product_to_program WHERE PROD2PROG_ID = " + str(List[j].getProd2ProgID())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    print sql
                    self.__LogObj.NewLog("Doppeltes ProductToProgram: " + sql,0)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #parameter
            elif(Table == "parameter"):
                ColumnList = FB_Constants.ParaNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql

                #check if Product is already existing...
                sqlExist = "SELECT PARAMETER_ID,PARAMETER_NUMBER FROM parameter WHERE PARAMETER_ID = " + \
                            str(List[j].getParameterID()) + " AND PARAMETER_NUMBER = " + str(List[j].getParameterNumber())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    print sql
                    self.__LogObj.NewLog("Doppelter Parameter: " + sql,0)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

            #parameterType
            elif(Table == "parameter_type"):
                ColumnList = FB_Constants.ParaTypeNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql

                #check if Product is already existing...
                sqlExist = "SELECT PARAMETER_TYPE_ID FROM parameter_type WHERE PARAMETER_TYPE_ID = " + str(List[j].getParameterTypeID2())

                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    print sql
                    self.__LogObj.NewLog("Doppeltes Parameter_Type: " + sql,0)
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
            #parameter List of Values
            elif(Table == "parameter_list_of_values"):
                ColumnList = FB_Constants.ParaListVNode

                for i in range(1,List[j].getMaxIndex()+1):
                    sql = sql + ColumnList[i]

                    if(i < List[0].getMaxIndex()):
                        sql = sql + ","

                #complete sql string
                sql = sql + ") " + List[j].getSQLValueList()
                #print sql

                #check if Product is already existing...
                sqlExist = "SELECT PARAMETER_TYPE_ID,PARAMETER_VALUE_ID FROM parameter_list_of_values WHERE PARAMETER_TYPE_ID = " + \
                           str(List[j].getParameterTypeID3()) + " AND PARAMETER_VALUE_ID = " + str(List[j].getParameterValueID())
                Cursor = Connection.cursor()
                Cursor.execute(sqlExist)

                if(len(Cursor.fetchall()) == 0):
                   #if item doesnt exist.... insert new record
                    try:
                        cur.execute(sql)
                    except:
                        print sql
                        self.__LogObj.NewLog("Falscher SQL-Befehl: " + sql,1)
                else:
                    print sql
                    self.__LogObj.NewLog("Doppeltes Parameter List of Values: " + sql,0)


        Connection.commit()

    ##return the current DOM-Object
    def getDOMObj(self):
        self.__DOMObj = parse(self.__xml_file)
        return self.__DOMObj

    ##save Documents to XML
    def SaveDocument(self):
        try:
            #self.__DOMObj = self.getDOMObj()
            OutFileObj = open(self.__xml_file,"w")

            #***************************************************************************************
            #products
            if(self.SaveElements(FB_Constants.ProductNode, self.__ProductList) == False):
                self.__LogObj.NewLog("error at saving product data -> no data object available",1)
            #***************************************************************************************
            #Applications
            if(self.SaveElements(FB_Constants.AppNode, self.__AppList) == False):
                self.__LogObj.NewLog("error at saving application data -> no data object available",1)
            #***************************************************************************************
            #Manufacturer
            if(self.SaveElements(FB_Constants.ManufacturerNode, self.__ManufactList) == False):
                self.__LogObj.NewLog("error at saving manufacturer data -> no data object available",1)
            #***************************************************************************************
            #Communication Objects
            if(self.SaveElements(FB_Constants.CommObjNode, self.__CommObjList) == False):
                self.__LogObj.NewLog("error at saving communications objects -> no data object available",1)
            #***************************************************************************************
            #Product to Program assignment
            if(self.SaveElements(FB_Constants.Prod2ProgrNode, self.__Prod2ProgrList) == False):
                self.__LogObj.NewLog("error at saving Product to Program objects -> no data object available",1)
            #***************************************************************************************
            #Mask
            if(self.SaveElements(FB_Constants.MaskNode, self.__MaskList) == False):
                self.__LogObj.NewLog("error at saving mask data -> no data object available",1)
            #***************************************************************************************
            #Parameter
            if(self.SaveElements(FB_Constants.ParaNode , self.__ParamList) == False):
                self.__LogObj.NewLog("error at saving Parameter data -> no data object available",1)
            #***************************************************************************************
            #ParameterType
            if(self.SaveElements(FB_Constants.ParaTypeNode , self.__ParamTypeList) == False):
                self.__LogObj.NewLog("error at saving ParameterType data -> no data object available",1)
            #***************************************************************************************
            #ParameterListOfValues
            if(self.SaveElements(FB_Constants.ParaListVNode , self.__ParamListVList) == False):
                self.__LogObj.NewLog("error at saving ParameterListOfValues data -> no data object available",1)


            String = self.__DOMObj.toxml(encoding = "ISO-8859-1")
            OutFileObj.write(String)
            OutFileObj.close()

        except IOError:
            #LOG File
            self.__LogObj.NewLog(IOError.message + " " + IOError.filename + " " + IOError.errno,2)

    ##copy the internal data to the DOM-Obj -> save data back to file
    #@param NodeList: List of main-tree Elements (xml-product base data) -> see Constants
    #@param ElementList: List of elements which should be saved
    def SaveElements(self,NodeList,ElementList):
        try:

            parentNode = self.__DOMObj.documentElement
            SubNodeList =  parentNode.getElementsByTagName(NodeList[0])
            #print SubNodeList
            #read out data copy they into DOMObj
            if(ElementList != None):
                #iterate through each Product in ProductList
                for i in range(len(ElementList)):
                    #for each element in Node: "ProductNode"

                    for j in range(1,len(NodeList)):
                        if(NodeList[0] == "manufacturer"):
                            Value = ElementList[i].getManufacturer(j)
                        elif(NodeList[0] == "hw_product"):
                            Value = ElementList[i].getProduct(j)
                        elif(NodeList[0] == "mask"):
                            Value = ElementList[i].getMask(j)
                        elif(NodeList[0] == "application_program"):
                            Value = ElementList[i].getApp(j)
                        elif(NodeList[0] == "communication_object"):
                            Value =  ElementList[i].getCommObj(j)
                        elif(NodeList[0] == "product_to_program"):
                            Value = ElementList[i].getProd2Prog(j)
                        elif(NodeList[0] == "parameter"):
                            Value = ElementList[i].getParameter(j)
                        elif(NodeList[0] == "parameter_type"):
                            Value = ElementList[i].getParameterType(j)
                        elif(NodeList[0] == "parameter_list_of_values"):
                            Value = ElementList[i].getParameterListValues(j)

                        #iterate List of Nodes within MainNode (ex. hw_product)
                        #find all Elements in hw_product
                        Element = SubNodeList[i].getElementsByTagName(NodeList[j])
                        #does Element-Node exist ? (different ets version-fils -> different element-counts
                        if(len(Element)>0):
                            if(NodeList[j] == Element[0].tagName):
                                #save internal Value to XML-Object
                                Element[0].firstChild.data = unicode(Value,"ISO-8859-1")

                return True
            else:
                return False

        except:
            self.__LogObj.NewLog("Exception at saving Elements to xml object at ",2)
            return False


    ##parse entire XML-Data-File. All Sub-Handler will be called automatically
    ##After that you can call all provided functions to get products,
    ##applications, communcations-objects etc.
    #@param xml-File: Path and Filename of sourcefile
    #@param return: return-value
    def parseXMLFile(self):
        try:

            #saxparser
            self.__handler = FB_XMLHandler.FB_XMLHandler(self.__LogObj)
            #self.__handler.ignorableWhitespace(['\n', '\r', '\t'])
            saxparser = xml.sax.make_parser()
            saxparser.setContentHandler(self.__handler)
            saxparser.parse(self.__xml_file)

            return self.__handler
        except:
            self.__LogObj.NewLog("General error at saxparser: " + self.__xml_file,2)
            return -1

    ##detect all Products within the given Product-Data-File
    #@return: List of FB_Product Instances
    def getProducts(self,xml_handler):

        try:
            self.__ProductList = xml_handler.getProductList()
            return self.__ProductList

        except:
            self.__LogObj.NewLog("Error at 'getProducts'" ,2)
            return -1


    ##detect all Applications within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_Applications Instances and Manufacturer-Data
    #to get Manufacturer-Data you also have to call getApplications
    def getApplications(self,xml_handler):

        try:
            self.__AppList = xml_handler.getAppList()
            self.__ManufactList = xml_handler.getManufacturerList()

            return [self.__AppList,self.__ManufactList]

        except:
            self.__LogObj.NewLog("Error at 'getApplications'" ,2)
            return -1

    ##detect all communication-objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_CommunicationObj Instances
    def getCommunicationObjects(self,xml_handler):

        try:
            self.__CommObjList = xml_handler.getCommObjList()

            return self.__CommObjList

        except:
            self.__LogObj.NewLog("Error at 'getCommunicationObjects'" ,2)
            return -1

    ##detect all product to programs assignments within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_Prod2Prog Instances
    def getProd2Progr(self,xml_handler):

        try:
            self.__Prod2ProgrList = xml_handler.getProd2ProgrList()

            return self.__Prod2ProgrList

        except:
            self.__LogObj.NewLog("Error at 'getProd2Progr'" ,2)
            return -1

    ##detect all mask objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_Mask Instances
    def getMask(self,xml_handler):

        try:
            self.__MaskList = xml_handler.getMaskList()

            return self.__MaskList

        except:
            self.__LogObj.NewLog("Error at 'getMaskList'" ,2)
            return -1


    ##detect all parameter objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_Parameter Instances
    def getParameter(self,xml_handler):

        try:
            self.__ParamList = xml_handler.getParameter()
            return self.__ParamList

        except:
            self.__LogObj.NewLog("Error at 'getParameter'" ,2)
            return -1

    ##detect all parameterType objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_ParameterType Instances
    def getParameterType(self,xml_handler):

        try:
            self.__ParamTypeList = xml_handler.getParameterType()

            return self.__ParamTypeList

        except:
            self.__LogObj.NewLog("Error at 'getParameterType'" ,2)
            return -1

    ##detect all parameterList of Values objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_ParameterListV Instances
    def getParameterListV(self,xml_handler):

        try:
            self.__ParamListVList = xml_handler.getParameterList()

            return self.__ParamListVList

        except:
            self.__LogObj.NewLog("Error at 'getParameterListV'" ,2)
            return -1


#*********************************************************************************
    ##craete new xml-product-data file and add root node
    #@param xml-Filename+Path:
    def CreateProductFile(self):
        try:

            #Start = """<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>\n
            Start = """<?xml version=\"1.0\" ?>\n
                <eib-products></eib-products>"""
            self.__DOMObj = minidom.parseString(Start)

            newDocument = self.__DOMObj.documentElement

            #insert all nodes through iteration of MainNodes
            #or choise of single nodes

#----------------------------------------------------------------------------------
            #manufacturer
            self.CreateNode(newDocument,FB_Constants.ManufacturerNode)
#----------------------------------------------------------------------------------
            #functional_entity
            self.CreateNode(newDocument,FB_Constants.FunctionalNode)
#----------------------------------------------------------------------------------
            #bcu_type
            self.CreateNode(newDocument,FB_Constants.BCUNode)
#----------------------------------------------------------------------------------
            #symbol
            self.CreateNode(newDocument,FB_Constants.SymbolNode)
#----------------------------------------------------------------------------------
            #hw_product
            self.CreateNode(newDocument,FB_Constants.ProductNode)
#----------------------------------------------------------------------------------
            #catalog_entry
            self.CreateNode(newDocument,FB_Constants.CatalogNode)
#----------------------------------------------------------------------------------
            #medium_type
            self.CreateNode(newDocument,FB_Constants.MediumNode)
#----------------------------------------------------------------------------------
            #mask
            self.CreateNode(newDocument,FB_Constants.MaskNode)
#----------------------------------------------------------------------------------
            #application_program
            self.CreateNode(newDocument,FB_Constants.AppNode)
#----------------------------------------------------------------------------------
            #virtual_device
            self.CreateNode(newDocument,FB_Constants.VirDeviceNode)
#----------------------------------------------------------------------------------
            #product to program...
            self.CreateNode(newDocument,FB_Constants.Prod2ProgrNode)
#----------------------------------------------------------------------------------
            #communication objects
            self.CreateNode(newDocument,FB_Constants.CommObjNode)
#----------------------------------------------------------------------------------
            #Parameter
            self.CreateNode(newDocument,FB_Constants.ParaNode)
#----------------------------------------------------------------------------------
            #ParameterType
            self.CreateNode(newDocument,FB_Constants.ParaTypeNode)
#----------------------------------------------------------------------------------
            #Parameter List of Values
            self.CreateNode(newDocument,FB_Constants.ParaListVNode)
#----------------------------------------------------------------------------------


#.....ab hier der Rest

            #open the new file
            OutFileObj = open(self.__xml_file,"w+")
            #write das zeugs
            String = self.__DOMObj.toxml(encoding = "ISO-8859-1")

            OutFileObj.write(String)
            OutFileObj.close()

        except IOError:
            #LOG File
            self.__LogObj.NewLog(IOError.message + " " + IOError.filename + " " + IOError.errno,2)

    ##craete ElementNodes at the new xml data file
    #@param Document: Document of the new DOM-object file
    #@param Element: Element which will be added
    def CreateNode(self,Document,Element):
        try:
            item = self.__DOMObj.createElement(Element[0])
            Document.appendChild(item)
            #SubNode-List
            SubNode = self.__DOMObj.getElementsByTagName(Element[0])

            for i in range(1,len(Element)):

                text = self.__DOMObj.createTextNode(" ")
                item = self.__DOMObj.createElement(Element[i])
                item.appendChild(text)
                SubNode[0].appendChild(item)

        except:
            #LOG File
            self.__LogObj.NewLog("Error at creation of Node:" + Element ,2)


class ProgressBar(threading.Thread):

    def __init__(self,BarObj,Converter,Dlg):
        threading.Thread.__init__(self)
        self.BarObj = BarObj
        self.Converter = Converter
        self.Dlg = Dlg


    def run(self):
        gtk.gdk.threads_enter()
        while self.Converter.Finisch == False:

            #self.Dlg.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))
            if(self.Converter.LineCount > 0):
                self.visu = "%3.2f" % (float(str(self.Converter.CurLine)) / float(str(self.Converter.LineCount)))
                #print self.visu
                if(self.Converter.CurLine > self.Converter.LineCount):
                    self.visu = 1.0
                self.BarObj.set_fraction(float(self.visu))
                while gtk.events_pending():
                    gtk.main_iteration(False)
                sleep(0.02)
        gtk.gdk.threads_leave()

