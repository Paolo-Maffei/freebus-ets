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
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_ParameterListV:

    #local variables ParameterList of values
    __ParameterTypeID3 = 0        #PARAMETER_TYPE_ID
    __RealValue = 0               #REAL_VALUE
    __DisplayValue = 0            #DISPLAYED_VALUE
    __DisplayOrder = 0            #DISPLAY_ORDER
    __ParameterValueID = 0        #PARAMETER_VALUE_ID
    __BinaryValueLength = 0       #BINARY_VALUE_LENGTH


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = "VALUES(" +  str(self.__ParameterTypeID3)  + "," + \
                             str(self.__RealValue)         + "," + \
                             str(self.__DisplayValue)      + "," + \
                             str(self.__DisplayOrder)      + "," + \
                             str(self.__ParameterValueID)  + "," + \
                             str(self.__BinaryValueLength) + ");"




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
            self.__BinaryValueLength = Value

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
            return self.__BinaryValueLength


    #returns the maximum index of all three parts
    def getMaxIndex(self):
        return 6

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
    #BINARY_VALUE_LENGTH
    def setBinaryValueLength(self,BinL):
        self.__BinaryValueLength = BinL

    def getBinaryValueLength(self):
        return self.__BinaryValueLength
 #**********************************************************************