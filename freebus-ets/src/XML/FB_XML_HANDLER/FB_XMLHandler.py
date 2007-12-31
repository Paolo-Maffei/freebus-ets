#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_XMLHandler.py
#Version: V0.1 , 25.12.2007
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================

from xml.dom.minidom import *
import codecs
import xml.sax
import sys, string
from XML.FB_XML_HANDLER import FB_ProductXMLHandler
from XML.FB_XML_HANDLER import FB_AppXMLHandler

##Class for Extracting Products from FB-XML Productfiles
class FB_XMLHandler(xml.sax.ContentHandler):

    __LogObj = None
    __products = []
    __prod = None
    __prod_XMLHandler = None     #private object of FB_ProductXMLHandler
    __app_XMLHandler = None      #private object of FB_AppXMLHandler

    #Constructor for FB_XMLHandler.
    def __init__(self, LogObj):
        self.__LogObj = LogObj
        #Product-Handling
        self.__prod_XMLHandler = FB_ProductXMLHandler.FB_ProductXMLHandler(self.__LogObj)
        #Application-Handling
        self.__app_XMLHandler = FB_AppXMLHandler.FB_AppXMLHandler(self.__LogObj)

    #return List of Instances of type FB_Products
    def getProductList(self):
        return self.__prod_XMLHandler.getProductList()

    #return List of Instances of type FB_Applications
    def getAppList(self):
        return self.__app_XMLHandler.getAppList()

    #return List of Instances of type FB_Manufacturer
    def getManufacturerList(self):
        return self.__app_XMLHandler.getManufacturerList()


    def startDocument(self):
        try:
            pass

        except SAXException:
            print "SAXError"

    def endDocument(self):
        try:
            pass

        except SAXException:
            print "SAXError"

    def startElement(self, eName, attrs):
        try:
            self.__prod_XMLHandler.startElement(eName, attrs)
            self.__app_XMLHandler.startElement(eName, attrs)

        except SAXException:
            print "Error again"

    def endElement(self,eName):
        try:
            self. __prod_XMLHandler.endElement(eName)
            self.__app_XMLHandler.endElement(eName)

        except SAXException:
            print "Error again"


    def characters(self ,char):
        try:
            self.__prod_XMLHandler.characters(char)
            self.__app_XMLHandler.characters(char)

        except SAXException:
             print "Error again"
