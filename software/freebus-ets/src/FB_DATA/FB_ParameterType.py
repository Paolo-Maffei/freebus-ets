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
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_ParameterType:

      #local variables of Parameter Type Node
    __ParameterTypeID2 = 0        #PARAMETER_TYPE_ID
    __AtomicTypeNumber = 0        #ATOMIC_TYPE_NUMBER
    __ProgramID2 = 0               #PROGRAM_ID
    __ParameterTypeName = ""      #PARAMETER_TYPE_NAME
    __ParameterTypeLowAccess = 0  #PARAMETER_TYPE_LOW_ACCESS
    __ParameterTypeHighAccess = 0 #PARAMETER_TYPE_HIGH_ACCESS
    __ParameterTypeSize = 0       #PARAMETER_TYPE_SIZE


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):


        List = "VALUES(" +  str(self.__ParameterTypeID2) + "," + \
                             str(self.__AtomicTypeNumber) + "," + \
                             str(self.__ProgramID2)       + "," + "'" + \
                             self.__ParameterTypeName     + "'" + "," + \
                             str(self.__ParameterTypeLowAccess)  + "," + \
                             str(self.__ParameterTypeHighAccess) + "," + \
                             str(self.__ParameterTypeSize)       + ");"


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
            self.__ParameterTypeLowAccess = Value
        elif(Index == 6):
            self.__ParameterTypeHighAccess = Value
        elif(Index == 7):
            self.__ParameterTypeSize = Value

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
            return self.__ParameterTypeLowAccess
        elif(Index == 6):
            return self.__ParameterTypeHighAccess
        elif(Index == 7):
            return self.__ParameterTypeSize

    #returns the maximum index of all three parts
    def getMaxIndex(self):
        return 7

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
