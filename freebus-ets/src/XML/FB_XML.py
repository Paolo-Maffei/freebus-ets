#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_XML.py
#Version: V0.1 , 10.11.2007
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

import codecs
import xml.sax.handler

from xml.dom import minidom

from xml.dom.minidom import *
from XML.FB_XML_HANDLER import FB_XMLHandler
from XML.FB_XML_HANDLER import FB_ProductXMLHandler
from XML.FB_XML_HANDLER import FB_AppXMLHandler
from XML.FB_XML_HANDLER import FB_CommXMLHandler
from XML.FB_XML_HANDLER import FB_Prod2ProgrXMLHandler
from XML.FB_XML_HANDLER import FB_MaskXMLHandler
from FB_DATA import FB_Constants


##This class contains all Methods to work with the FB-XML Files
class FB_XML:

    __LogObj = None
    __DOMObj = None
    __xml_file = ""
    __handler = -1     #instance of XML-handler
    __ProductList = None    #List of instances of read Products

    ##Constructor
    #for each product file you have to create an instance of FB_XML
    def __init__(self,LogObj,file):
        self.__LogObj = LogObj
        self.__xml_file = file


    ##return the current DOM-Object
    def getDOMObj(self):
        self.__DOMObj = parse(self.__xml_file)
        return self.__DOMObj

    ##save Documents to XML
    def SaveDocument(self):
        try:
            #self.__DOMObj = self.getDOMObj()
            OutFileObj = open(self.__xml_file,"w")

            parentNode = self.__DOMObj.documentElement

            #suche alle hw_products -> in List
            SubNodeList =  parentNode.getElementsByTagName(FB_Constants.ProductNode[0])
            #read out data copy they into DOMObj
            if(self.__ProductList <> None):
                #iterate through each Product in ProductList
                for i in range(len(self.__ProductList)):
                    #for each element in Node: "ProductNode"
                    for j in range(1,len(FB_Constants.ProductNode)):
                        Value = self.__ProductList[i].getProduct(j)
                        #iterate List of Nodes within MainNode (ex. hw_product)
                        #find all Elements in hw_product
                        Element = SubNodeList[i].getElementsByTagName(FB_Constants.ProductNode[j])

                        #does Element-Node exist ? (different ets version-fils -> different element-counts
                        if(len(Element)>0):
                            if(FB_Constants.ProductNode[j] == Element[0].tagName):
                                #save internal Value to XML-Object
                                Element[0].firstChild.data = Value

            else:
                self.__LogObj.NewLog("error at saving product data -> no data object available",1)


            String = self.__DOMObj.toxml(encoding = "ISO-8859-1")

            OutFileObj.write(String)
            OutFileObj.close()

        except IOError:
            #LOG File
            self.__LogObj.NewLog(IOError.message + " " + IOError.filename + " " + IOError.errno,2)


    ##parse entire XML-Data-File. All Sub-Handler will be called automatically
    ##After that you can call all provided functions to get products,
    ##applications, communcations-objects etc.
    #@param xml-File: Path and Filename of sourcefile
    #@param return: return-value
    def parseXMLFile(self):
        try:
            self.__DOMObj = self.getDOMObj()

            self.__handler = FB_XMLHandler.FB_XMLHandler(self.__LogObj)
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
            AppList = xml_handler.getAppList()
            Manufac = xml_handler.getManufacturerList()

            return [AppList,Manufac]

        except:
            self.__LogObj.NewLog("Error at 'getApplications'" ,2)
            return -1

    ##detect all communication-objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_CommunicationObj Instances
    def getCommunicationObjects(self,xml_handler):

        try:
            CommObjList = xml_handler.getCommObjList()

            return CommObjList

        except:
            self.__LogObj.NewLog("Error at 'getCommunicationObjects'" ,2)
            return -1

    ##detect all product to programs assignments within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_Prod2Prog Instances
    def getProd2Progr(self,xml_handler):

        try:
            Prod2Prog = xml_handler.getProd2ProgrList()

            return Prod2Prog

        except:
            self.__LogObj.NewLog("Error at 'getProd2Progr'" ,2)
            return -1

    ##detect all mask objects within the given Product-Data-File
    #@param xml-File: Path and Filename of sourcefile
    #@return: List of FB_Mask Instances
    def getMask(self,xml_handler):

        try:
            Mask = xml_handler.getMaskList()

            return Mask

        except:
            self.__LogObj.NewLog("Error at 'getMaskList'" ,2)
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

    ##Add text elements to given DOM-Obj of XML-File
    #@param SubNode: (Sub)-Node which contains al Nodes with textelements which should be edited
    #@param Element: List of TextElements according to SubNode
    def EditTextElement(self,SubNode,ElementList):
        try:pass

            #NodeList = SubNode.childNodes
            #print NodeList
        except:
            #LOG File
            self.__LogObj.NewLog("Error edit a Textelement:"  ,2)

