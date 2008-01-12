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

    ##Constructor
    def __init__(self,LogObj):
        self.__LogObj = LogObj

    ##return the current DOM-Object
    def getDOMObj(self):
        return self.__DOMObj

    ##return List which contains all editable Textnodes (correct Level)
    def getTextLevel(self):
        parent = self.__DOMObj.documentElement
        return parent.childNodes

    ##save Documents to XML
    def SaveDocument(self, DOMObj, xml_file):
        try:
            OutFileObj = open(xml_file,"w")
            String = DOMObj.toxml().encode('utf-8')
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
    def parseXMLFile(self,xml_file):
        try:
            self.__DOMObj = parse(xml_file)    #DOM Object

            handler = FB_XMLHandler.FB_XMLHandler(self.__LogObj)
            saxparser = xml.sax.make_parser()
            saxparser.setContentHandler(handler)
            saxparser.parse(xml_file)

            return handler
        except:
            self.__LogObj.NewLog("General error at saxparser: " + xml_file,2)
            return -1

    ##detect all Products within the given Product-Data-File
    #@return: List of FB_Product Instances
    def getProducts(self,xml_handler):

        try:
            ProductList = xml_handler.getProductList()
            return ProductList

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
    def CreateProductFile(self,xml_file):
        try:

            Start = """<?xml version="1.0" encoding="ISO-8859-1" ?>
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
            OutFileObj = open(xml_file,"w+")
            #write das zeugs
            String = self.__DOMObj.toxml().encode('ISO-8859-1')

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
                text = self.__DOMObj.createTextNode("doof")
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

