#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ParameterListV.py
#Version: V0.1 , 13.06.2008
#Version: V0.2 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_ParameterListV:

    #local variables ParameterList of values
    __ParameterTypeID3 = None        #PARAMETER_TYPE_ID
    __RealValue = None               #REAL_VALUE
    __DisplayValue = None            #DISPLAYED_VALUE
    __DisplayOrder = None            #DISPLAY_ORDER
    __ParameterValueID = None        #PARAMETER_VALUE_ID
    __BinaryValue = None             #BINARY_VALUE            NEU
    __BinaryValueLength = None       #BINARY_VALUE_LENGTH
    __DoubleValue = None             #DOUBLE_VALUE            NEU


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__ParameterTypeID3,self.__RealValue,self.__DisplayValue,self.__DisplayOrder,
               self.__ParameterValueID,self.__BinaryValue, self.__BinaryValueLength, self.__DoubleValue)

        return List

#----------------------- ParameterList of values Handling --------------------------------------
    def setParameterListValues(self,Index, Value):
        if(Index == 1):
            self.__ParameterTypeID3 = Value
        elif(Index == 2):
            self.__RealValue = Value
        elif(Index == 3):
            self.__DisplayValue = Value
        elif(Index == 4):
            self.__DisplayOrder = Value
        elif(Index == 5):
            self.__ParameterValueID = Value
        elif(Index == 6):
            self.__BinaryValue = Value
        elif(Index == 7):
            self.__BinaryValueLength = Value
        elif(Index == 8):
            self.__DoubleValue = Value


    def getParameterListValues(self,Index):
        if(Index == 1):
            return self.__ParameterTypeID3
        elif(Index == 2):
            return self.__RealValue
        elif(Index == 3):
            return self.__DisplayValue
        elif(Index == 4):
            return self.__DisplayOrder
        elif(Index == 5):
            return self.__ParameterValueID
        elif(Index == 6):
            return self.__BinaryValue
        elif(Index == 7):
            return self.__BinaryValueLength
        elif(Index == 8):
            return self.__DoubleValue

#---------------------------------------------------------------------------------
#----------------------- ParameterList of values Handling ------------------------
#---------------------------------------------------------------------------------
#**********************************************************************
   #Handling PARAMETER_TYPE_ID
    def setParameterTypeID3(self,PT_ID3):
        self.__ParameterTypeID3 = PT_ID3

    def getParameterTypeID3(self):
        return self.__ParameterTypeID3

#**********************************************************************
    #REAL_VALUE
    def setRealValue(self,Value):
        self.__RealValue = Value

    def getRealValue(self):
        return self.__RealValue

#**********************************************************************
    #DISPLAYED_VALUE
    def setDisplayValue(self,D_Value):
        self.__DisplayValue = D_Value

    def getDisplayValue(self):
        return self.__DisplayValue

#**********************************************************************
    #DISPLAY_ORDER
    def setDisplayOrder(self,D_Order):
        self.__DisplayOrder = D_Order

    def getDisplayOrder(self):
        return self.__DisplayOrder

#**********************************************************************
    #PARAMETER_VALUE_ID
    def setParameterValueID(self,P_ValueID):
        self.__ParameterValueID = P_ValueID

    def getParameterValueID(self):
        return self.__ParameterValueID
#**********************************************************************
    #BINARY_VALUE
    def setBinaryValue(self,P_Value):
        self.__BinaryValue = P_Value

    def getBinaryValue(self):
        return self.__BinaryValue
#**********************************************************************
    #BINARY_VALUE_LENGTH
    def setBinaryValueLength(self,BinL):
        self.__BinaryValueLength = BinL

    def getBinaryValueLength(self):
        return self.__BinaryValueLength
 #**********************************************************************
    #DOUBLE_VALUE
    def setDoubleValue(self,DoubleValue):
        self.__DoubleValue = DoubleValue

    def getDoubleValue(self):
        return self.__DoubleValue
 #**********************************************************************
