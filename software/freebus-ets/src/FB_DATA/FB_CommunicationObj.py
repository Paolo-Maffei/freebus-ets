#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source Datei: FB_CommunicationObj.py
#Version: V0.1 , 31.12.2007
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Comm-Objects-Data which based from FB XML Product-Files
class FB_CommObj:

    __ProgID = 0           #PROGRAM_ID
    __ObjName = ""          #OBJECT_NAME
    __ObjFunction = ""      #OBJECT_FUNCTION
    __ObjReadEnabled = 0   #OBJECT_READENABLED
    __ObjWriteEnabled = 0  #OBJECT_WRITEENABLED
    __ObjCommEnabled = 0   #OBJECT_COMMENABLED
    __ObjTransEnabled = 0  #OBJECT_TRANSENABLED
    __ObjDisplayOrder = 0  #OBJECT_DISPLAY_ORDER
    __ParentParamValue = 0 #PARENT_PARAMETER_VALUE
    __ObjID = 0            #OBJECT_ID
    __ParamID = 0          #PARAMETER_ID
    __ObjNumber = 0        #OBJECT_NUMBER
    __ObjDescription = ""  #OBJECT_DESCRIPTION    NEU
    __ObjType = 0          #OBJECT_TYPE
    __ObjPriority = 0      #OBJECT_PRIORITY
    __ObjUpdateEnabled = 0 #OBJECT_UPDATEENABLED
    __ObjUniqueNumber = 0  #OBJECT_UNIQUE_NUMBER
    __EIBDataTypeCode = 0  #EIB_DATA_TYPE_CODE        NEU
    __EIBDataSubTypeCode = 0 #EIB_DATA_SUBTYPE_CODE   NEU
    __ObjReadOnInitEN = 0  #OBJECT_READONINITENABLED  NEU

    __return = None


    def __init__(self):
        #print "okk"
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__ProgID, self.__ObjName, self.__ObjFunction, self.__ObjReadEnabled, self.__ObjWriteEnabled,
                self.__ObjCommEnabled, self.__ObjTransEnabled, self.__ObjDisplayOrder, self.__ParentParamValue,
                self.__ObjID, self.__ParamID, self.__ObjNumber,self.__ObjDescription ,self.__ObjType, self.__ObjPriority, self.__ObjUpdateEnabled,
                self.__ObjUniqueNumber,self.__EIBDataTypeCode,self.__EIBDataSubTypeCode, self.__ObjReadOnInitEN)

        return List


    def setCommObj(self,Index, Value):

        if(Index == 1):
            self.__ProgID = Value
        elif(Index == 2):
            self.__ObjName = Value
        elif(Index == 3):
            self.__ObjFunction = Value
        elif(Index == 4):
            self.__ObjReadEnabled = Value
        elif(Index == 5):
            self.__ObjWriteEnabled = Value
        elif(Index == 6):
            self.__ObjCommEnabled = Value
        elif(Index == 7):
            self.__ObjTransEnabled = Value
        elif(Index == 8):
            self.__ObjDisplayOrder = Value
        elif(Index == 9):
            self.__ParentParamValue = Value
        elif(Index == 10):
            self.__ObjID = Value
        elif(Index == 11):
            self.__ParamID = Value
        elif(Index == 12):
            self.__ObjNumber = Value
        elif(Index == 13):
            self.__ObjDescription = Value
        elif(Index == 14):
            self.__ObjType = Value
        elif(Index == 15):
            self.__ObjPriority = Value
        elif(Index == 16):
            self.__ObjUpdateEnabled = Value
        elif(Index == 17):
            self.__ObjUniqueNumber = Value
        elif(Index == 18):
            self.__EIBDataTypeCode = Value
        elif(Index == 19):
            self.__EIBDataSubTypeCode = Value
        elif(Index == 20):
            self.__ObjReadOnInitEN = Value


    def getCommObj(self,Index):
        if(Index == 1):
            return self.__ProgID
        elif(Index == 2):
            return self.__ObjName
        elif(Index == 3):
            return self.__ObjFunction
        elif(Index == 4):
            return self.__ObjReadEnabled
        elif(Index == 5):
            return self.__ObjWriteEnabled
        elif(Index == 6):
            return self.__ObjCommEnabled
        elif(Index == 7):
            return self.__ObjTransEnabled
        elif(Index == 8):
            return self.__ObjDisplayOrder
        elif(Index == 9):
            return self.__ParentParamValue
        elif(Index == 10):
            return self.__ObjID
        elif(Index == 11):
            return self.__ParamID
        elif(Index == 12):
            return self.__ObjNumber
        elif(Index == 13):
            return self.__ObjDescription
        elif(Index == 14):
            return self.__ObjType
        elif(Index == 15):
            return self.__ObjPriority
        elif(Index == 16):
            return self.__ObjUpdateEnabled
        elif(Index == 17):
            return self.__ObjUniqueNumber
        elif(Index == 18):
            return self.__EIBDataTypeCode
        elif(Index == 19):
            return self.__EIBDataSubTypeCode
        elif(Index == 20):
            return self.__ObjReadOnInitEN

#**********************************************************************
    #Handling PROGRAM_ID
    def setProgramID(self,P_ID):
        self.__ProgID = P_ID

    def getProgramID(self):
        return self.__ProgID
#**********************************************************************
    #Handling OBJECT_NAME
    def setObjName(self,O_Name):
        self.__ObjName = O_Name

    def getObjName(self):
        return self.__ObjName

#**********************************************************************
    #Handling OBJECT_FUNCTION
    def setObjFunction(self,ObjFct):
        self.__ObjFunction = ObjFct

    def getObjFunction(self):
        return self.__ObjFunction

#**********************************************************************
    #Handling OBJECT_READENABLED
    def setObjReadEN(self,R_EN):
        self.__ObjReadEnabled = R_EN

    def getObjReadEN(self):
        return self.__ObjReadEnabled

#**********************************************************************
    #Handling OBJECT_WRITEENABLED
    def setObjWriteEN(self,W_EN):
        self.__ObjWriteEnabled = W_EN

    def getObjWriteEN(self):
        return self.__ObjWriteEnabled

#**********************************************************************
    #Handling OBJECT_COMMENABLED
    def setObjCommEN(self,C_EN):
        self.__ObjCommEnabled = C_EN

    def getObjCommEN(self):
        return self.__ObjCommEnabled

#**********************************************************************
    #Handling OBJECT_TRANSENABLED
    def setObjTransEN(self,T_EN):
        self.__ObjTransEnabled = T_EN

    def getObjTransEN(self):
        return self.__ObjTransEnabled

#**********************************************************************
    # OBJECT_DISPLAY_ORDER
    def setObjDisplOrder(self,DisOrder):
        self.__ObjDisplayOrder = DisOrder

    def getObjDisplOrder(self):
        return self.__ObjDisplayOrder

#**********************************************************************
    # PARENT_PARAMETER_VALUE
    def setParentParaValue(self,PP_Value):
        self.__ParentParamValue = PP_Value

    def getParentParaValue(self):
        return self.__ParentParamValue

#**********************************************************************
    #OBJECT_ID
    def setObjID(self,O_ID):
        self.__ObjID = O_ID

    def getObjID(self):
        return self.__ObjID

#**********************************************************************
    #PARAMETER_ID
    def setParaID(self,P_ID):
        self.__ParamID = P_ID

    def getParaID(self):
        return self.__ParamID

#**********************************************************************
    #OBJECT_NUMBER
    def setObjNumber(self,O_No):
        self.__ObjNumber = O_No

    def getObjNumber(self):
        return self.__ObjNumber

#**********************************************************************
    #OBJECT_DESCRIPTION
    def setObjDescription(self,O_Des):
        self.__ObjDescription = O_Des

    def getObjDescription(self):
        return self.__ObjDescription

#**********************************************************************
    #OBJECT_TYPE
    def setObjType(self,O_Type):
        self.__ObjType = O_Type

    def getObjType(self):
        return self.__ObjType

#**********************************************************************
    #OBJECT_PRIORITY
    def setObjPriority(self,O_Prio):
        self.__ObjPriority = O_Prio

    def getObjPriority(self):
        return self.__ObjPriority

#**********************************************************************
    #OBJECT_UPDATEENABLED
    def setObjUpdateEN(self,O_Up_EN):
        self.__ObjUpdateEnabled = O_Up_EN

    def getObjUpdateEN(self):
        return self.__ObjUpdateEnabled

#**********************************************************************
    #OBJECT_UNIQUE_NUMBER
    def setObjUniqueNo(self,O_UN_No):
        self.__ObjUniqueNumber = O_UN_No

    def getObjUniqueNo(self):
        return self.__ObjUniqueNumber

#**********************************************************************
    #EIB_DATA_TYPE_CODE
    def setEIBDataTypeCode(self,EIBTypeCode):
        self.__EIBDataTypeCode = EIBTypeCode

    def getEIBDataTypeCode(self):
        return self.__EIBDataTypeCode

#**********************************************************************
   #EIB_DATA_SUBTYPE_CODE
    def setEIBDataSubTypeCode(self,EIBSubTypeCode):
        self.__EIBDataSubTypeCode = EIBSubTypeCode

    def getEIBDataSubTypeCode(self):
        return self.__EIBDataSubTypeCode

#**********************************************************************
  #OBJECT_READONINITENABLED
    def setObjReadOnInitEN(self,O_ReadEN):
        self.__ObjReadOnInitEN = O_ReadEN

    def getObjReadOnInitEN(self):
        return self.__ObjReadOnInitEN

#**********************************************************************



