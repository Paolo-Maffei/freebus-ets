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


from xml.dom.minidom import *
from XML.FB_XML_HANDLER import FB_XMLHandler
from XML.FB_XML_HANDLER import FB_ProductXMLHandler
from XML.FB_XML_HANDLER import FB_AppXMLHandler


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

    ##load XML Data from file and save as DOM Object
    def LoadDocument(self,xml_file):
        try:

            self.__DOMObj = parse(xml_file)

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


