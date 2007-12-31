#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source Datei: FB_Product.py
#Version: V0.1 , 17.11.2007
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Application-Data which based from FB XML Product-Files
class FB_Apps:

    __ProgID = ""       #PROGRAM_ID
    __SymbolID = ""     #SYMBOL_ID
    __MaskID = ""       #MASK_ID
    __ProgName = ""     #PROGRAM_NAME
    __ProgVersion = ""  #PROGRAM_VERSION
    __ProgVersionNo = ""#PROGRAM_VERSION_NUMBER
    __Linkable = ""     #LINKABLE
    __DevType = ""      #DEVICE_TYPE
    __PEIType = ""      #PEI_TYPE
    __AddTabsize = ""   #ADDRESS_TAB_SIZE
    __AssTabAddr = ""   #ASSOCTAB_ADDRESS
    __AssTsize = ""     #ASSOCTAB_SIZE
    __ComTabAddr = ""   #COMMSTAB_ADDRESS
    __ComTabsize = ""   #COMMSTAB_SIZE
    __ProgSN = ""       #PROGRAM_SERIAL_NUMBER
    __AppManID = ""     #MANUFACTURER_ID
    __EEPROMData = ""   #EEPROM_DATA
    __DataLength = ""   #DATA_LENGTH
    __S19File = ""      #S19_FILE
    __MapFile = ""      #MAP_FILE
    __AssemblerID = ""  #ASSEMBLER_ID
    __HelpFileName = "" #HELP_FILE_NAME
    __ContextID = ""    #CONTEXT_ID
    __DynamicMng = ""   #DYNAMIC_MANAGEMENT
    __ProgType = ""     #PROGRAM_TYPE
    __RAMSize = ""      #RAM_SIZE
    __OrgManID = ""     #ORIGINAL_MANUFACTURER_ID
    __APIVersion = ""   #API_VERSION
    __ProgStyle = ""    #PROGRAM_STYLE
    __PollMaster = ""   #IS_POLLING_MASTER
    __NoPollGroups = "" #NUMBER_OF_POLLING_GROUPS
    __AllowedInETS = "" #AllowedInSimpleEts
    __MinEtsVersion = ""#MinEtsVersion

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
    #Handling SYMBOL_ID
    def setSymbolID(self,S_ID):
        self.__SymbolID = S_ID

    def getSymbolID(self):
        return self.__SymbolID

#**********************************************************************
    #Handling MASK_ID
    def setMaskID(self,Mask):
        self.__MaskID = Mask

    def getMaskID(self):
        return self.__MaskID

#**********************************************************************
    #Handling PROGRAM_NAME
    def setProgramName(self,P_Name):
        self.__ProgName = P_Name

    def getProgramName(self):
        return self.__ProgName

#**********************************************************************
    #Handling PROGRAM_VERSION
    def setProgramV(self,P_Version):
        self.__ProgVersion = P_Version

    def getProgramV(self):
        return self.__ProgVersion

#**********************************************************************
    #Handling PROGRAM_VERSION_NUMBER
    def setProgramVNo(self,P_VersionNo):
        self.__ProgVersionNo = P_VersionNo

    def getProgramVNo(self):
        return self.__ProgVersionNo

#**********************************************************************
    #Handling LINKABLE
    def setLinkable(self,Linkable):
        self.__Linkable = Linkable

    def getLinkable(self):
        return self.__Linkable

#**********************************************************************
    # DEVICE_TYPE
    def setDeviceType(self,DeviceType):
        self.__DevType = DeviceType

    def getDeviceType(self):
        return self.__DevType

#**********************************************************************
    # PEI_TYPE
    def setPEIType(self,PEIType):
        self.__PEIType = PEIType

    def getPEIType(self):
        return self.__PEIType

#**********************************************************************
    #ADDRESS_TAB_SIZE
    def setAddrTabSize(self,AddrTabSize):
        self.__AddTabsize = AddrTabSize

    def getAddrTabSize(self):
        return self.__AddTabsize

#**********************************************************************
    #ASSOCTAB_ADDRESS
    def setAssTabAddr(self,AssTabAddr):
        self.__AssTabAddr = AssTabAddr

    def getAssTabAddr(self):
        return self.__AssTabAddr

#**********************************************************************
    #ASSOCTAB_SIZE
    def setAssTabSize(self,AssTabSize):
        self.__AssTsize = AssTabSize

    def getAssTabSize(self):
        return self.__AssTsize

#**********************************************************************
    #COMMSTAB_ADDRESS
    def setComTabAddr(self,ComTabAddr):
        self.__ComTabAddr = ComTabAddr

    def getComTabAddr(self):
        return self.__ComTabAddr

#**********************************************************************
    #COMMSTAB_SIZE
    def setComTabSize(self,ComTabSize):
        self.__ComTabsize = ComTabSize

    def getComTabSize(self):
        return self.__ComTabsize

#**********************************************************************
    #PROGRAM_SERIAL_NUMBER
    def setProgramSN(self,P_SN):
        self.__ProgSN = P_SN

    def getProgramSN(self):
        return self.__ProgSN

#**********************************************************************
    #MANUFACTURER_ID
    def setAppManufacID(self,M_ID):
        self.__AppManID = M_ID

    def getAppManufacID(self):
        return self.__AppManID

#**********************************************************************
    #EEPROM_DATA
    def setEEPRPOMData(self,E_Data):
        self.__EEPROMData = E_Data

    def getEEPRPOMData(self):
        return self.__EEPROMData

#**********************************************************************
    #DATA_LENGTH
    def setDataLength(self,DataL):
        self.__DataLength = DataL

    def getDataLength(self):
        return self.__DataLength

#**********************************************************************
    #S19_FILE
    def setS19File(self,S_File):
        self.__S19File = S_File

    def getS19File(self):
        return self.__S19File

#**********************************************************************
    #MAP_FILE
    def setMapFile(self,M_File):
        self.__MapFile = M_File

    def getMapFile(self):
        return self.__MapFile

#**********************************************************************
    #ASSEMBLER_ID
    def setAssID(self,A_ID):
        self.__AssemblerID = A_ID

    def getAssID(self):
        return self.__AssemblerID

#**********************************************************************
    #HELP_FILE_NAME
    def setHelpFileName(self,H_File):
        self.__HelpFileName = H_File

    def getHelpFileName(self):
        return self.__HelpFileName

#**********************************************************************
    #CONTEXT_ID
    def setContextID(self,C_ID):
        self.__ContextID = C_ID

    def getContextID(self):
        return self.__ContextID

#**********************************************************************
    #DYNAMIC_MANAGEMENT
    def setDynMng(self,Dynmamic):
        self.__DynamicMng = Dynmamic

    def getDynMng(self):
        return self.__DynamicMng

#**********************************************************************
    #PROGRAM_TYPE
    def setProgramType(self,ProgType):
        self.__ProgType = ProgType

    def getProgramType(self):
        return self.__ProgType

#**********************************************************************
    #RAM_SIZE
    def setRamSize(self,RAM):
        self.__RAMSize = RAM

    def getRamSize(self):
        return self.__RAMSize

#**********************************************************************
    #ORIGINAL_MANUFACTURER_ID
    def setOrigManID(self,OMan_ID):
        self.__OrgManID = OMan_ID

    def getOrigManID(self):
        return self.__OrgManID

#**********************************************************************
    #API_VERSION
    def setAPIVersion(self,API):
        self.__APIVersion = API

    def getAPIVersion(self):
        return self.__APIVersion

#**********************************************************************
    #PROGRAM_STYLE
    def setProgramStyle(self,P_Style):
        self.__ProgStyle = P_Style

    def getProgramStyle(self):
        return self.__ProgStyle

#**********************************************************************
    #IS_POLLING_MASTER
    def setPollingMaster(self,Master):
        self.__PollMaster = Master

    def getPollingMaster(self):
        return self.__PollMaster

#**********************************************************************
    #NUMBER_OF_POLLING_GROUPS
    def setPollingGroups(self,Groups):
        self.__NoPollGroups = Groups

    def getPollingGroups(self):
        return self.__NoPollGroups

#**********************************************************************
    #AllowedInSimpleEts
    def setAllowETS(self,ETS):
        self.__AllowedInETS = ETS

    def getAllowETS(self):
        return self.__AllowedInETS

#**********************************************************************
    #MinEtsVersion
    def setMinETS(self,MinETS):
        self.__MinEtsVersion = MinETS

    def getMinETS(self):
        return self.__MinEtsVersion




