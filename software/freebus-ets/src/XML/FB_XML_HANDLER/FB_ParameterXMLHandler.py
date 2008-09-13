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
#Version: V0.2 , 15.06.2008
#Version: V0.3 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================

from re import *
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
    __isParentParmValue = False         #PARENT_PARM_VALUE             NEU
    __isParameterSize = False           #PARAMETER_SIZE
    __isParameterFunction = False       #PARAMETER_FUNCTION            NEU
    __isParameterDisplayOrder = False   #PARAMETER_DISPLAY_ORDER
    __isParameterAddress = False        #PARAMETER_ADDRESS
    __isParameterBitOffset = False      #PARAMETER_BITOFFSET
    __isParameterDescription = False    #PARAMETER_DESCRIPTION
    __isParameterID = False             #PARAMETER_ID
    __isParParameterID = False          #PAR_PARAMETER_ID
    __isParameterLabel = False          #PARAMETER_LABEL                NEU
    __isParameterDefault = False        #PARAMETER_DEFAULT_LONG
    __isParameterDefaultStr = False     #PARAMETER_DEFAULT_STRING       NEU
    __isContext_ID = False              #CONTEXT_ID                     NEU
    __isParameterDefaultDouble = False  #PARAMETER_DEFAULT_DOUBLE       NEU
    __isPatchAlways = False             #PATCH_ALWAYS
    __isAddressSpace = False            #ADDRESS_SPACE
    __isEIB_Object_Ref = False          #EIB_OBJECT_REF                 NEU
    __isEIB_Property_ID = False         #EIB_PROPERTY_ID                NEU
    __isCalculationID = False           #CalculationID                  NEU
    __isCalculationSet = False          #CalculationSet                 NEU
    __isAliasName = False               #AliasName                      NEU



    #Block of Parameter Type Node
    __isParameterTypeID2 = False        #PARAMETER_TYPE_ID
    __isAtomicTypeNumber = False        #ATOMIC_TYPE_NUMBER
    __isPrgramID2 = False               #PROGRAM_ID
    __isParameterTypeName = False       #PARAMETER_TYPE_NAME
    __isParameter_Min_Value = False     #PARAMETER_MINIMUM_VALUE            NEU
    __isParameter_Max_Value = False     #PARAMETER_MAXIMUM_VALUE            NEU
    __isParameter_Type_Description = False #PARAMETER_TYPE_DESCRIPTION         NEU
    __isParameterTypeLowAccess = False  #PARAMETER_TYPE_LOW_ACCESS
    __isParameterTypeHighAccess = False #PARAMETER_TYPE_HIGH_ACCESS
    __isParameterTypeSize = False       #PARAMETER_TYPE_SIZE
    __isParameter_MinDouble_Value = False #PARAMETER_MINIMUM_DOUBLE_VALUE    NEU
    __isParameter_MaxDouble_Value = False #PARAMETER_MAXIMUM_DOUBLE_VALUE    NEU
    __isParameter_UI_HINT = False       #PARAMETER_UI_HINT                 NEU



    #Block of ParameterList of values
    __isParameterTypeID3 = False        #PARAMETER_TYPE_ID
    __isRealValue = False               #REAL_VALUE
    __isDisplayValue = False            #DISPLAYED_VALUE
    __isDisplayOrder = False            #DISPLAY_ORDER
    __isParameterValueID = False        #PARAMETER_VALUE_ID
    __isBinaryValue = False             #BINARY_VALUE            NEU
    __isBinaryValueLength = False       #BINARY_VALUE_LENGTH
    __isDoubleValue = False             #DOUBLE_VALUE            NEU


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
                #print "start parameter"
                self.__isParameter = True

            if(eName == "parameter_type"):
                #print "start parameter type"
                self.__isParaType = True


            if(eName == "parameter_list_of_values"):
                #print "start list of value"
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

            elif(eName == "PARENT_PARM_VALUE" and self.__isParameter == True):
                self.__isParentParmValue = True

            elif(eName == "PARAMETER_SIZE" and self.__isParameter == True):
                self.__isParameterSize = True

            elif(eName == "PARAMETER_FUNCTION" and self.__isParameter == True):
                self.__isParameterFunction = True

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

            elif(eName == "PARAMETER_LABEL" and self.__isParameter == True):
                self.__isParameterLabel = True

            elif(eName == "PARAMETER_DEFAULT_LONG" and self.__isParameter == True):
                self.__isParameterDefault = True

            elif(eName == "PARAMETER_DEFAULT_STRING" and self.__isParameter == True):
                self.__isParameterDefaultStr = True

            elif(eName == "CONTEXT_ID" and self.__isParameter == True):
                self.__isContext_ID = True

            elif(eName == "PARAMETER_DEFAULT_DOUBLE" and self.__isParameter == True):
                self.__isParameterDefaultDouble = True

            elif(eName == "PATCH_ALWAYS" and self.__isParameter == True):
                self.__isPatchAlways = True

            elif(eName == "ADDRESS_SPACE" and self.__isParameter == True):
                self.__isAddressSpace = True

            elif(eName == "EIB_OBJECT_REF" and self.__isParameter == True):
                self.__isEIB_Object_Ref = True

            elif(eName == "EIB_PROPERTY_ID" and self.__isParameter == True):
                self.__isEIB_Property_ID = True

            elif(eName == "CalculationID" and self.__isParameter == True):
                self.__isCalculationID = True

            elif(eName == "CalculationSet" and self.__isParameter == True):
                self.__isCalculationSet = True

            elif(eName == "AliasName" and self.__isParameter == True):
                self.__isAliasName = True

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

            elif(eName == "PARAMETER_MINIMUM_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_Min_Value = True

            elif(eName == "PARAMETER_MAXIMUM_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_Max_Value = True

            elif(eName == "PARAMETER_TYPE_DESCRIPTION" and self.__isParaType == True):
                #print eName
                self.__isParameter_Type_Description = True

            elif(eName == "PARAMETER_TYPE_LOW_ACCESS" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeLowAccess = True

            elif(eName == "PARAMETER_TYPE_HIGH_ACCESS" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeHighAccess = True

            elif(eName == "PARAMETER_TYPE_SIZE" and self.__isParaType == True):
                #print eName
                self.__isParameterTypeSize = True

            elif(eName == "PARAMETER_MINIMUM_DOUBLE_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_MinDouble_Value = True

            elif(eName == "PARAMETER_MAXIMUM_DOUBLE_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_MaxDouble_Value = True

            elif(eName == "PARAMETER_UI_HINT" and self.__isParaType == True):
                #print eName
                self.__isParameter_UI_HINT = True

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

            elif(eName == "BINARY_VALUE" and self.__isParaList == True):
                self.__isBinaryValue = True

            elif(eName == "BINARY_VALUE_LENGTH" and self.__isParaList == True):
                self.__isBinaryValueLength = True

            elif(eName == "DOUBLE_VALUE" and self.__isParaList == True):
                self.__isDoubleValue = True


        except SAXException:
            print "Error again"



    def endElement(self,eName):
       # if(self.__isParameter == True):
       #     print eName

        try:
            if(eName == "parameter"):
                self.__isParameter = False
                #print "end parameter"

                self.__parameter.append(self.__para)
                del self.__para
                self.__para = FB_Parameter.FB_Parameter()

            if(eName == "parameter_type"):

                self.__isParaType = False
                #print "end parameter type"
                self.__paratype.append(self.__paraTy)
                del self.__paraTy
                self.__paraTy = FB_ParameterType.FB_ParameterType()

            if(eName == "parameter_list_of_values"):
                self.__isParaList = False
                #print "end list of value"
                self.__paraList.append(self.__paraLi)
                del self.__paraLi
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

            elif(eName == "PARENT_PARM_VALUE" and self.__isParameter == True):
                self.__isParentParmValue = False

            elif(eName == "PARAMETER_SIZE" and self.__isParameter == True):
                self.__isParameterSize = False

            elif(eName == "PARAMETER_FUNCTION" and self.__isParameter == True):
                self.__isParameterFunction = False

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

            elif(eName == "PARAMETER_LABEL" and self.__isParameter == True):
                self.__isParameterLabel = False

            elif(eName == "PARAMETER_DEFAULT_LONG" and self.__isParameter == True):
                self.__isParameterDefault = False

            elif(eName == "PARAMETER_DEFAULT_STRING" and self.__isParameter == True):
                self.__isParameterDefaultStr = False

            elif(eName == "CONTEXT_ID" and self.__isParameter == True):
                self.__isContext_ID = False

            elif(eName == "PARAMETER_DEFAULT_DOUBLE" and self.__isParameter == True):
                self.__isParameterDefaultDouble = False

            elif(eName == "PATCH_ALWAYS" and self.__isParameter == True):
                self.__isPatchAlways = False

            elif(eName == "ADDRESS_SPACE" and self.__isParameter == True):
                self.__isAddressSpace = False

            elif(eName == "EIB_OBJECT_REF" and self.__isParameter == True):
                self.__isEIB_Object_Ref = False

            elif(eName == "EIB_PROPERTY_ID" and self.__isParameter == True):
                self.__isEIB_Property_ID = False

            elif(eName == "CalculationID" and self.__isParameter == True):
                self.__isCalculationID = False

            elif(eName == "CalculationSet" and self.__isParameter == True):
                self.__isCalculationSet = False

            elif(eName == "AliasName" and self.__isParameter == True):
                self.__isAliasName = False

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

            elif(eName == "PARAMETER_MINIMUM_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_Min_Value = False

            elif(eName == "PARAMETER_MAXIMUM_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_Max_Value = False

            elif(eName == "PARAMETER_TYPE_DESCRIPTION" and self.__isParaType == True):
                #print eName
                self.__isParameter_Type_Description = False

            elif(eName == "PARAMETER_TYPE_LOW_ACCESS" and self.__isParaType == True):
                self.__isParameterTypeLowAccess = False

            elif(eName == "PARAMETER_TYPE_HIGH_ACCESS" and self.__isParaType == True):
                self.__isParameterTypeHighAccess = False

            elif(eName == "PARAMETER_TYPE_SIZE" and self.__isParaType == True):
                self.__isParameterTypeSize = False

            elif(eName == "PARAMETER_MINIMUM_DOUBLE_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_MinDouble_Value = False

            elif(eName == "PARAMETER_MAXIMUM_DOUBLE_VALUE" and self.__isParaType == True):
                #print eName
                self.__isParameter_MaxDouble_Value = False

            elif(eName == "PARAMETER_UI_HINT" and self.__isParaType == True):
                #print eName
                self.__isParameter_UI_HINT = False

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

            elif(eName == "BINARY_VALUE" and self.__isParaList == True):
                self.__isBinaryValue = False

            elif(eName == "BINARY_VALUE_LENGTH" and self.__isParaList == True):
                self.__isBinaryValueLength = False

            elif(eName == "DOUBLE_VALUE" and self.__isParaList == True):
                self.__isDoubleValue = False

        except SAXException:
            print "Error again"


    def characters(self ,char):

       # re = compile('\s')
       # test = re.sub(" ",char.encode( "iso-8859-1" ))
        strValue = char.encode( "iso-8859-1" )

        #------------------- Parameter -----------------------
        if(self.__isPrgramID1 == True):
            self.__para.setProgramID(self.IsNumber(strValue))

        elif(self.__isParameterTypeID1 == True):
            self.__para.setParameterTypeID(self.IsNumber(strValue))

        elif(self.__isParameterNumber  == True):
            self.__para.setParameterNumber(self.IsNumber(strValue))

        elif(self.__isParameterName == True):
            self.__para.setParameterName(self.IsString(strValue))

        elif(self.__isParameterLowAccess == True):
            self.__para.setParameterLow(self.IsNumber(strValue))

        elif(self.__isParameterHighAccess == True):
            self.__para.setParameterHigh(self.IsNumber(strValue))

        elif(self.__isParentParmValue == True):
            self.__para.setParentParmValue(self.IsNumber(strValue))

        elif(self.__isParameterSize == True):
            self.__para.setParameterSize(self.IsNumber(strValue))

        elif(self.__isParameterFunction == True):
            self.__para.setParameterFunction(self.IsString(strValue))

        elif(self.__isParameterDisplayOrder == True):
            self.__para.setParameterDisplayOrder(self.IsNumber(strValue))

        elif(self.__isParameterAddress == True):
            self.__para.setParameterAddress(self.IsNumber(strValue))

        elif(self.__isParameterBitOffset == True):
            self.__para.setParameterBitOffset(self.IsNumber(strValue))

        elif(self.__isParameterDescription == True):
            self.__para.setParameterDescription(self.IsString(strValue))

        elif(self.__isParameterID == True):
            self.__para.setParameterID(self.IsNumber(strValue))

        elif(self.__isParParameterID == True):
            self.__para.setParParameterID(self.IsNumber(strValue))

        elif(self.__isParameterLabel == True):
            self.__para.setParameterLabel(self.IsString(strValue))

        elif(self.__isParameterDefault == True):
            self.__para.setParameterDefaultLong(self.IsNumber(strValue))

        elif(self.__isParameterDefaultStr == True):
            self.__para.setParameterDefaultString(self.IsString(strValue))

        elif(self.__isContext_ID == True):
            self.__para.setContextID(self.IsNumber(strValue))

        elif(self.__isParameterDefaultDouble == True):
            self.__para.setParameterDefaultDouble(self.IsNumber(strValue))

        elif(self.__isPatchAlways == True):
            self.__para.setPatchAlways(self.IsNumber(strValue))

        elif(self.__isAddressSpace == True):
            self.__para.setAddressSpace(self.IsNumber(strValue))

        elif(self.__isEIB_Object_Ref == True):
            self.__para.setEIBObjRef(self.IsNumber(strValue))

        elif(self.__isEIB_Property_ID == True):
            self.__para.setEIBPropertyID(self.IsNumber(strValue))

        elif(self.__isCalculationID == True):
            self.__para.setCalculationID(self.IsNumber(strValue))

        elif(self.__isCalculationSet == True):
            self.__para.setCalculationSet(self.IsString(strValue))

        elif(self.__isAliasName == True):
            self.__para.setAliasName(self.IsString(strValue))

        #------------------- ParameterType -----------------------
        if(self.__isParameterTypeID2 == True):
            self.__paraTy.setParameterTypeID2(self.IsNumber(strValue))

        elif(self.__isAtomicTypeNumber == True):
            self.__paraTy.setAtomicTypeNumber(self.IsNumber(strValue))

        elif(self.__isPrgramID2  == True):
             self.__paraTy.setProgramID2(self.IsNumber(strValue))

        elif(self.__isParameterTypeName == True):
             self.__paraTy.setParameterTypeName(self.IsString(strValue))

        elif(self.__isParameter_Min_Value == True):
             self.__paraTy.setParameterMinValue(self.IsNumber(strValue))

        elif(self.__isParameter_Max_Value == True):
             self.__paraTy.setParameterMaxValue(self.IsNumber(strValue))

        elif(self.__isParameter_Type_Description == True):
             self.__paraTy.setParameterTypeDescription(self.IsString(strValue))

        elif(self.__isParameterTypeLowAccess == True):
             self.__paraTy.setParameterTypeLow(self.IsNumber(strValue))

        elif(self.__isParameterTypeHighAccess == True):
            self.__paraTy.setParameterTypeHigh(self.IsNumber(strValue))

        elif(self.__isParameterTypeSize == True):
            self.__paraTy.setParameterTypeSize(self.IsNumber(strValue))

        elif(self.__isParameter_MinDouble_Value == True):
            self.__paraTy.setParameterMinDoubleValue(self.IsNumber(strValue))

        elif(self.__isParameter_MaxDouble_Value == True):
            self.__paraTy.setParameterMaxDoubleValue(self.IsNumber(strValue))

        elif(self.__isParameter_UI_HINT == True):
            self.__paraTy.setParameterUIHint(self.IsString(strValue))

        #------------------- ParameterList of values --------------------
        if(self.__isParameterTypeID3 == True):
            self.__paraLi.setParameterTypeID3(self.IsNumber(strValue))

        elif(self.__isRealValue == True):
            self.__paraLi.setRealValue(self.IsNumber(strValue))

        elif(self.__isDisplayValue  == True):
            self.__paraLi.setDisplayValue(self.IsString(strValue))

        elif(self.__isDisplayOrder == True):
            self.__paraLi.setDisplayOrder(self.IsNumber(strValue))

        elif(self.__isParameterValueID == True):
            self.__paraLi.setParameterValueID(self.IsNumber(strValue))

        elif(self.__isBinaryValue == True):
            self.__paraLi.setBinaryValue(self.IsNumber(strValue))

        elif(self.__isBinaryValueLength == True):
            self.__paraLi.setBinaryValueLength(self.IsNumber(strValue))

        elif(self.__isDoubleValue == True):
            self.__paraLi.setDoubleValue(self.IsNumber(strValue))


    #check for Number in parsed value
    def IsNumber(self,strValue):
        #print strValue
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
