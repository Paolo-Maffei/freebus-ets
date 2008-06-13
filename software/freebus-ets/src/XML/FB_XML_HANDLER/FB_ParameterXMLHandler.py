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


from FB_DATA import FB_Parameter
from FB_DATA import FB_ParameterType
from FB_DATA import FB_ParameterListV

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
    __isPrgramID1 = False               #PROGRAM_ID
    __isParameterTypeID1 = False        #PARAMETER_TYPE_ID
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
        self.__para = FB_Parameter.FB_Parameter()
        self.__paraTy = FB_ParameterType.FB_ParameterType()
        self.__paraLi = FB_ParameterListV.FB_ParameterListV()

        self.__parameter = []                #init List
        self.__paratype = []                #init List
        self.__paraList = []                #init List


    #return List of Instances of type FB_Parameters
    def getParameter(self):
        #print self.__parameter
        return self.__parameter

    #returns a list of ParameterType Node
    def getParameterType(self):
        #print self.__paratype
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
          #  if(self.__isParaType == True):
          #      print eName

            if(eName == "parameter"):
                self.__isParameter = True

            if(eName == "parameter_type"):
                self.__isParaType = True


            if(eName == "parameter_list_of_values"):
                self.__isParaList = True

            #------------------- Parmater -----------------------
            if(eName == "PROGRAM_ID" and self.__isParameter == True):
                self.__isPrgramID1 = True

            elif(eName == "PARAMETER_TYPE_ID" and self.__isParameter == True):
                self.__isParameterTypeID1 = True

            elif(eName == "PARAMETER_NUMBER" and self.__isParameter == True):
                self.__isParameterNumber = True

            elif(eName == "PARAMETER_NAME" and self.__isParameter == True):
                self.__isParameterName = True

            elif(eName == "PARAMETER_LOW_ACCESS" and self.__isParameter == True):
                self.__isParameterLowAccess = True

            elif(eName == "PARAMETER_HIGH_ACCESS" and self.__isParameter == True):
                self.__isParameterHighAccess = True

            elif(eName == "PARAMETER_SIZE" and self.__isParameter == True):
                self.__isParameterSize = True

            elif(eName == "PARAMETER_DISPLAY_ORDER" and self.__isParameter == True):
                self.__isParameterDisplayOrder = True

            elif(eName == "PARAMETER_ADDRESS" and self.__isParameter == True):
                self.__isParameterAddress = True

            elif(eName == "PARAMETER_BITOFFSET" and self.__isParameter == True):
                self.__isParameterBitOffset = True

            elif(eName == "PARAMETER_DESCRIPTION" and self.__isParameter == True):
                self.__isParameterDescription = True

            elif(eName == "PARAMETER_ID" and self.__isParameter == True):
                self.__isParameterID = True

            elif(eName == "PAR_PARAMETER_ID" and self.__isParameter == True):
                self.__isParParameterID = True

            elif(eName == "PARAMETER_DEFAULT_LONG" and self.__isParameter == True):
                self.__isParameterDefault = True

            elif(eName == "PATCH_ALWAYS" and self.__isParameter == True):
                self.__isPatchAlways = True

            elif(eName == "ADDRESS_SPACE" and self.__isParameter == True):
                self.__isAddressSpace = True
            #------------------- end of Parmater -----------------------


            #------------------- ParameterType -----------------------
            if(eName == "PARAMETER_TYPE_ID" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeID2 = True

            elif(eName == "ATOMIC_TYPE_NUMBER" and self.__isParaType == True):
                #print eName
                self.__isAtomicTypeNumber = True

            elif(eName == "PROGRAM_ID" and self.__isParaType == True):
                #print eName
                self.__isPrgramID2 = True

            elif(eName == "PARAMETER_TYPE_NAME" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeName = True

            elif(eName == "PARAMETER_TYPE_LOW_ACCESS" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeLowAccess = True

            elif(eName == "PARAMETER_TYPE_HIGH_ACCESS" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeHighAccess = True

            elif(eName == "PARAMETER_TYPE_SIZE" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeSize = True

            #------------------- end of ParameterType -----------------------

            #------------------- ParameterList of values --------------------
            if(eName == "PARAMETER_TYPE_ID" and self.__isParaList == True):
                self.__isParameterTypeID3 = True

            elif(eName == "REAL_VALUE" and self.__isParaList == True):
                self.__isRealValue = True

            elif(eName == "DISPLAYED_VALUE" and self.__isParaList == True):
                self.__isDisplayValue = True

            elif(eName == "DISPLAY_ORDER" and self.__isParaList == True):
                self.__isDisplayOrder = True

            elif(eName == "PARAMETER_VALUE_ID" and self.__isParaList == True):
                self.__isParameterValueID = True

            elif(eName == "BINARY_VALUE_LENGTH" and self.__isParaList == True):
                self.__isBinaryValueLength = True


        except SAXException:
            print "Error again"



    def endElement(self,eName):
       # if(self.__isParameter == True):
       #     print eName

        try:
            if(eName == "parameter"):
                self.__isParameter = False
          #      print "start parame"
                self.__parameter.append(self.__para)
                self.__para = None
                self.__para = FB_Parameter.FB_Parameter()

            if(eName == "parameter_type"):

                self.__isParaType = False

                self.__paratype.append(self.__paraTy)
                self.__paraTy = None
                self.__paraTy = FB_ParameterType.FB_ParameterType()

            if(eName == "parameter_list_of_values"):
                self.__isParaList = False

                self.__paraList.append(self.__paraLi)
                self.__paraLi = None
                self.__paraLi = FB_ParameterListV.FB_ParameterListV()

            #------------------- Parmater -----------------------
            if(eName == "PROGRAM_ID" and self.__isParameter == True):
                self.__isPrgramID1 = False

            elif(eName == "PARAMETER_TYPE_ID" and self.__isParameter == True):
                self.__isParameterTypeID1 = False

            elif(eName == "PARAMETER_NUMBER" and self.__isParameter == True):
                self.__isParameterNumber = False

            elif(eName == "PARAMETER_NAME" and self.__isParameter == True):
                self.__isParameterName = False

            elif(eName == "PARAMETER_LOW_ACCESS" and self.__isParameter == True):
                self.__isParameterLowAccess = False

            elif(eName == "PARAMETER_HIGH_ACCESS" and self.__isParameter == True):
                self.__isParameterHighAccess = False

            elif(eName == "PARAMETER_SIZE" and self.__isParameter == True):
                self.__isParameterSize = False

            elif(eName == "PARAMETER_DISPLAY_ORDER" and self.__isParameter == True):
                self.__isParameterDisplayOrder = False

            elif(eName == "PARAMETER_ADDRESS" and self.__isParameter == True):
                self.__isParameterAddress = False

            elif(eName == "PARAMETER_BITOFFSET" and self.__isParameter == True):
                self.__isParameterBitOffset = False

            elif(eName == "PARAMETER_DESCRIPTION" and self.__isParameter == True):
                self.__isParameterDescription = False

            elif(eName == "PARAMETER_ID" and self.__isParameter == True):
                self.__isParameterID = False

            elif(eName == "PAR_PARAMETER_ID" and self.__isParameter == True):
                self.__isParParameterID = False

            elif(eName == "PARAMETER_DEFAULT_LONG" and self.__isParameter == True):
                self.__isParameterDefault = False

            elif(eName == "PATCH_ALWAYS" and self.__isParameter == True):
                self.__isPatchAlways = False

            elif(eName == "ADDRESS_SPACE" and self.__isParameter == True):
                self.__isAddressSpace = False
            #------------------- end of Parmater -----------------------

            #------------------- ParameterType -----------------------
            if(eName == "PARAMETER_TYPE_ID" and self.__isParaType == True):
                self.__isParameterTypeID2 = False

            elif(eName == "ATOMIC_TYPE_NUMBER" and self.__isParaType == True):
                self.__isAtomicTypeNumber = False

            elif(eName == "PROGRAM_ID" and self.__isParaType == True):
                self.__isPrgramID2 = False

            elif(eName == "PARAMETER_TYPE_NAME" and self.__isParaType == True):
                self.__isParameterTypeName = False

            elif(eName == "PARAMETER_TYPE_LOW_ACCESS" and self.__isParaType == True):
                self.__isParameterTypeLowAccess = False

            elif(eName == "PARAMETER_TYPE_HIGH_ACCESS" and self.__isParaType == True):
                self.__isParameterTypeHighAccess = False

            elif(eName == "PARAMETER_TYPE_SIZE" and self.__isParaType == True):
                self.__isParameterTypeSize = False

            #------------------- end of ParameterType -----------------------

            #------------------- ParameterList of values --------------------
            if(eName == "PARAMETER_TYPE_ID" and self.__isParaList == True):
                self.__isParameterTypeID3 = False

            elif(eName == "REAL_VALUE" and self.__isParaList == True):
                self.__isRealValue = False

            elif(eName == "DISPLAYED_VALUE" and self.__isParaList == True):
                self.__isDisplayValue = False

            elif(eName == "DISPLAY_ORDER" and self.__isParaList == True):
                self.__isDisplayOrder = False

            elif(eName == "PARAMETER_VALUE_ID" and self.__isParaList == True):
                self.__isParameterValueID = False

            elif(eName == "BINARY_VALUE_LENGTH" and self.__isParaList == True):
                self.__isBinaryValueLength = False


        except SAXException:
            print "Error again"


    def characters(self ,char):

        #------------------- Parameter -----------------------
        if(self.__isPrgramID1 == True):
            #self.__Index = 1
            self.__para.setProgramID(char.encode( "iso-8859-1" ))
        if(self.__isParameterTypeID1 == True):
            #self.__Index = 2
            self.__para.setParameterTypeID(char.encode( "iso-8859-1" ))
        if(self.__isParameterNumber  == True):
            #self.__Index = 3
            self.__para.setParameterNumber(char.encode( "iso-8859-1" ))
        if(self.__isParameterName == True):
            #self.__Index = 4
            self.__para.setParameterName(char.encode( "iso-8859-1" ))
        if(self.__isParameterLowAccess == True):
            #self.__Index = 5
            self.__para.setParameterLow(char.encode( "iso-8859-1" ))
        if(self.__isParameterHighAccess == True):
            #self.__Index = 6
            self.__para.setParameterHigh(char.encode( "iso-8859-1" ))
        if(self.__isParameterSize == True):
            #self.__Index = 7
            self.__para.setParameterSize(char.encode( "iso-8859-1" ))
        if(self.__isParameterDisplayOrder == True):
            #self.__Index = 8
            self.__para.setParameterDisplayOrder(char.encode( "iso-8859-1" ))
        if(self.__isParameterAddress == True):
            #self.__Index = 9
            self.__para.setParameterAddress(char.encode( "iso-8859-1" ))
        if(self.__isParameterBitOffset == True):
            #self.__Index = 10
            self.__para.setParameterBitOffset(char.encode( "iso-8859-1" ))
        if(self.__isParameterDescription == True):
            #self.__Index = 11
            self.__para.setParameterDescription(char.encode( "iso-8859-1" ))
        if(self.__isParameterID == True):
            #self.__Index = 12
            self.__para.setParameterID(char.encode( "iso-8859-1" ))
        if(self.__isParParameterID == True):
            #self.__Index = 13
            self.__para.setParParameterID(char.encode( "iso-8859-1" ))
        if(self.__isParameterDefault == True):
            #self.__Index = 14
            self.__para.setParameterDefault(char.encode( "iso-8859-1" ))
        if(self.__isPatchAlways == True):
            #self.__Index = 15
            self.__para.setPatchAlways(char.encode( "iso-8859-1" ))
        if(self.__isAddressSpace == True):
            #self.__Index = 16
            self.__para.setAddressSpace(char.encode( "iso-8859-1" ))

        #------------------- ParameterType -----------------------
        if(self.__isParameterTypeID2 == True):
            #self.__Index = 1
            self.__paraTy.setParameterTypeID2(char.encode( "iso-8859-1" ))

        if(self.__isAtomicTypeNumber == True):
            #self.__Index = 2
            ##print char
            self.__paraTy.setAtomicTypeNumber(char.encode( "iso-8859-1" ))
        if(self.__isPrgramID2  == True):
            #self.__Index = 3
            #print char
            self.__paraTy.setProgramID2(char.encode( "iso-8859-1" ))
        if(self.__isParameterTypeName == True):
            #self.__Index = 4
            #print char
            self.__paraTy.setParameterTypeName(char.encode( "iso-8859-1" ))
        if(self.__isParameterTypeLowAccess == True):
            #self.__Index = 5
            #print char
            self.__paraTy.setParameterTypeLow(char.encode( "iso-8859-1" ))
        if(self.__isParameterTypeHighAccess == True):
            #self.__Index = 6
            #print char
            self.__paraTy.setParameterTypeHigh(char.encode( "iso-8859-1" ))
        if(self.__isParameterTypeSize == True):
            #self.__Index = 7
            self.__paraTy.setParameterTypeSize(char.encode( "iso-8859-1" ))



        #------------------- ParameterList of values --------------------
        if(self.__isParameterTypeID3 == True):
            #self.__Index = 1
            self.__paraLi.setParameterTypeID3(char.encode( "iso-8859-1" ))
        if(self.__isRealValue == True):
            #self.__Index = 2
            self.__paraLi.setRealValue(char.encode( "iso-8859-1" ))
        if(self.__isDisplayValue  == True):
            #self.__Index = 3
            self.__paraLi.setDisplayValue(char.encode( "iso-8859-1" ))
        if(self.__isDisplayOrder == True):
            #self.__Index = 4
            self.__paraLi.setDisplayOrder(char.encode( "iso-8859-1" ))
        if(self.__isParameterValueID == True):
            #self.__Index = 5
            self.__paraLi.setParameterValueID(char.encode( "iso-8859-1" ))
        if(self.__isBinaryValueLength == True):
            #self.__Index = 6
            self.__paraLi.setBinaryValueLength(char.encode( "iso-8859-1" ))
