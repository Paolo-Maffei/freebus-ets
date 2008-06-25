#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_CatalogEntry.py
#Version: V0.1 , 23.06.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_CatalogEntry:

    __CatalogEntry_ID = 0    #CATALOG_ENTRY_ID
    __Product_ID = 0         #PRODUCT_ID
    __ManufacturerID = 0     #MANUFACTURER_ID
    __OrderNumber = ""       #ORDER_NUMBER
    __EntryName = ""         #ENTRY_NAME
    __EntryWidthModul = 0    #ENTRY_WIDTH_IN_MODULES
    __EntryWidthMM = 0       #ENTRY_WIDTH_IN_MILLIMETERS
    __DIN_Flag = 0           #DIN_FLAG
    __PageNumber = 0         #PAGE_NUMBER
    __DesignationType = ""   #DESIGNATION_TYPE
    __EntryStatusCode = 0    #ENTRY_STATUS_CODE
    __RegistrationTS = 0     #REGISTRATION_TS


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__CatalogEntry_ID,self.__Product_ID,self.__Manufacturer_ID,self.__OrderNumber,
                self.__EntryName,self.__EntryWidthModul,self.__EntryWidthMM,self.__DIN_Flag,
                self.__PageNumber,self.__DesignationType,self.__EntryStatusCode,self.__RegistrationTS)

        return List

    #general set and get property with index for each element, coresponds to FB_Constants
    def setCatalogEntry(self,Index, Value):
        if(Index == 1):
            self.__CatalogEntry_ID = Value
        elif(Index == 2):
            self.__Product_ID = Value
        elif(Index == 3):
            self.__Manufacturer_ID = Value
        elif(Index == 4):
            self.__OrderNumber = Value
        elif(Index == 5):
            self.__EntryName = Value
        elif(Index == 6):
            self.__EntryWidthModul = Value
        elif(Index == 7):
            self.__EntryWidthMM = Value
        elif(Index == 8):
            self.__DIN_Flag = Value
        elif(Index == 9):
            self.__PageNumber = Value
        elif(Index == 10):
            self.__DesignationType = Value
        elif(Index == 11):
            self.__EntryStatusCode = Value
        elif(Index == 12):
            self.__RegistrationTS = Value


    def getCatalogEntry(self,Index):
         if(Index == 1):
            return self.__CatalogEntry_ID
         elif(Index == 2):
            return self.__Product_ID
         elif(Index == 3):
            return self.__Manufacturer_ID
         elif(Index == 4):
            return self.__OrderNumber
         elif(Index == 5):
            return self.__EntryName
         elif(Index == 6):
            return self.__EntryWidthModul
         elif(Index == 7):
            return self.__EntryWidthMM
         elif(Index == 8):
            return self.__DIN_Flag
         elif(Index == 9):
            return self.__PageNumber
         elif(Index == 10):
            return self.__DesignationType
         elif(Index == 11):
            return self.__EntryStatusCode
         elif(Index == 12):
            return self.__RegistrationTS


#**********************************************************************
    #CATALOG_ENTRY_ID
    def setCatalogEntryID(self,C_ID):
        self.__CatalogEntry_ID = C_ID

    def getCatalogEntryID(self):
        return self.__CatalogEntry_ID
#**********************************************************************
    #PRODUCT_ID
    def setProductID(self,P_ID):
        self.__Product_ID = P_ID

    def getProductID(self):
        return self.__Product_ID

#**********************************************************************
    #MANUFACTURER_ID
    def setManufacturerID(self,M_ID):
        self.__Manufacturer_ID = M_ID

    def getManufacturerID(self):
        return self.__Manufacturer_ID

#**********************************************************************
    #ORDER_NUMBER
    def setOrderNumber(self,OrderNo):
        self.__OrderNumber = OrderNo

    def getOrderNumber(self):
        return self.__OrderNumber

#**********************************************************************

    #ENTRY_NAME
    def setEntryName(self,E_Name):
        self.__EntryName = E_Name

    def getEntryName(self):
        return self.__EntryName

#**********************************************************************

    #ENTRY_WIDTH_IN_MODULES
    def setEntryWidthModul(self,WidthModul):
        self.__EntryWidthModul = WidthModul

    def getEntryWidthModul(self):
        return self.__EntryWidthModul

#**********************************************************************
    #ENTRY_WIDTH_IN_MILLIMETERS
    def setEntryWidthMM(self,WidthMM):
        self.__EntryWidthMM = WidthMM

    def getEntryWidthMM(self):
        return self.__EntryWidthMM

#**********************************************************************
    #DIN_FLAG
    def setDINFlag(self,DIN_Flag):
        self.__DIN_Flag = DIN_Flag

    def getDINFlag(self):
        return self.__DIN_Flag

#**********************************************************************
    #PAGE_NUMBER
    def setPageNumber(self,Page_Number):
        self.__PageNumber = Page_Number

    def getPageNumber(self):
        return self.__PageNumber

#**********************************************************************
   #DESIGNATION_TYPE
    def setDesignationType(self,D_Type):
        self.__DesignationType  = D_Type

    def getDesignationType(self):
        return self.__DesignationType

#**********************************************************************
   #ENTRY_STATUS_CODE
    def setEntryStatusCode(self,E_Status):
        self.__EntryStatusCode = E_Status

    def getEntryStatusCode(self):
        return self.__EntryStatusCode

#**********************************************************************
    #REGISTRATION_TS
    def setRegistrationTS(self,RegTS):
        self.__RegistrationTS = RegTS

    def getRegistrationTS(self):
        return self.__RegistrationTS

