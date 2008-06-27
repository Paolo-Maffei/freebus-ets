#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_CatalogXMLHandler.py
#Version: V0.1 , 25.12.2007
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 15.06.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================


from FB_DATA import FB_CatalogEntry

##General XML-Handler Class, parse entire XML-Data File and fill alle Data-Structures
##Products, Applications, Communications-objects
class FB_CatalogXMLHandler():

    __LogObj = None
    __CatalogEntry = []
    __Catalog = None        #prviate object for catalog-Data
    __Index = 0
    __isCatalogEntry = False       #Catalog-Entry found ?


    __isCatalogEntry_ID = False    #CATALOG_ENTRY_ID
    __isProduct_ID = False         #PRODUCT_ID
    __isManufacturerID = False     #MANUFACTURER_ID
    __isOrderNumber = False        #ORDER_NUMBER
    __isEntryName = False          #ENTRY_NAME
    __isEntryWidthModul = False    #ENTRY_WIDTH_IN_MODULES
    __isEntryWidthMM = False       #ENTRY_WIDTH_IN_MILLIMETERS
    __isDIN_Flag = False           #DIN_FLAG
    __isPageNumber = False         #PAGE_NUMBER
    __isDesignationType = False    #DESIGNATION_TYPE
    __isEntryStatusCode = False    #ENTRY_STATUS_CODE
    __isRegistrationTS = False     #REGISTRATION_TS




    def __init__(self, LogObj):
        self.__LogObj = LogObj
        self.__Catalog = FB_CatalogEntry.FB_CatalogEntry()
        self.__CatalogEntry = []                #init List


    #return List of Instances of type FB_CatalogEntry
    def getCatalogList(self):
        return self.__CatalogEntry


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
            #print eName

            if(eName == "catalog_entry"):
                self.__isCatalogEntry = True

            elif(eName == "CATALOG_ENTRY_ID"):
                if(self.__isCatalogEntry == True):
                    self.__isCatalogEntry_ID = True

            elif(eName == "PRODUCT_ID"):
                if(self.__isCatalogEntry == True):
                    self.__isProduct_ID = True

            elif(eName == "MANUFACTURER_ID"):
                if(self.__isCatalogEntry == True):
                    self.__isManufacturerID = True

            elif(eName == "ORDER_NUMBER"):
                if(self.__isCatalogEntry == True):
                    self.__isOrderNumber = True

            elif(eName == "ENTRY_NAME"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryName = True

            elif(eName == "ENTRY_WIDTH_IN_MODULES"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryWidthModul = True

            elif(eName == "ENTRY_WIDTH_IN_MILLIMETERS"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryWidthMM = True

            elif(eName == "DIN_FLAG"):
                if(self.__isCatalogEntry == True):
                    self.__isDIN_Flag = True

            elif(eName == "PAGE_NUMBER"):
                if(self.__isCatalogEntry == True):
                    self.__isPageNumber = True

            elif(eName == "DESIGNATION_TYPE"):
                if(self.__isCatalogEntry == True):
                    self.__isDesignationType = True

            elif(eName == "ENTRY_STATUS_CODE"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryStatusCode = True

            elif(eName == "REGISTRATION_TS"):
                if(self.__isCatalogEntry == True):
                    self.__isRegistrationTS = True


        except SAXException:
            print "Error again"

    def endElement(self,eName):
        #print eName
        if(eName == "catalog_entry"):
            self.__isCatalogEntry=False

            self.__CatalogEntry.append(self.__Catalog)
            del self.__Catalog
            self.__Catalog = FB_CatalogEntry.FB_CatalogEntry()

        elif(eName == "CATALOG_ENTRY_ID"):
            if(self.__isCatalogEntry == True):
                self.__isCatalogEntry_ID = False

        elif(eName == "PRODUCT_ID"):
            if(self.__isCatalogEntry == True):
                self.__isProduct_ID = False

        elif(eName == "MANUFACTURER_ID"):
            if(self.__isCatalogEntry == True):
                self.__isManufacturerID = False

        elif(eName == "ORDER_NUMBER"):
            if(self.__isCatalogEntry == True):
                self.__isOrderNumber = False

        elif(eName == "ENTRY_NAME"):
            if(self.__isCatalogEntry == True):
                self.__isEntryName = False

        elif(eName == "ENTRY_WIDTH_IN_MODULES"):
            if(self.__isCatalogEntry == True):
                self.__isEntryWidthModul = False

        elif(eName == "ENTRY_WIDTH_IN_MILLIMETERS"):
            if(self.__isCatalogEntry == True):
                self.__isEntryWidthMM = False

        elif(eName == "DIN_FLAG"):
            if(self.__isCatalogEntry == True):
                self.__isDIN_Flag = False

        elif(eName == "PAGE_NUMBER"):
            if(self.__isCatalogEntry == True):
                self.__isPageNumber = False

        elif(eName == "DESIGNATION_TYPE"):
            if(self.__isCatalogEntry == True):
                self.__isDesignationType = False

        elif(eName == "ENTRY_STATUS_CODE"):
            if(self.__isCatalogEntry == True):
                self.__isEntryStatusCode = False

        elif(eName == "REGISTRATION_TS"):
            if(self.__isCatalogEntry == True):
                self.__isRegistrationTS = False


    def characters(self ,char):
        strValue = char.encode( "iso-8859-1" )

        if(self.__isCatalogEntry_ID == True):
            #self.__Index = 1
            self.__Catalog.setCatalogEntryID(self.IsNumber(strValue))
        elif(self.__isProduct_ID == True):
            #self.__Index = 2
            self.__Catalog.setProductID(self.IsNumber(strValue))
        elif(self.__isManufacturerID  == True):
            #self.__Index = 3
            self.__Catalog.setManufacturerID(self.IsNumber(strValue))
        elif(self.__isOrderNumber == True):
            #self.__Index = 4
            self.__Catalog.setOrderNumber(self.IsString(strValue))
        elif(self.__isEntryName == True):
            #self.__Index = 5
            self.__Catalog.setEntryName(self.IsString(strValue))
        elif(self.__isEntryWidthModul == True):
            #self.__Index = 6
            self.__Catalog.setEntryWidthModul(self.IsNumber(strValue))
        elif(self.__isEntryWidthMM == True):
            #self.__Index = 7
            self.__Catalog.setEntryWidthMM(self.IsNumber(strValue))
        elif(self.__isDIN_Flag == True):
            #self.__Index = 8
            self.__Catalog.setDINFlag(self.IsNumber(strValue))
        elif(self.__isPageNumber == True):
            #self.__Index = 9
            self.__Catalog.setPageNumber(self.IsString(strValue))
        elif(self.__isDesignationType == True):
            #self.__Index = 10
            self.__Catalog.setDesignationType(self.IsNumber(strValue))
        elif(self.__isEntryStatusCode == True):
            #self.__Index = 11
            self.__Catalog.setEntryStatusCode(self.IsNumber(strValue))
        elif(self.__isRegistrationTS == True):
            #self.__Index = 12
            self.__Catalog.setRegistrationTS(self.IsNumber(strValue))


    def IsNumber(self,strValue):

        if(strValue.isdigit() == True):
            return strValue
        else:
            return "0"

    #check for String in parsed value
    def IsString(self,strValue):

        Value = strValue.replace('\\r\\n',' ')
        Value = Value.replace('\\rn', ' ')
        Value = Value.replace("'", ' ')
        return Value
