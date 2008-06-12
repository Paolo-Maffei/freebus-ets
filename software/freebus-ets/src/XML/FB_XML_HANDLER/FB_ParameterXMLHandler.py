#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ParameterXMLHandler.py
#Version: V0.1 , 09.06.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================


from FB_DATA import FB_Products

##General XML-Handler Class, parse entire XML-Data File and fill alle Data-Structures
##Products, Applications, Communications-objects
class FB_ParameterXMLHandler():

    __LogObj = None
    __parameter = []            #List of Parameter
    __paratype = []        #List of ParameterType
    __paraList = []        #List of ParameterList (look at FB_Constants...)
    __para = None
    __paraTy = None
    __paraLi = None

    __Index = 0

    __isParameter = False
    __isParaType = False
    __isParaList = False


    #Block of Paramter variable
    __isPrgramID1 = False                #PROGRAM_ID
    __isParameterTypeID1 = False         #PARAMETER_TYPE_ID
    __isParameterNumber = False         #PARAMETER_NUMBER
    __isParameterName = False           #PARAMETER_NAME
    __isParameterLowAccess = False      #PARAMETER_LOW_ACCESS
    __isParameterHighAccess = False     #PARAMETER_HIGH_ACCESS
    __isParameterSize = False           #PARAMETER_SIZE
    __isParameterDisplayOrder = False   #PARAMETER_DISPLAY_ORDER
    __isParameterAddress = False        #PARAMETER_ADDRESS
    __isParameterBitOffset = False      #PARAMETER_BITOFFSET
    __isParameterDescription = False    #PARAMETER_DESCRIPTION
    __isParameterID = False             #PARAMETER_ID
    __isParParameterID = False          #PAR_PARAMETER_ID
    __isParameterDefault = False        #PARAMETER_DEFAULT_LONG
    __isPatchAlways = False             #PATCH_ALWAYS
    __isAddressSpace = False            #ADDRESS_SPACE


    #Block of Parameter Type Node
    __isParameterTypeID2 = False        #PARAMETER_TYPE_ID
    __isAtomicTypeNumber = False        #ATOMIC_TYPE_NUMBER
    __isPrgramID2 = False               #PROGRAM_ID
    __isParameterTypeName = False       #PARAMETER_TYPE_NAME
    __isParameterTypeLowAccess = False  #PARAMETER_TYPE_LOW_ACCESS
    __isParameterTypeHighAccess = False #PARAMETER_TYPE_HIGH_ACCESS
    __isParameterTypeSize = False       #PARAMETER_TYPE_SIZE


    #Block of ParameterList of values
    __isParameterTypeID3 = False        #PARAMETER_TYPE_ID
    __isRealValue = False               #REAL_VALUE
    __isDisplayValue = False            #DISPLAYED_VALUE
    __isDisplayOrder = False            #DISPLAY_ORDER
    __isParameterValueID = False        #PARAMETER_VALUE_ID
    __isBinaryValueLength = False       #BINARY_VALUE_LENGTH


    def __init__(self, LogObj):
        self.__LogObj = LogObj
        self.__para = FB_Parameter.FB_Parameter()    #FB_ProductXMLHandler
        self.__products = []                #init List


    #return List of Instances of type FB_Parameters
    def getParameter(self):
        return self.__parameter

    #returns a list of ParameterType Node
    def getParameterType(self):
        return self.__paratype

    #returns the Parameter List of Values Node
    def getParameterList(self):
        return self.__paraList


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
            if(eName == "parameter"):
                self.__isParameter = True

            elif(eName == "parameter_type"):
                self.__isParaType = True

            elif(eName == "parameter_list_of_values"):
                self.__isParaList = True

            #------------------- Parmater -----------------------
            elif(eName == "PROGRAM_ID"):
                if(self.__isParameter == True):
                    self.__isPrgramID1 = True

            elif(eName == "PARAMETER_TYPE_ID"):
                if(self.__isParameter == True):
                    self.__isParameterTypeID1 = True

            elif(eName == "PARAMETER_NUMBER"):
                if(self.__isParameter == True):
                    self.__isParameterNumber = True

            elif(eName == "PARAMETER_NAME"):
                if(self.__isParameter == True):
                    self.__isParameterName = True

            elif(eName == "PARAMETER_LOW_ACCESS"):
                if(self.__isParameter == True):
                    self.__isParameterLowAccess = True

            elif(eName == "PARAMETER_HIGH_ACCESS"):
                if(self.__isParameter == True):
                    self.__isParameterHighAccess = True

            elif(eName == "PARAMETER_SIZE"):
                if(self.__isParameter == True):
                    self.__isParameterSize = True

            elif(eName == "PARAMETER_DISPLAY_ORDER"):
                if(self.__isParameter == True):
                    self.__isParameterDisplayOrder = True

            elif(eName == "PARAMETER_ADDRESS"):
                if(self.__isParameter == True):
                    self.__isParameterAddress = True

            elif(eName == "PARAMETER_BITOFFSET"):
                if(self.__isParameter == True):
                    self.__isParameterBitOffset = True

            elif(eName == "PARAMETER_DESCRIPTION"):
                if(self.__isParameter == True):
                    self.__isParameterDescription = True

            elif(eName == "PARAMETER_ID"):
                if(self.__isParameter == True):
                    self.__isParameterID = True

            elif(eName == "PAR_PARAMETER_ID"):
                if(self.__isParameter == True):
                    self.__isParParameterID = True

            elif(eName == "PARAMETER_DEFAULT_LONG"):
                if(self.__isParameter == True):
                    self.__isParameterDefault = True

            elif(eName == "PATCH_ALWAYS"):
                if(self.__isParameter == True):
                    self.__isPatchAlways = True

            elif(eName == "ADDRESS_SPACE"):
                if(self.__isParameter == True):
                    self.__isAddressSpace = True
            #------------------- end of Parmater -----------------------


            #------------------- ParameterType -----------------------
            elif(eName == "PARAMETER_TYPE_ID"):
                if(self.__isParaType == True):
                    self.__isParameterTypeID2 = True

            elif(eName == "ATOMIC_TYPE_NUMBER"):
                if(self.__isParaType == True):
                    self.__isAtomicTypeNumber = True

            elif(eName == "PROGRAM_ID"):
                if(self.__isParaType == True):
                    self.__isPrgramID2 = True

            elif(eName == "PARAMETER_TYPE_NAME"):
                if(self.__isParaType == True):
                    self.__isParameterTypeName = True

            elif(eName == "PARAMETER_TYPE_LOW_ACCESS"):
                if(self.__isParaType == True):
                    self.__isParameterTypeLowAccess = True

            elif(eName == "PARAMETER_TYPE_HIGH_ACCESS"):
                if(self.__isParameter == True):
                    self.__isParameterTypeHighAccess = True

            elif(eName == "PARAMETER_TYPE_SIZE"):
                if(self.__isParaType == True):
                    self.__isParameterTypeSize = True

            #------------------- end of ParameterType -----------------------

            #------------------- ParameterList of values --------------------
            elif(eName == "PARAMETER_TYPE_ID"):
                if(self.__isParaList == True):
                    self.__isParameterTypeID3 = True

            elif(eName == "REAL_VALUE"):
                if(self.__isParaList == True):
                    self.__isRealValue = True

            elif(eName == "DISPLAYED_VALUE"):
                if(self.__isParaList == True):
                    self.__isDisplayValue = True

            elif(eName == "DISPLAY_ORDER"):
                if(self.__isParaList == True):
                    self.__isDisplayOrder = True

            elif(eName == "PARAMETER_VALUE_ID"):
                if(self.__isParaList == True):
                    self.__isParameterValueID = True

            elif(eName == "BINARY_VALUE_LENGTH"):
                if(self.__isParaList == True):
                    self.__isBinaryValueLength = True


        except SAXException:
            print "Error again"



    def endElement(self,eName):
        #print eName
        if(eName == "parameter"):
            self.__isParameter=False

            self.__parameter.append(self.__para)
            self.__para = None
            #self.__para = FB_Products.FB_Products()

        elif(eName == "parameter_type"):
            self.__isParaType = False

            self.__paratype.append(self.__paraTy)
            self.__paraTy = None
            #self.__paraTy = FB_Products.FB_Products()

        elif(eName == "parameter_list_of_values"):
            self.__isParaList = False

            self.__paraList.append(self.__paraLi)
            self.__paraLi = None
            #self.__paraLi = FB_Products.FB_Products()


        #------------------- Parmater -----------------------
        elif(eName == "PROGRAM_ID"):
            if(self.__isParameter == True):
                self.__isPrgramID1 = False

        elif(eName == "PARAMETER_TYPE_ID"):
            if(self.__isParameter == True):
                self.__isParameterTypeID1 = False

        elif(eName == "PARAMETER_NUMBER"):
            if(self.__isParameter == True):
                self.__isParameterNumber = False

        elif(eName == "PARAMETER_NAME"):
            if(self.__isParameter == True):
                self.__isParameterName = False

        elif(eName == "PARAMETER_LOW_ACCESS"):
            if(self.__isParameter == True):
                self.__isParameterLowAccess = False

        elif(eName == "PARAMETER_HIGH_ACCESS"):
            if(self.__isParameter == True):
                self.__isParameterHighAccess = False

        elif(eName == "PARAMETER_SIZE"):
            if(self.__isParameter == True):
                self.__isParameterSize = False

        elif(eName == "PARAMETER_DISPLAY_ORDER"):
            if(self.__isParameter == True):
                self.__isParameterDisplayOrder = False

        elif(eName == "PARAMETER_ADDRESS"):
            if(self.__isParameter == True):
                self.__isParameterAddress = False

        elif(eName == "PARAMETER_BITOFFSET"):
            if(self.__isParameter == True):
                self.__isParameterBitOffset = False

        elif(eName == "PARAMETER_DESCRIPTION"):
            if(self.__isParameter == True):
                self.__isParameterDescription = False

        elif(eName == "PARAMETER_ID"):
            if(self.__isParameter == True):
                self.__isParameterID = False

        elif(eName == "PAR_PARAMETER_ID"):
            if(self.__isParameter == True):
                self.__isParParameterID = False

        elif(eName == "PARAMETER_DEFAULT_LONG"):
            if(self.__isParameter == True):
                self.__isParameterDefault = False

        elif(eName == "PATCH_ALWAYS"):
            if(self.__isParameter == True):
                self.__isPatchAlways = False

        elif(eName == "ADDRESS_SPACE"):
            if(self.__isParameter == True):
                self.__isAddressSpace = False
        #------------------- end of Parmater -----------------------

        #------------------- ParameterType -----------------------
        elif(eName == "PARAMETER_TYPE_ID"):
            if(self.__isParaType == True):
                self.__isParameterTypeID2 = False

        elif(eName == "ATOMIC_TYPE_NUMBER"):
            if(self.__isParaType == True):
                self.__isAtomicTypeNumber = False

        elif(eName == "PROGRAM_ID"):
            if(self.__isParaType == True):
                self.__isPrgramID2 = False

        elif(eName == "PARAMETER_TYPE_NAME"):
            if(self.__isParaType == True):
                self.__isParameterTypeName = False

        elif(eName == "PARAMETER_TYPE_LOW_ACCESS"):
            if(self.__isParaType == True):
                self.__isParameterTypeLowAccess = False

        elif(eName == "PARAMETER_TYPE_HIGH_ACCESS"):
            if(self.__isParameter == True):
                self.__isParameterTypeHighAccess = False

        elif(eName == "PARAMETER_TYPE_SIZE"):
            if(self.__isParaType == True):
                self.__isParameterTypeSize = False

        #------------------- end of ParameterType -----------------------

        #------------------- ParameterList of values --------------------
        elif(eName == "PARAMETER_TYPE_ID"):
            if(self.__isParaList == True):
                self.__isParameterTypeID3 = False

        elif(eName == "REAL_VALUE"):
            if(self.__isParaList == True):
                self.__isRealValue = False

        elif(eName == "DISPLAYED_VALUE"):
            if(self.__isParaList == True):
                self.__isDisplayValue = False

        elif(eName == "DISPLAY_ORDER"):
            if(self.__isParaList == True):
                self.__isDisplayOrder = False

        elif(eName == "PARAMETER_VALUE_ID"):
            if(self.__isParaList == True):
                self.__isParameterValueID = False

        elif(eName == "BINARY_VALUE_LENGTH"):
            if(self.__isParaList == True):
                self.__isBinaryValueLength = False



    def characters(self ,char):

        #print char.encode( "iso-8859-1" )
        if(self.__isProductID == True):
            #self.__Index = 1
            self.__prod.setProductID(char.encode( "iso-8859-1" ))
        if(self.__isManufacturerID == True):
            #self.__Index = 2
            self.__prod.setManufactuerID(char.encode( "iso-8859-1" ))
        if(self.__isSymbolID  == True):
            #self.__Index = 3
            self.__prod.setSymbolID(char.encode( "iso-8859-1" ))
        if(self.__isProductName == True):
            #self.__Index = 4
            self.__prod.setProductName(char.encode( "iso-8859-1" ))
        if(self.__isProductVersion == True):
            #self.__Index = 5
            self.__prod.setProductVersion(char.encode( "iso-8859-1" ))
        if(self.__isCompType == True):
            #self.__Index = 6
            self.__prod.setCompType(char.encode( "iso-8859-1" ))
        if(self.__isCompAttr == True):
            #self.__Index = 7
            self.__prod.setCompAttr(char.encode( "iso-8859-1" ))
        if(self.__isBusCurrent == True):
            #self.__Index = 8
            self.__prod.setBusCurrent(char.encode( "iso-8859-1" ))
        if(self.__isProductSN == True):
            #self.__Index = 9
            self.__prod.setProductSN(char.encode( "iso-8859-1" ))
        if(self.__isCompTypeNo == True):
            #self.__Index = 10
            self.__prod.setCompTypeNo(char.encode( "iso-8859-1" ))
        if(self.__isProductPic == True):
            #self.__Index = 11
            self.__prod.setProductPic(char.encode( "iso-8859-1" ))
        if(self.__isBCUType == True):
            #self.__Index = 12
            self.__prod.setBCUType(char.encode( "iso-8859-1" ))
        if(self.__isProductHandling == True):
            #self.__Index = 13
            self.__prod.setProductHandling(char.encode( "iso-8859-1" ))
        if(self.__isProductDLL == True):
            #self.__Index = 14
            self.__prod.setProductDLL(char.encode( "iso-8859-1" ))
        if(self.__isOrigManID == True):
            #self.__Index = 15
            self.__prod.setOrigManID(char.encode( "iso-8859-1" ))

        #if(self.__Index <> 0):
        #    self.__prod.setProduct(self.__Index,char.encode( "iso-8859-1" ))
        #    self.__Index = 0