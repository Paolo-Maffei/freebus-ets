#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ParameterType.py
#Version: V0.1 , 13.06.2008
#Version: V0.2 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_ParameterType:

      #local variables of Parameter Type Node
    __ParameterTypeID2 = 0            #PARAMETER_TYPE_ID
    __AtomicTypeNumber = 0            #ATOMIC_TYPE_NUMBER
    __ProgramID2 = 0                  #PROGRAM_ID
    __ParameterTypeName = ""          #PARAMETER_TYPE_NAME
    __Parameter_Min_Value = 0         #PARAMETER_MINIMUM_VALUE            NEU
    __Parameter_Max_Value = 0         #PARAMETER_MAXIMUM_VALUE            NEU
    __Parameter_Type_Description = "" #PARAMETER_TYPE_DESCRIPTION         NEU
    __ParameterTypeLowAccess = 0      #PARAMETER_TYPE_LOW_ACCESS
    __ParameterTypeHighAccess = 0     #PARAMETER_TYPE_HIGH_ACCESS
    __ParameterTypeSize = 0           #PARAMETER_TYPE_SIZE
    __Parameter_MinDouble_Value = 0.0 #PARAMETER_MINIMUM_DOUBLE_VALUE    NEU
    __Parameter_MaxDouble_Value = 0.0 #PARAMETER_MAXIMUM_DOUBLE_VALUE    NEU
    __Parameter_UI_HINT = ""          #PARAMETER_UI_HINT                 NEU

    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):


        List = (self.__ParameterTypeID2,self.__AtomicTypeNumber,self.__ProgramID2,self.__ParameterTypeName,
                self.__Parameter_Min_Value, self.__Parameter_Max_Value, self.__Parameter_Type_Description,
                self.__ParameterTypeLowAccess,self.__ParameterTypeHighAccess,self.__ParameterTypeSize,
                self.__Parameter_MinDouble_Value, self.__Parameter_MaxDouble_Value, self.__Parameter_UI_HINT)

        return List
#---------------------------------------------------------------------------------
#----------------------- Parameter Handling --------------------------------------
#---------------------------------------------------------------------------------

    #general set and get property with index for each element, coresponds to FB_Constants

#----------------------- Parameter Type Handling --------------------------------------
    def setParameterType(self,Index, Value):
        if(Index == 1):
            self.__ParameterTypeID2 = Value
        elif(Index == 2):
            self.__AtomicTypeNumber = Value
        elif(Index == 3):
            self.__ProgramID2 = Value
        elif(Index == 4):
            self.__ParameterTypeName = Value
        elif(Index == 5):
            self.__Parameter_Min_Value = Value
        elif(Index == 6):
            self.__Parameter_Max_Value = Value
        elif(Index == 7):
            self.__Parameter_Type_Description = Value
        elif(Index == 8):
            self.__ParameterTypeLowAccess = Value
        elif(Index == 9):
            self.__ParameterTypeHighAccess = Value
        elif(Index == 10):
            self.__ParameterTypeSize = Value
        elif(Index == 11):
            self.__Parameter_MinDouble_Value = Value
        elif(Index == 12):
            self.__Parameter_MaxDouble_Value = Value
        elif(Index == 13):
            self.__Parameter_UI_HINT = Value


    def getParameterType(self,Index):
        if(Index == 1):
            return self.__ParameterTypeID2
        elif(Index == 2):
            return self.__AtomicTypeNumber
        elif(Index == 3):
            return self.__ProgramID2
        elif(Index == 4):
            return self.__ParameterTypeName
        elif(Index == 5):
            return self.__Parameter_Min_Value
        elif(Index == 6):
            return self.__Parameter_Max_Value
        elif(Index == 7):
            return self.__Parameter_Type_Description
        elif(Index == 8):
            return self.__ParameterTypeLowAccess
        elif(Index == 9):
            return self.__ParameterTypeHighAccess
        elif(Index == 10):
            return self.__ParameterTypeSize
        elif(Index == 11):
            return self.__Parameter_MinDouble_Value
        elif(Index == 12):
            return self.__Parameter_MaxDouble_Value
        elif(Index == 13):
            return self.__Parameter_UI_HINT

#---------------------------------------------------------------------------------
#----------------------- Parameter Type Handling --------------------------------------
#---------------------------------------------------------------------------------
#**********************************************************************
   #Handling PARAMETER_TYPE_ID
    def setParameterTypeID2(self,PT_ID2):
        self.__ParameterTypeID2 = PT_ID2

    def getParameterTypeID2(self):
        return self.__ParameterTypeID2

#**********************************************************************
    #ATOMIC_TYPE_NUMBER
    def setAtomicTypeNumber(self,AtomicNo):
        self.__AtomicTypeNumber = AtomicNo

    def getAtomicTypeNumber(self):
        return self.__AtomicTypeNumber

#**********************************************************************
    #PROGRAM_ID
    def setProgramID2(self,P_ID2):
        self.__ProgramID2 = P_ID2

    def getProgramID2(self):
        return self.__ProgramID2

#**********************************************************************
    #PARAMETER_TYPE_NAME
    def setParameterTypeName(self,P_TypeName):
        self.__ParameterTypeName = P_TypeName

    def getParameterTypeName(self):
        return self.__ParameterTypeName

#**********************************************************************
    #PARAMETER_MINIMUM_VALUE
    def setParameterMinValue(self,P_MinValue):
        self.__Parameter_Min_Value = P_MinValue

    def getParameterMinValue(self):
        return self.__Parameter_Min_Value
#**********************************************************************
    #PARAMETER_MAXIMUM_VALUE
    def setParameterMaxValue(self,P_MaxValue):
        self.__Parameter_Max_Value = P_MaxValue

    def getParameterMaxValue(self):
        return self.__Parameter_Max_Value
#**********************************************************************
    #PARAMETER_TYPE_DESCRIPTION
    def setParameterTypeDescription(self,P_TypeDescr):
        self.__Parameter_Type_Description = P_TypeDescr

    def getParameterTypeDescription(self):
        return self.__Parameter_Type_Description

#**********************************************************************
    #PARAMETER_TYPE_LOW_ACCESS
    def setParameterTypeLow(self,P_TLow):
        self.__ParameterTypeLowAccess = P_TLow

    def getParameterTypeLow(self):
        return self.__ParameterTypeLowAccess
#**********************************************************************
    #PARAMETER_TYPE_HIGH_ACCESS
    def setParameterTypeHigh(self,P_THigh):
        self.__ParameterTypeHighAccess = P_THigh

    def getParameterTypeHigh(self):
        return self.__ParameterTypeHighAccess
 #**********************************************************************
    #PARAMETER_TYPE_SIZE
    def setParameterTypeSize(self,P_TSize):
        self.__ParameterTypeSize = P_TSize

    def getParameterTypeSize(self):
        return self.__ParameterTypeSize
 #**********************************************************************
    #PARAMETER_MINIMUM_DOUBLE_VALUE
    def setParameterMinDoubleValue(self,P_MinDoubleValue):
        self.__Parameter_MinDouble_Value = P_MinDoubleValue

    def getParameterMinDoubleValue(self):
        return self.__Parameter_MinDouble_Value
 #**********************************************************************
    #PARAMETER_MAXIMUM_DOUBLE_VALUE
    def setParameterMaxDoubleValue(self,P_MaxDoubleValue):
        self.__Parameter_MaxDouble_Value = P_MaxDoubleValue

    def getParameterMaxDoubleValue(self):
        return self.__Parameter_MaxDouble_Value
 #**********************************************************************
    #PARAMETER_UI_HINT
    def setParameterUIHint(self,P_UIHint):
        self.__Parameter_UI_HINT = P_UIHint

    def getParameterUIHint(self):
        return self.__Parameter_UI_HINT
 #**********************************************************************


