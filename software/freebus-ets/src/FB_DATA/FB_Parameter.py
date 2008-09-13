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
#Version: V0.2 , 20.07.2008
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
    __ParentParmValue = 0      #PARENT_PARM_VALUE             NEU
    __ParameterSize = 0        #PARAMETER_SIZE
    __ParameterFunction = ""   #PARAMETER_FUNCTION            NEU
    __ParameterDisplayOrder = 0 #PARAMETER_DISPLAY_ORDER
    __ParameterAddress = 0     #PARAMETER_ADDRESS
    __ParameterBitOffset = 0   #PARAMETER_BITOFFSET
    __ParameterDescription = ""#PARAMETER_DESCRIPTION
    __ParameterID = 0          #PARAMETER_ID
    __ParParameterID = 0       #PAR_PARAMETER_ID
    __ParameterLabel = ""      #PARAMETER_LABEL                NEU
    __ParameterDefaultLong = 0 #PARAMETER_DEFAULT_LONG
    __ParameterDefaultStr = "" #PARAMETER_DEFAULT_STRING       NEU
    __Context_ID = 0           #CONTEXT_ID                     NEU
    __ParameterDefaultDouble = 0.0 #PARAMETER_DEFAULT_DOUBLE   NEU
    __PatchAlways = 0          #PATCH_ALWAYS
    __AddressSpace = 0         #ADD ESS_SPACE
    __EIB_Object_Ref = 0       #EIB_OBJECT_REF                 NEU
    __EIB_Property_ID = 0      #EIB_PROPERTY_ID                NEU
    __CalculationID = 0        #CalculationID                  NEU
    __CalculationSet = ""      #CalculationSet                 NEU
    __AliasName = ""           #AliasName                      NEU


    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__ProgramID,self.__ParameterTypeID,self.__ParameterNumber,self.__ParameterName,
                self.__ParameterLowAccess,self.__ParameterHighAccess,self.__ParentParmValue, self.__ParameterSize,
                self.__ParameterFunction, self.__ParameterDisplayOrder, self.__ParameterAddress,self.__ParameterBitOffset,
                self.__ParameterDescription,self.__ParameterID,self.__ParParameterID, self.__ParameterLabel,
                self.__ParameterDefaultLong, self.__ParameterDefaultStr, self.__Context_ID, self.__ParameterDefaultDouble,
                self.__PatchAlways,self.__AddressSpace, self.__EIB_Object_Ref, self.__EIB_Property_ID, self.__CalculationID,
                self.__CalculationSet, self.__AliasName)


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
            self.__ParentParmValue = Value
        elif(Index == 8):
            self.__ParameterSize = Value
        elif(Index == 9):
            self.__ParameterFunction = Value
        elif(Index == 10):
            self.__ParameterDisplayOrder = Value
        elif(Index == 11):
            self.__ParameterAddress = Value
        elif(Index == 12):
            self.__ParameterBitOffset = Value
        elif(Index == 13):
            self.__ParameterDescription = Value
        elif(Index == 14):
            self.__ParameterID = Value
        elif(Index == 15):
            self.__ParParameterID = Value
        elif(Index == 16):
            self.__ParameterLabel = Value
        elif(Index == 17):
            self.__ParameterDefaultLong = Value
        elif(Index == 18):
            self.__ParameterDefaultStr = Value
        elif(Index == 19):
            self.__Context_ID = Value
        elif(Index == 20):
            self.__ParameterDefaultDouble = Value
        elif(Index == 21):
            self.__PatchAlways = Value
        elif(Index == 22):
            self.__AddressSpace = Value
        elif(Index == 23):
            self.__EIB_Object_Ref = Value
        elif(Index == 24):
            self.__EIB_Property_ID = Value
        elif(Index == 25):
            self.__CalculationID = Value
        elif(Index == 26):
            self.__CalculationSet = Value
        elif(Index == 27):
            self.__AliasName = Value


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
            return self.__ParentParmValue
        elif(Index == 8):
            return self.__ParameterSize
        elif(Index == 9):
            return self.__ParameterFunction
        elif(Index == 10):
            return self.__ParameterDisplayOrder
        elif(Index == 11):
            return self.__ParameterAddress
        elif(Index == 12):
            return self.__ParameterBitOffset
        elif(Index == 13):
            return self.__ParameterDescription
        elif(Index == 14):
            return self.__ParameterID
        elif(Index == 15):
            return self.__ParParameterID
        elif(Index == 16):
            return self.__ParameterLabel
        elif(Index == 17):
            return self.__ParameterDefaultLong
        elif(Index == 18):
            return self.__ParameterDefaultStr
        elif(Index == 19):
            return self.__Context_ID
        elif(Index == 20):
            return self.__ParameterDefaultDouble
        elif(Index == 21):
            return self.__PatchAlways
        elif(Index == 22):
            return self.__AddressSpace
        elif(Index == 23):
            return self.__EIB_Object_Ref
        elif(Index == 24):
            return self.__EIB_Property_ID
        elif(Index == 25):
            return self.__CalculationID
        elif(Index == 26):
            return self.__CalculationSet
        elif(Index == 27):
            return self.__AliasName


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
    #PARENT_PARM_VALUE
    def setParentParmValue(self,P_ParmValue):
        self.__ParentParmValue = P_ParmValue

    def getParentParmValue(self):
        return self.__ParentParmValue
#**********************************************************************
    #Handling PARAMETER_SIZE
    def setParameterSize(self,P_Size):
        self.__ParameterSize = P_Size

    def getParameterSize(self):
        return self.__ParameterSize

#**********************************************************************
    #PARAMETER_FUNCTION
    def setParameterFunction(self,P_Function):
        self.__ParameterFunction = P_Function

    def getParameterFunction(self):
        return self.__ParameterFunction

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
    #PARAMETER_LABEL
    def setParameterLabel(self,P_Label):
        self.__ParameterLabel = P_Label

    def getParameterLabel(self):
        return self.__ParameterLabel

#**********************************************************************
    #PARAMETER_DEFAULT_LONG
    def setParameterDefaultLong(self,P_DefaultL):
        self.__ParameterDefaultLong = P_DefaultL

    def getParameterDefaultLong(self):
        return self.__ParameterDefaultLong

#**********************************************************************
    #PARAMETER_DEFAULT_STRING
    def setParameterDefaultString(self,P_DefaultStr):
        self.__ParameterDefaultStr = P_DefaultStr

    def getParameterDefaultString(self):
        return self.__ParameterDefaultStr

#**********************************************************************
    #CONTEXT_ID
    def setContextID(self,ContextID):
        self.__Context_ID = ContextID

    def getContextID(self):
        return self.__Context_ID
#**********************************************************************
    #PARAMETER_DEFAULT_DOUBLE
    def setParameterDefaultDouble(self,P_DefaultDouble):
        self.__ParameterDefaultDouble = P_DefaultDouble

    def getParameterDefaultDouble(self):
        return self.__ParameterDefaultDouble
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
    #EIB_OBJECT_REF
    def setEIBObjRef(self,EIB_ObjRef):
        self.__EIB_Object_Ref = EIB_ObjRef

    def getEIBObjRef(self):
        return self.__EIB_Object_Ref
 #**********************************************************************
    #EIB_PROPERTY_ID
    def setEIBPropertyID(self,EIB_PropID):
        self.__EIB_Property_ID = EIB_PropID

    def getEIBPropertyID(self):
        return self.__EIB_Property_ID
#**********************************************************************
    #CalculationID
    def setCalculationID(self,CalcID):
        self.__CalculationID = CalcID

    def getCalculationID(self):
        return self.__CalculationID
 #**********************************************************************
    #CalculationSet
    def setCalculationSet(self,CalcSet):
        self.__CalculationSet = CalcSet

    def getCalculationSet(self):
        return self.__CalculationSet
 #**********************************************************************
   #AliasName
    def setAliasName(self,AliasName):
        self.__AliasName = AliasName

    def getAliasName(self):
        return self.__AliasName
 #**********************************************************************
