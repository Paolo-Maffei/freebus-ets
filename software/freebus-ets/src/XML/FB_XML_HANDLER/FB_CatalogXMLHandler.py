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
#Version: V0.4 , 20.07.2008
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
    __isSymbol_ID = False          #SYMBOL_ID                        NEU
    __isOrderNumber = False        #ORDER_NUMBER
    __isEntryName = False          #ENTRY_NAME
    __isEntryColour = False        #ENTRY_COLOUR                     NEU
    __isEntryWidthModul = False    #ENTRY_WIDTH_IN_MODULES
    __isEntryWidthMM = False       #ENTRY_WIDTH_IN_MILLIMETERS
    __isPrice = False              #PRICE                            NEU
    __isCurrency = False           #CURRENCY                         NEU
    __isQuantityUnit = False       #QUANTITY_UNIT                    NEU
    __isMaterialPrice = False      #MATERIAL_PRICE                   NEU
    __isMountingHours = False      #MOUNTING_HOURS                   NEU
    __isMountingMinutes = False    #MOUNTING_MINUTES                 NEU
    __isMountingSeconds = False    #MOUNTING_SECONDS                 NEU
    __isDIN_Flag = False           #DIN_FLAG
    __isSeries = False             #SERIES                           NEU
    __isCatalogName = False        #CATALOG_NAME                     NEU
    __isPageNumber = False         #PAGE_NUMBER
    __isEntryPictrue = False       #ENTRY_PICTURE                    NEU
    __isDesignationType = False    #DESIGNATION_TYPE
    __isDesignationFunction = False #DESIGNATION_FUNCTION            NEU
    __isHelpFileName = False       #HELP_FILE_NAME                   NEU
    __isContextID = False          #CONTEXT_ID                       NEU
    __isRAMSize = False            #RAM_SIZE                         NEU
    __isRegistrationNo = False     #REGISTRATION_NUMBER              NEU
    __isRegistrationYear = False   #REGISTRATION_YEAR                NEU
    __isEntryStatusCode = False    #ENTRY_STATUS_CODE
    __isRegistrationTS = False     #REGISTRATION_TS
    __isRegistrationDate = False   #REGISTRATION_DATE                NEU
    __isRegistrationComment = False #REGISTRATION_COMMENT            NEU




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

            elif(eName == "SYMBOL_ID"):
                if(self.__isCatalogEntry == True):
                    self.__isSymbol_ID = True

            elif(eName == "ORDER_NUMBER"):
                if(self.__isCatalogEntry == True):
                    self.__isOrderNumber = True

            elif(eName == "ENTRY_NAME"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryName = True

            elif(eName == "ENTRY_COLOUR"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryColour = True

            elif(eName == "ENTRY_WIDTH_IN_MODULES"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryWidthModul = True

            elif(eName == "ENTRY_WIDTH_IN_MILLIMETERS"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryWidthMM = True

            elif(eName == "PRICE"):
                if(self.__isCatalogEntry == True):
                    self.__isPrice = True

            elif(eName == "CURRENCY"):
                if(self.__isCatalogEntry == True):
                    self.__isCurrency = True

            elif(eName == "QUANTITY_UNIT"):
                if(self.__isCatalogEntry == True):
                    self.__isQuantityUnit = True

            elif(eName == "MATERIAL_PRICE"):
                if(self.__isCatalogEntry == True):
                    self.__isMaterialPrice = True

            elif(eName == "MOUNTING_HOURS"):
                if(self.__isCatalogEntry == True):
                    self.__isMountingHours = True

            elif(eName == "MOUNTING_MINUTES"):
                if(self.__isCatalogEntry == True):
                    self.__isMountingMinutes = True

            elif(eName == "MOUNTING_SECONDS"):
                if(self.__isCatalogEntry == True):
                    self.__isMountingSeconds = True

            elif(eName == "DIN_FLAG"):
                if(self.__isCatalogEntry == True):
                    self.__isDIN_Flag = True

            elif(eName == "SERIES"):
                if(self.__isCatalogEntry == True):
                    self.__isSeries = True

            elif(eName == "CATALOG_NAME"):
                if(self.__isCatalogEntry == True):
                    self.__isCatalogName = True

            elif(eName == "PAGE_NUMBER"):
                if(self.__isCatalogEntry == True):
                    self.__isPageNumber = True

            elif(eName == "ENTRY_PICTURE"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryPictrue = True

            elif(eName == "DESIGNATION_TYPE"):
                if(self.__isCatalogEntry == True):
                    self.__isDesignationType = True

            elif(eName == "DESIGNATION_FUNCTION"):
                if(self.__isCatalogEntry == True):
                    self.__isDesignationFunction = True

            elif(eName == "HELP_FILE_NAME"):
                if(self.__isCatalogEntry == True):
                    self.__isHelpFileName = True

            elif(eName == "CONTEXT_ID"):
                if(self.__isCatalogEntry == True):
                    self.__isContextID = True

            elif(eName == "RAM_SIZE"):
                if(self.__isCatalogEntry == True):
                    self.__isRAMSize = True

            elif(eName == "REGISTRATION_NUMBER"):
                if(self.__isCatalogEntry == True):
                    self.__isRegistrationNo = True

            elif(eName == "REGISTRATION_YEAR"):
                if(self.__isCatalogEntry == True):
                    self.__isRegistrationYear = True

            elif(eName == "ENTRY_STATUS_CODE"):
                if(self.__isCatalogEntry == True):
                    self.__isEntryStatusCode = True

            elif(eName == "REGISTRATION_TS"):
                if(self.__isCatalogEntry == True):
                    self.__isRegistrationTS = True

            elif(eName == "REGISTRATION_DATE"):
                if(self.__isCatalogEntry == True):
                    self.__isRegistrationDate = True

            elif(eName == "REGISTRATION_COMMENT"):
                if(self.__isCatalogEntry == True):
                    self.__isRegistrationComment = True


        except SAXException:
            print "Error again"

    def endElement(self,eName):
        #print eName
        if(eName == "catalog_entry"):
            self.__isCatalogEntry = False

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

        elif(eName == "SYMBOL_ID"):
            if(self.__isCatalogEntry == True):
                self.__isSymbol_ID = False

        elif(eName == "ORDER_NUMBER"):
            if(self.__isCatalogEntry == True):
                self.__isOrderNumber = False

        elif(eName == "ENTRY_NAME"):
            if(self.__isCatalogEntry == True):
                self.__isEntryName = False

        elif(eName == "ENTRY_COLOUR"):
            if(self.__isCatalogEntry == True):
                self.__isEntryColour = False

        elif(eName == "ENTRY_WIDTH_IN_MODULES"):
            if(self.__isCatalogEntry == True):
                self.__isEntryWidthModul = False

        elif(eName == "ENTRY_WIDTH_IN_MILLIMETERS"):
            if(self.__isCatalogEntry == True):
                self.__isEntryWidthMM = False

        elif(eName == "PRICE"):
            if(self.__isCatalogEntry == True):
                self.__isPrice = False

        elif(eName == "CURRENCY"):
            if(self.__isCatalogEntry == True):
                self.__isCurrency = False

        elif(eName == "QUANTITY_UNIT"):
            if(self.__isCatalogEntry == True):
                    self.__isQuantityUnit = False

        elif(eName == "MATERIAL_PRICE"):
            if(self.__isCatalogEntry == True):
                self.__isMaterialPrice = False

        elif(eName == "MOUNTING_HOURS"):
            if(self.__isCatalogEntry == True):
                self.__isMountingHours = False

        elif(eName == "MOUNTING_MINUTES"):
            if(self.__isCatalogEntry == True):
                self.__isMountingMinutes = False

        elif(eName == "MOUNTING_SECONDS"):
            if(self.__isCatalogEntry == True):
                self.__isMountingSeconds = False

        elif(eName == "DIN_FLAG"):
            if(self.__isCatalogEntry == True):
                self.__isDIN_Flag = False

        elif(eName == "SERIES"):
            if(self.__isCatalogEntry == True):
                self.__isSeries = False

        elif(eName == "CATALOG_NAME"):
            if(self.__isCatalogEntry == True):
                self.__isCatalogName = False

        elif(eName == "PAGE_NUMBER"):
            if(self.__isCatalogEntry == True):
                self.__isPageNumber = False

        elif(eName == "ENTRY_PICTURE"):
            if(self.__isCatalogEntry == True):
                self.__isEntryPictrue = False

        elif(eName == "DESIGNATION_TYPE"):
            if(self.__isCatalogEntry == True):
                self.__isDesignationType = False

        elif(eName == "DESIGNATION_FUNCTION"):
            if(self.__isCatalogEntry == True):
                self.__isDesignationFunction = False

        elif(eName == "HELP_FILE_NAME"):
            if(self.__isCatalogEntry == True):
                self.__isHelpFileName = False

        elif(eName == "CONTEXT_ID"):
            if(self.__isCatalogEntry == True):
                self.__isContextID = False

        elif(eName == "RAM_SIZE"):
            if(self.__isCatalogEntry == True):
                self.__isRAMSize = False

        elif(eName == "REGISTRATION_NUMBER"):
            if(self.__isCatalogEntry == True):
                self.__isRegistrationNo = False

        elif(eName == "REGISTRATION_YEAR"):
            if(self.__isCatalogEntry == True):
                self.__isRegistrationYear = False

        elif(eName == "ENTRY_STATUS_CODE"):
            if(self.__isCatalogEntry == True):
                self.__isEntryStatusCode = False

        elif(eName == "REGISTRATION_TS"):
            if(self.__isCatalogEntry == True):
                self.__isRegistrationTS = False

        elif(eName == "REGISTRATION_DATE"):
            if(self.__isCatalogEntry == True):
                self.__isRegistrationDate = False

        elif(eName == "REGISTRATION_COMMENT"):
            if(self.__isCatalogEntry == True):
                self.__isRegistrationComment = False


    def characters(self ,char):
        strValue = char.encode( "iso-8859-1" )

        if(self.__isCatalogEntry_ID == True):
            self.__Catalog.setCatalogEntryID(self.IsNumber(strValue))

        elif(self.__isProduct_ID == True):
            self.__Catalog.setProductID(self.IsNumber(strValue))

        elif(self.__isManufacturerID  == True):
            self.__Catalog.setManufacturerID(self.IsNumber(strValue))

        elif(self.__isSymbol_ID  == True):
            self.__Catalog.setSymbolID(self.IsNumber(strValue))

        elif(self.__isOrderNumber == True):
            self.__Catalog.setOrderNumber(self.IsString(strValue))

        elif(self.__isEntryName == True):
            self.__Catalog.setEntryName(self.IsString(strValue))

        elif(self.__isEntryColour == True):
            self.__Catalog.setEntryColour(self.IsString(strValue))

        elif(self.__isEntryWidthModul == True):
            self.__Catalog.setEntryWidthModul(self.IsNumber(strValue))

        elif(self.__isEntryWidthMM == True):
           self.__Catalog.setEntryWidthMM(self.IsNumber(strValue))

        elif(self.__isPrice == True):
           self.__Catalog.setPrice(self.IsNumber(strValue))

        elif(self.__isCurrency == True):
           self.__Catalog.setCurrency(self.IsString(strValue))

        elif(self.__isQuantityUnit == True):
           self.__Catalog.setQuantityUnit(self.IsNumber(strValue))

        elif(self.__isMaterialPrice == True):
           self.__Catalog.setMaterialPrice(self.IsNumber(strValue))

        elif(self.__isMountingHours == True):
           self.__Catalog.setMountingHours(self.IsNumber(strValue))

        elif(self.__isMountingMinutes == True):
           self.__Catalog.setMountingMinutes(self.IsNumber(strValue))

        elif(self.__isMountingSeconds == True):
           self.__Catalog.setMountingSeconds(self.IsNumber(strValue))

        elif(self.__isDIN_Flag == True):
            self.__Catalog.setDINFlag(self.IsNumber(strValue))

        elif(self.__isSeries == True):
            self.__Catalog.setSeries(self.IsString(strValue))

        elif(self.__isCatalogName == True):
            self.__Catalog.setCatalogName(self.IsString(strValue))

        elif(self.__isPageNumber == True):
           self.__Catalog.setPageNumber(self.IsNumber(strValue))

        elif(self.__isEntryPictrue == True):
           self.__Catalog.setEntryPicture(self.IsString(strValue))

        elif(self.__isDesignationType == True):
            self.__Catalog.setDesignationType(self.IsString(strValue))

        elif(self.__isDesignationFunction == True):
            self.__Catalog.setDesignationFunction(self.IsString(strValue))

        elif(self.__isHelpFileName == True):
            self.__Catalog.setHelpFileName(self.IsString(strValue))

        elif(self.__isContextID == True):
            self.__Catalog.setContextID(self.IsNumber(strValue))

        elif(self.__isRAMSize == True):
            self.__Catalog.setRamSize(self.IsNumber(strValue))

        elif(self.__isRegistrationNo == True):
            self.__Catalog.setRegistrationNumber(self.IsNumber(strValue))

        elif(self.__isRegistrationYear == True):
            self.__Catalog.setRegistrationYear(self.IsNumber(strValue))

        elif(self.__isEntryStatusCode == True):
            self.__Catalog.setEntryStatusCode(self.IsNumber(strValue))

        elif(self.__isRegistrationTS == True):
            self.__Catalog.setRegistrationTS(self.IsNumber(strValue))

        elif(self.__isRegistrationDate == True):
            self.__Catalog.setRegistrationDate(self.IsString(strValue))

        elif(self.__isRegistrationComment == True):
            self.__Catalog.setRegistrationComment(self.IsString(strValue))



    def IsNumber(self,strValue):

        if(strValue.isdigit() == True):
            return strValue
        else:
            return "0"

    #check for String in parsed value
    def IsString(self,strValue):

        Value = strValue.replace('\\r\\n',' ')
        Value = Value.replace('\\r',' ')
        Value = Value.replace('\\n',' ')
        Value = Value.replace('\\rn', ' ')
        Value = Value.replace("'", ' ')
        return Value
