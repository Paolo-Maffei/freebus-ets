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
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Comm-Objects-Data which based from FB XML Product-Files
class FB_CommObj:

    __ProgID = ""           #PROGRAM_ID
    __ObjName = ""          #OBJECT_NAME
    __ObjFunction = ""      #OBJECT_FUNCTION
    __ObjReadEnabled = ""   #OBJECT_READENABLED
    __ObjWriteEnabled = ""  #OBJECT_WRITEENABLED
    __ObjCommEnabled = ""   #OBJECT_COMMENABLED
    __ObjTransEnabled = ""  #OBJECT_TRANSENABLED
    __ObjDisplayOrder = ""  #OBJECT_DISPLAY_ORDER
    __ParentParamValue = "" #PARENT_PARAMETER_VALUE
    __ObjID = ""            #OBJECT_ID
    __ParamID = ""          #PARAMETER_ID
    __ObjNumber = ""        #OBJECT_NUMBER
    __ObjType = ""          #OBJECT_TYPE
    __ObjPriority = ""      #OBJECT_PRIORITY
    __ObjUpdateEnabled = "" #OBJECT_UPDATEENABLED
    __ObjUniqueNumber = ""  #OBJECT_UNIQUE_NUMBER

    def __init__(self):
        #print "okk"
        pass

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



