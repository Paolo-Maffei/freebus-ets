#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_Parameter.py
#Version: V0.1 , 12.06.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Product-Data which based from FB XML Product-Files
class FB_Parameter:

    #local variables of Parameter block
    __ProgramID = 0            #PROGRAM_ID
    __ParameterTypeID = 0      #PARAMETER_TYPE_ID
    __ParameterNumber = 0      #PARAMETER_NUMBER
    __ParameterName = ""       #PARAMETER_NAME
    __ParameterLowAccess = 0   #PARAMETER_LOW_ACCESS
    __ParameterHighAccess = 0  #PARAMETER_HIGH_ACCESS
    __ParameterSize = 0        #PARAMETER_SIZE
    __ParameterDisplayOrder = 0 #PARAMETER_DISPLAY_ORDER
    __ParameterAddress = 0     #PARAMETER_ADDRESS
    __ParameterBitOffset = 0   #PARAMETER_BITOFFSET
    __ParameterDescription = ""#PARAMETER_DESCRIPTION
    __ParameterID = 0          #PARAMETER_ID
    __ParParameterID = 0       #PAR_PARAMETER_ID
    __ParameterDefault = 0     #PARAMETER_DEFAULT_LONG
    __PatchAlways = 0          #PATCH_ALWAYS
    __AddressSpace = 0         #ADDRESS_SPACE


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = "VALUES(" +  str(self.__ProgramID)       + "," + \
                             str(self.__ParameterTypeID) + "," + \
                             str(self.__ParameterNumber) + "," + "'" + \
                             self.__ParameterName        + "'" + "," + \
                             str(self.__ParameterLowAccess)  + "," + \
                             str(self.__ParameterHighAccess) + "," + \
                             str(self.__ParameterSize)       + "," + \
                             str(self.__ParameterDisplayOrder)  + "," + \
                             str(self.__ParameterAddress)       + "," + \
                             str(self.__ParameterBitOffset)     + "," + "'" + \
                             self.__ParameterDescription  + "'" + "," + \
                             str(self.__ParameterID)      + "," + \
                             str(self.__ParParameterID)   + "," + \
                             str(self.__ParameterDefault) + "," + \
                             str(self.__PatchAlways)      + "," + \
                             str(self.__AddressSpace)     + ");"


        return List
#---------------------------------------------------------------------------------
#----------------------- Parameter Handling --------------------------------------
#---------------------------------------------------------------------------------

    #general set and get property with index for each element, coresponds to FB_Constants
    def setParameter(self,Index, Value):
        if(Index == 1):
            self.__ProgramID = Value
        elif(Index == 2):
            self.__ParameterTypeID = Value
        elif(Index == 3):
            self.__ParameterNumber = Value
        elif(Index == 4):
            self.__ParameterName = Value
        elif(Index == 5):
            self.__ParameterLowAccess = Value
        elif(Index == 6):
            self.__ParameterHighAccess = Value
        elif(Index == 7):
            self.__ParameterSize = Value
        elif(Index == 8):
            self.__ParameterDisplayOrder = Value
        elif(Index == 9):
            self.__ParameterAddress = Value
        elif(Index == 10):
            self.__ParameterBitOffset = Value
        elif(Index == 11):
            self.__ParameterDescription = Value
        elif(Index == 12):
            self.__ParameterID = Value
        elif(Index == 13):
            self.__ParParameterID = Value
        elif(Index == 14):
            self.__ParameterDefault = Value
        elif(Index == 15):
            self.__PatchAlways = Value
        elif(Index == 16):
            self.__AddressSpace = Value

    def getParameter(self,Index):
         if(Index == 1):
            return self.__ProgramID
         elif(Index == 2):
            return self.__ParameterTypeID
         elif(Index == 3):
            return self.__ParameterNumber
         elif(Index == 4):
            return self.__ParameterName
         elif(Index == 5):
            return self.__ParameterLowAccess
         elif(Index == 6):
            return self.__ParameterHighAccess
         elif(Index == 7):
            return self.__ParameterSize
         elif(Index == 8):
            return self.__ParameterDisplayOrder
         elif(Index == 9):
            return self.__ParameterAddress
         elif(Index == 10):
            return self.__ParameterBitOffset
         elif(Index == 11):
            return self.__ParameterDescription
         elif(Index == 12):
            return self.__ParameterID
         elif(Index == 13):
            return self.__ParParameterID
         elif(Index == 14):
            return self.__ParameterDefault
         elif(Index == 15):
            return self.__PatchAlways
         elif(Index == 16):
            return self.__AddressSpace


    #returns the maximum index of all three parts
    def getMaxIndex(self):
        return 16

#**********************************************************************
    #Handling PROGRAM_ID
    def setProgramID(self,P_ID):
        self.__ProgramID = P_ID

    def getProgramID(self):
        return self.__ProgramID
#**********************************************************************
    #Handling PARAMETER_TYPE_ID
    def setParameterTypeID(self,ParamT_ID):
        self.__ParameterTypeID = ParamT_ID

    def getParameterTypeID(self):
        return self.__ParameterTypeID

#**********************************************************************
    #Handling PARAMETER_NUMBER
    def setParameterNumber(self,P_Number):
        self.__ParameterNumber = P_Number

    def getParameterNumber(self):
        return self.__ParameterNumber

#**********************************************************************
    #Handling PARAMETER_NAME
    def setParameterName(self,P_Name):
        self.__ParameterName = P_Name

    def getParameterName(self):
        return self.__ParameterName

#**********************************************************************
    #Handling PARAMETER_LOW_ACCESS
    def setParameterLow(self,P_Low):
        self.__ParameterLowAccess = P_Low

    def getParameterLow(self):
        return self.__ParameterLowAccess

#**********************************************************************
    #Handling PARAMETER_HIGH_ACCESS
    def setParameterHigh(self,P_High):
        self.__ParameterHighAccess = P_High

    def getParameterHigh(self):
        return self.__ParameterHighAccess

#**********************************************************************
    #Handling PARAMETER_SIZE
    def setParameterSize(self,P_Size):
        self.__ParameterSize = P_Size

    def getParameterSize(self):
        return self.__ParameterSize

#**********************************************************************
    #Handling PARAMETER_DISPLAY_ORDER
    def setParameterDisplayOrder(self,P_DisplayO):
        self.__ParameterDisplayOrder = P_DisplayO

    def getParameterDisplayOrder(self):
        return self.__ParameterDisplayOrder

#**********************************************************************
    #Handling PARAMETER_ADDRESS
    def setParameterAddress(self,P_Address):
        self.__ParameterAddress = P_Address

    def getParameterAddress(self):
        return self.__ParameterAddress

#**********************************************************************
   #Handling PARAMETER_BITOFFSET
    def setParameterBitOffset(self,P_Offset):
        self.__ParameterBitOffset  = P_Offset

    def getParameterBitOffset(self):
        return self.__ParameterBitOffset

#**********************************************************************
   #Handling PARAMETER_DESCRIPTION
    def setParameterDescription(self,P_Descr):
        self.__ParameterDescription = P_Descr

    def getParameterDescription(self):
        return self.__ParameterDescription

#**********************************************************************
    #PARAMETER_ID
    def setParameterID(self,Param_ID):
        self.__ParameterID = Param_ID

    def getParameterID(self):
        return self.__ParameterID

#**********************************************************************
    #PAR_PARAMETER_ID
    def setParParameterID(self,PP_ID):
        self.__ParParameterID = PP_ID

    def getParParameterID(self):
        return self.__ParParameterID

#**********************************************************************
    #PARAMETER_DEFAULT_LONG
    def setParameterDefault(self,P_Default):
        self.__ParameterDefault = P_Default

    def getParameterDefault(self):
        return self.__ParameterDefault

#**********************************************************************
    #PATCH_ALWAYS
    def setPatchAlways(self,Patch):
        self.__PatchAlways = Patch

    def getPatchAlways(self):
        return self.__PatchAlways
#**********************************************************************
    #ADDRESS_SPACE
    def setAddressSpace(self,A_Space):
        self.__AddressSpace = A_Space

    def getAddressSpace(self):
        return self.__AddressSpace
 #**********************************************************************

