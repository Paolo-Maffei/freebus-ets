#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ProductXMLHandler.py
#Version: V0.1 , 25.12.2007
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 15.06.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================


from FB_DATA import FB_Products

##General XML-Handler Class, parse entire XML-Data File and fill alle Data-Structures
##Products, Applications, Communications-objects
class FB_ProductXMLHandler():

    __LogObj = None
    __products = []
    __prod = None        #prviate object for product-Data
    __Index = 0

    __isHWProduct = False
    __isProductID = False
    __isManufacturerID = False
    __isSymbolID = False
    __isProductName = False
    __isProductVersion = False
    __isCompType = False
    __isCompAttr = False
    __isBusCurrent = False
    __isProductSN = False
    __isCompTypeNo = False
    __isProductPic = False
    __isBCUType = False
    __isProductHandling = False
    __isProductDLL = False
    __isOrigManID = False



    def __init__(self, LogObj):
        self.__LogObj = LogObj
        self.__prod = FB_Products.FB_Products()    #FB_ProductXMLHandler
        self.__products = []                #init List


    #return List of Instances of type FB_Products
    def getProductList(self):
        return self.__products


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

            if(eName == "hw_product"):
                self.__isHWProduct = True

            elif(eName == "PRODUCT_ID"):
                if(self.__isHWProduct == True):
                    self.__isProductID = True

            elif(eName == "MANUFACTURER_ID"):
                if(self.__isHWProduct == True):
                    self.__isManufacturerID = True

            elif(eName == "SYMBOL_ID"):
                if(self.__isHWProduct == True):
                    self.__isSymbolID = True

            elif(eName == "PRODUCT_NAME"):
                if(self.__isHWProduct == True):
                    self.__isProductName = True

            elif(eName == "PRODUCT_VERSION_NUMBER"):
                if(self.__isHWProduct == True):
                    self.__isProductVersion = True

            elif(eName == "COMPONENT_TYPE"):
                if(self.__isHWProduct == True):
                    self.__isCompType = True

            elif(eName == "COMPONENT_ATTRIBUTES"):
                if(self.__isHWProduct == True):
                    self.__isCompAttr = True

            elif(eName == "BUS_CURRENT"):
                if(self.__isHWProduct == True):
                    self.__isBusCurrent = True

            elif(eName == "PRODUCT_SERIAL_NUMBER"):
                if(self.__isHWProduct == True):
                    self.__isProductSN = True

            elif(eName == "COMPONENT_TYPE_NUMBER"):
                if(self.__isHWProduct == True):
                    self.__isCompTypeNo = True

            elif(eName == "PRODUCT_PICTURE"):
                if(self.__isHWProduct == True):
                    self.__isProductPic = True

            elif(eName == "BCU_TYPE_NUMBER"):
                if(self.__isHWProduct == True):
                    self.__isBCUType = True

            elif(eName == "PRODUCT_HANDLING"):
                if(self.__isHWProduct == True):
                    self.__isProductHandling = True

            elif(eName == "PRODUCT_DLL"):
                if(self.__isHWProduct == True):
                    self.__isProductDLL = True

            elif(eName == "ORIGINAL_MANUFACTURER_ID"):
                if(self.__isHWProduct == True):
                    self.__isOrigManID = True


        except SAXException:
            print "Error again"

    def endElement(self,eName):
        #print eName
        if(eName == "hw_product"):
            self.__isHWProduct=False

            self.__products.append(self.__prod)
            del self.__prod
            self.__prod = FB_Products.FB_Products()

        elif(eName == "PRODUCT_ID"):
            if(self.__isHWProduct == True):
                self.__isProductID = False

        elif(eName == "MANUFACTURER_ID"):
            if(self.__isHWProduct == True):
                self.__isManufacturerID = False

        elif(eName == "SYMBOL_ID"):
            if(self.__isHWProduct == True):
                self.__isSymbolID = False

        elif(eName == "PRODUCT_NAME"):
            if(self.__isHWProduct == True):
                self.__isProductName = False

        elif(eName == "PRODUCT_VERSION_NUMBER"):
            if(self.__isHWProduct == True):
                self.__isProductVersion = False

        elif(eName == "COMPONENT_TYPE"):
            if(self.__isHWProduct == True):
                self.__isCompType = False

        elif(eName == "COMPONENT_ATTRIBUTES"):
            if(self.__isHWProduct == True):
                self.__isCompAttr = False

        elif(eName == "BUS_CURRENT"):
            if(self.__isHWProduct == True):
                self.__isBusCurrent = False

        elif(eName == "PRODUCT_SERIAL_NUMBER"):
            if(self.__isHWProduct == True):
                self.__isProductSN = False

        elif(eName == "COMPONENT_TYPE_NUMBER"):
            if(self.__isHWProduct == True):
                self.__isCompTypeNo = False

        elif(eName == "PRODUCT_PICTURE"):
            if(self.__isHWProduct == True):
                self.__isProductPic = False

        elif(eName == "BCU_TYPE_NUMBER"):
            if(self.__isHWProduct == True):
                self.__isBCUType = False

        elif(eName == "PRODUCT_HANDLING"):
            if(self.__isHWProduct == True):
                self.__isProductHandling = False

        elif(eName == "PRODUCT_DLL"):
            if(self.__isHWProduct == True):
                self.__isProductDLL = False

        elif(eName == "ORIGINAL_MANUFACTURER_ID"):
            if(self.__isHWProduct == True):
                self.__isOrigManID = False



    def characters(self ,char):

        strValue = char.encode( "iso-8859-1" )

        #print char.encode( "iso-8859-1" )
        if(self.__isProductID == True):
            #self.__Index = 1
            self.__prod.setProductID(self.IsNumber(strValue))
        elif(self.__isManufacturerID == True):
            #self.__Index = 2
            self.__prod.setManufactuerID(self.IsNumber(strValue))
        elif(self.__isSymbolID  == True):
            #self.__Index = 3
            self.__prod.setSymbolID(self.IsNumber(strValue))
        elif(self.__isProductName == True):
            #self.__Index = 4
            self.__prod.setProductName(self.IsString(strValue))
        elif(self.__isProductVersion == True):
            #self.__Index = 5
            self.__prod.setProductVersion(self.IsNumber(strValue))
        elif(self.__isCompType == True):
            #self.__Index = 6
            self.__prod.setCompType(self.IsNumber(strValue))
        elif(self.__isCompAttr == True):
            #self.__Index = 7
            self.__prod.setCompAttr(self.IsNumber(strValue))
        elif(self.__isBusCurrent == True):
            #self.__Index = 8
            self.__prod.setBusCurrent(self.IsNumber(strValue))
        elif(self.__isProductSN == True):
            #self.__Index = 9
            self.__prod.setProductSN(self.IsString(strValue))
        elif(self.__isCompTypeNo == True):
            #self.__Index = 10
            self.__prod.setCompTypeNo(self.IsNumber(strValue))
        elif(self.__isProductPic == True):
            #self.__Index = 11
            self.__prod.setProductPic(self.IsString(strValue))
        elif(self.__isBCUType == True):
            #self.__Index = 12
            self.__prod.setBCUType(self.IsNumber(strValue))
        elif(self.__isProductHandling == True):
            #self.__Index = 13
            self.__prod.setProductHandling(self.IsNumber(strValue))
        elif(self.__isProductDLL == True):
            #self.__Index = 14
            self.__prod.setProductDLL(self.IsString(strValue))
        elif(self.__isOrigManID == True):
            #self.__Index = 15
            self.__prod.setOrigManID(self.IsNumber(strValue))

        #if(self.__Index <> 0):
        #    self.__prod.setProduct(self.__Index,char.encode( "iso-8859-1" ))
        #    self.__Index = 0

    def IsNumber(self,strValue):
        #print strValue
        if(strValue.isdigit() == True):
            return strValue
        else:
            return "0"

    #check for String in parsed value
    def IsString(self,strValue):

        #Value = strValue.replace('\\r\\n',' ')
        #Value = Value.replace('\\rn', ' ')
        #Value = Value.replace("'", ' ')
        return strValue
