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
#Version: V0.2 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_CatalogEntry:

    __CatalogEntry_ID = None         #CATALOG_ENTRY_ID
    __Product_ID = None              #PRODUCT_ID
    __ManufacturerID = None          #MANUFACTURER_ID
    __Symbol_ID = None               #SYMBOL_ID                        NEU
    __OrderNumber = None             #ORDER_NUMBER
    __EntryName = None               #ENTRY_NAME
    __EntryColour = None             #ENTRY_COLOUR                     NEU
    __EntryWidthModul = None         #ENTRY_WIDTH_IN_MODULES
    __EntryWidthMM = None            #ENTRY_WIDTH_IN_MILLIMETERS
    __Price = None                   #PRICE                            NEU
    __Currency = None                #CURRENCY                         NEU
    __QuantityUnit = None            #QUANTITY_UNIT                    NEU
    __MaterialPrice = None           #MATERIAL_PRICE                   NEU
    __MountingHours = None           #MOUNTING_HOURS                   NEU
    __MountingMinutes = None         #MOUNTING_MINUTES                 NEU
    __MountingSeconds = None         #MOUNTING_SECONDS                 NEU
    __DIN_Flag = None                #DIN_FLAG
    __Series = None                  #SERIES                           NEU
    __CatalogName = None             #CATALOG_NAME                     NEU
    __PageNumber = None              #PAGE_NUMBER
    __EntryPictrue = None            #ENTRY_PICTURE                    NEU
    __DesignationType = None         #DESIGNATION_TYPE
    __DesignationFunction = None     #DESIGNATION_FUNCTION           NEU
    __HelpFileName = None            #HELP_FILE_NAME                   NEU
    __ContextID = None               #CONTEXT_ID                       NEU
    __RAMSize = None                 #RAM_SIZE                         NEU
    __RegistrationNo = None          #REGISTRATION_NUMBER              NEU
    __RegistrationYear = None        #REGISTRATION_YEAR                NEU
    __EntryStatusCode = None         #ENTRY_STATUS_CODE
    __RegistrationTS = None          #REGISTRATION_TS
    __RegistrationDate = None        #REGISTRATION_DATE                NEU
    __RegistrationComment = None     #REGISTRATION_COMMENT           NEU


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__CatalogEntry_ID,self.__Product_ID,self.__Manufacturer_ID,self.__Symbol_ID, self.__OrderNumber,
                self.__EntryName,self.__EntryColour, self.__EntryWidthModul,self.__EntryWidthMM,self.__Price,
                self.__Currency, self.__QuantityUnit,self.__MaterialPrice, self.__MountingHours, self.__MountingMinutes,
                self.__MountingSeconds,self.__DIN_Flag, self.__Series, self.__CatalogName, self.__PageNumber,
                self.__EntryPictrue,self.__DesignationType, self.__DesignationFunction, self.__HelpFileName, self.__ContextID,
                self.__RAMSize, self.__RegistrationNo, self.__RegistrationYear, self.__EntryStatusCode,self.__RegistrationTS,
                self.__RegistrationDate, self.__RegistrationComment)

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
            self.__Symbol_ID = Value
        elif(Index == 5):
            self.__OrderNumber = Value
        elif(Index == 6):
            self.__EntryName = Value
        elif(Index == 7):
            self.__EntryColour = Value
        elif(Index == 8):
            self.__EntryWidthModul = Value
        elif(Index == 9):
            self.__EntryWidthMM = Value
        elif(Index == 10):
            self.__Price = Value
        elif(Index == 11):
            self.__Currency = Value
        elif(Index == 12):
            self.__QuantityUnit = Value
        elif(Index == 13):
            self.__MaterialPrice = Value
        elif(Index == 14):
            self.__MountingHours = Value
        elif(Index == 15):
            self.__MountingMinutes = Value
        elif(Index == 16):
            self.__MountingSeconds = Value
        elif(Index == 17):
            self.__DIN_Flag = Value
        elif(Index == 18):
            self.__Series = Value
        elif(Index == 19):
            self.__CatalogName = Value
        elif(Index == 20):
            self.__PageNumber = Value
        elif(Index == 21):
            self.__EntryPictrue = Value
        elif(Index == 22):
            self.__DesignationType = Value
        elif(Index == 23):
            self.__DesignationFunction = Value
        elif(Index == 24):
            self.__HelpFileName = Value
        elif(Index == 25):
            self.__ContextID = Value
        elif(Index == 26):
            self.__RAMSize = Value
        elif(Index == 27):
            self.__RegistrationNo = Value
        elif(Index == 28):
            self.__RegistrationYear = Value
        elif(Index == 29):
            self.__EntryStatusCode = Value
        elif(Index == 30):
            self.__RegistrationTS = Value
        elif(Index == 31):
            self.__RegistrationDate = Value
        elif(Index == 32):
            self.__RegistrationComment = Value

    def getCatalogEntry(self,Index):
        if(Index == 1):
            return self.__CatalogEntry_ID
        elif(Index == 2):
            return self.__Product_ID
        elif(Index == 3):
            return self.__Manufacturer_ID
        elif(Index == 4):
            return self.__Symbol_ID
        elif(Index == 5):
            return self.__OrderNumber
        elif(Index == 6):
            return self.__EntryName
        elif(Index == 7):
            return self.__EntryColour
        elif(Index == 8):
            return self.__EntryWidthModul
        elif(Index == 9):
            return self.__EntryWidthMM
        elif(Index == 10):
            return self.__Price
        elif(Index == 11):
            return self.__Currency
        elif(Index == 12):
            return self.__QuantityUnit
        elif(Index == 13):
            return self.__MaterialPrice
        elif(Index == 14):
            return self.__MountingHours
        elif(Index == 15):
            return self.__MountingMinutes
        elif(Index == 16):
            return self.__MountingSeconds
        elif(Index == 17):
            return self.__DIN_Flag
        elif(Index == 18):
            return self.__Series
        elif(Index == 19):
            return self.__CatalogName
        elif(Index == 20):
            return self.__PageNumber
        elif(Index == 21):
            return self.__EntryPictrue
        elif(Index == 22):
            return self.__DesignationType
        elif(Index == 23):
            return self.__DesignationFunction
        elif(Index == 24):
            return self.__HelpFileName
        elif(Index == 25):
            return self.__ContextID
        elif(Index == 26):
            return self.__RAMSize
        elif(Index == 27):
            return self.__RegistrationNo
        elif(Index == 28):
            return self.__RegistrationYear
        elif(Index == 29):
            return self.__EntryStatusCode
        elif(Index == 30):
            return self.__RegistrationTS
        elif(Index == 31):
            return self.__RegistrationDate
        elif(Index == 32):
            return self.__RegistrationComment

#**********************************************************************
    #CATALOG_ENTRY_ID
    def setCatalogEntryID(self,C_ID):
        self.__CatalogEntry_ID = C_ID

    def getCatalogEntryID(self):
        return self.__CatalogEntry_ID
#*********************************************************************
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
    #SYMBOL_ID
    def setSymbolID(self,S_ID):
        self.__Symbol_ID = S_ID

    def getSymbolID(self):
        return self.__Symbol_ID

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
    #ENTRY_COLOUR
    def setEntryColour(self,E_Colour):
        self.__EntryColour = E_Colour

    def getEntryColour(self):
        return self.__EntryColour
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
    #PRICE
    def setPrice(self,Price):
        self.__Price = Price

    def getPrice(self):
        return self.__Price
#**********************************************************************
    #CURRENCY
    def setCurrency(self,Currency):
        self.__Currency = Currency

    def getCurrency(self):
        return self.__Currency
#**********************************************************************
    #QUANTITY_UNIT
    def setQuantityUnit(self,QuantityUnit):
        self.__QuantityUnit = QuantityUnit

    def getQuantityUnit(self):
        return self.__QuantityUnit
#**********************************************************************
    #MATERIAL_PRICE
    def setMaterialPrice(self,M_Price):
        self.__MaterialPrice = M_Price

    def getMaterialPrice(self):
        return self.__MaterialPrice
#**********************************************************************
    #MOUNTING_HOURS
    def setMountingHours(self,M_Hours):
        self.__MountingHours = M_Hours

    def getMountingHours(self):
        return self.__MountingHours
#**********************************************************************
    #MOUNTING_MINUTES
    def setMountingMinutes(self,M_Minutes):
        self.__MountingMinutes = M_Minutes

    def getMountingMinutes(self):
        return self.__MountingMinutes
#**********************************************************************
    #MOUNTING_SECONDS
    def setMountingSeconds(self,M_Seconds):
        self.__MountingSeconds = M_Seconds

    def getMountingSeconds(self):
        return self.__MountingSeconds
#**********************************************************************
    #DIN_FLAG
    def setDINFlag(self,DIN_Flag):
        self.__DIN_Flag = DIN_Flag

    def getDINFlag(self):
        return self.__DIN_Flag
#**********************************************************************
    #SERIES
    def setSeries(self,Series):
        self.__Series = Series

    def getSeries(self):
        return self.__Series
#**********************************************************************
    #CATALOG_NAME
    def setCatalogName(self,CatalogName):
        self.__CatalogName = CatalogName

    def getCatalogName(self):
        return self.__CatalogName
#**********************************************************************
    #PAGE_NUMBER
    def setPageNumber(self,Page_Number):
        self.__PageNumber = Page_Number

    def getPageNumber(self):
        return self.__PageNumber
#**********************************************************************
    #ENTRY_PICTURE
    def setEntryPicture(self,EntryPic):
        self.__EntryPictrue = EntryPic

    def getEntryPicture(self):
        return self.__EntryPictrue
#**********************************************************************
   #DESIGNATION_TYPE
    def setDesignationType(self,D_Type):
        self.__DesignationType  = D_Type

    def getDesignationType(self):
        return self.__DesignationType
#**********************************************************************
   #DESIGNATION_FUNCTION
    def setDesignationFunction(self,D_Function):
        self.__DesignationFunction  = D_Function

    def getDesignationFunction(self):
        return self.__DesignationFunction
#**********************************************************************
   #HELP_FILE_NAME
    def setHelpFileName(self,HelpFile):
        self.__HelpFileName  = HelpFile

    def getHelpFileName(self):
        return self.__HelpFileName
#**********************************************************************
   #CONTEXT_ID
    def setContextID(self,ContextID):
        self.__ContextID  = ContextID

    def getContextID(self):
        return self.__ContextID
#**********************************************************************
   #RAM_SIZE
    def setRamSize(self,RamSize):
        self.__RAMSize  = RamSize

    def getRamSize(self):
        return self.__RAMSize
#**********************************************************************
   #REGISTRATION_NUMBER
    def setRegistrationNumber(self,RegNo):
        self.__RegistrationNo  = RegNo

    def getRegistrationNumber(self):
        return self.__RegistrationNo
#**********************************************************************
   #REGISTRATION_YEAR
    def setRegistrationYear(self,RegYear):
        self.__RegistrationYear  = RegYear

    def getRegistrationYear(self):
        return self.__RegistrationYear

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
#**********************************************************************
    #REGISTRATION_DATE
    def setRegistrationDate(self,RegDate):
        self.__RegistrationDate = RegDate

    def getRegistrationDate(self):
        return self.__RegistrationDate
#**********************************************************************
    #REGISTRATION_COMMENT
    def setRegistrationComment(self,RegComment):
        self.__RegistrationComment = RegComment

    def getRegistrationComment(self):
        return self.__RegistrationComment

