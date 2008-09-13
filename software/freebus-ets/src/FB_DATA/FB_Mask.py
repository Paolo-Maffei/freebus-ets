#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source Datei: FB_Mask.py
#Version: V0.1 , 06.01.2008
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Mask-Data which based from FB XML Product-Files
class FB_Mask:

    __MaskID = 0                #MASK_ID
    __MaskVersion = 0           #MASK_VERSION
    __UserRamStart = 0          #USER_RAM_START
    __UserRamEnd = 0            #USER_RAM_END
    __UserEEpromStart = 0       #USER_EEPROM_START
    __UserEEpromEnd = 0         #USER_EEPROM_END
    __RunErrorAddress = 0       #RUN_ERROR_ADDRESS
    __Address_Tab_Addr = 0      #ADDRESS_TAB_ADDRESS
    __AssocTab_Addr = 0         #ASSOCTABPTR_ADDRESS
    __CommsTab_Addr = 0         #COMMSTABPTR_ADDRESS
    __Manufact_Data_Addr = 0    #MANUFACTURER_DATA_ADDRESS
    __Manufact_Data_Size = 0    #MANUFACTURER_DATA_SIZE
    __Manufact_ID_Addr = 0      #MANUFACTURER_ID_ADDRESS
    __Rout_Addr = 0             #ROUTECNT_ADDRESS
    __Manufact_ID_Protetect = 0 #MANUFACTURER_ID_PROTECTED
    __Mask_Version_Name = ""     #MASK_VERSION_NAME
    __Mask_EEpromData = ""       #MASK_EEPROM_DATA
    __Mask_Data_Length = 0      #MASK_DATA_LENGTH
    __Address_Tab = 0           #ADDRESS_TAB_LCS
    __Assoc_Tab = 0             #ASSOC_TAB_LCS
    __App_Program = 0           #APPLICATION_PROGRAM_LCS
    __PEI_Program = 0           #PEI_PROGRAM_LCS
    __Load_Control_Addr = 0     #LOAD_CONTROL_ADDRESS
    __Run_Control_Addr = 0      #RUN_CONTROL_ADDRESS
    __ExtMemoryStart = 0        #EXTERNAL_MEMORY_START    NEU
    __ExtMemoryEnd = 0          #EXTERNAL_MEMORY_END      NEU
    __AppProgramRCS = 0         #APPLICATION_PROGRAM_RCS  NEU
    __PEIProgramRCS = 0         #PEI_PROGRAM_RCS          NEU
    __PortADDR = 0              #PORT_A_DDR               NEU
    __Port_Addr_Protect = 0     #PORT_ADDRESS_PROTECTED
    __Medium_TypeNo = 0         #MEDIUM_TYPE_NUMBER
    __Medium_TypeNo2 = 0        #MEDIUM_TYPE_NUMBER2      NEU
    __BCU_TypeNo = 0            #BCU_TYPE_NUMBER


    def __init__(self):
        #print "okk"
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__MaskID,self.__MaskVersion,self.__UserRamStart,self.__UserRamEnd,self.__UserEEpromStart,
                self.__UserEEpromEnd,self.__RunErrorAddress,self.__Address_Tab_Addr,self.__AssocTab_Addr,
                self.__CommsTab_Addr,self.__Manufact_Data_Addr,self.__Manufact_Data_Size,self.__Manufact_ID_Addr,
                self.__Rout_Addr,self.__Manufact_ID_Protetect,self.__Mask_Version_Name,self.__Mask_EEpromData,
                self.__Mask_Data_Length,self.__Address_Tab,self.__Assoc_Tab,self.__App_Program,self.__PEI_Program,
                self.__Load_Control_Addr,self.__Run_Control_Addr,self.__ExtMemoryStart, self.__ExtMemoryEnd,
                self.__AppProgramRCS, self.__PEIProgramRCS,self.__PortADDR, self.__Port_Addr_Protect,self.__Medium_TypeNo,
                self.__Medium_TypeNo2,self.__BCU_TypeNo)

        return List

    def setMask(self,Index, Value):
        if(Index == 1):
            self.__MaskID = Value
        elif(Index == 2):
            self.__MaskVersion = Value
        elif(Index == 3):
            self.__UserRamStart = Value
        elif(Index == 4):
            self.__UserRamEnd = Value
        elif(Index == 5):
            self.__UserEEpromStart = Value
        elif(Index == 6):
            self.__UserEEpromEnd = Value
        elif(Index == 7):
            self.__RunErrorAddress = Value
        elif(Index == 8):
            self.__Address_Tab_Addr = Value
        elif(Index == 9):
            self.__AssocTab_Addr = Value
        elif(Index == 10):
            self.__CommsTab_Addr = Value
        elif(Index == 11):
            self.__Manufact_Data_Addr = Value
        elif(Index == 12):
            self.__Manufact_Data_Size = Value
        elif(Index == 13):
            self.__Manufact_ID_Addr = Value
        elif(Index == 14):
            self.__Rout_Addr = Value
        elif(Index == 15):
            self.__Manufact_ID_Protetect = Value
        elif(Index == 16):
            self.__Mask_Version_Name = Value
        elif(Index == 17):
            self.__Mask_EEpromData = Value
        elif(Index == 18):
            self.__Mask_Data_Length = Value
        elif(Index == 19):
            self.__Address_Tab = Value
        elif(Index == 20):
            self.__Assoc_Tab = Value
        elif(Index == 21):
            self.__App_Program = Value
        elif(Index == 22):
            self.__PEI_Program = Value
        elif(Index == 23):
            self.__Load_Control_Addr = Value
        elif(Index == 24):
            self.__Run_Control_Addr = Value
        elif(Index == 25):
            self.__ExtMemoryStart = Value
        elif(Index == 26):
            self.__ExtMemoryEnd = Value
        elif(Index == 27):
            self.__AppProgramRCS = Value
        elif(Index == 28):
            self.__PEIProgramRCS = Value
        elif(Index == 29):
            self.__PortADDR = Value
        elif(Index == 30):
            self.__Port_Addr_Protect = Value
        elif(Index == 31):
            self.__Medium_TypeNo = Value
        elif(Index == 33):
            self.__Medium_TypeNo2 = Value
        elif(Index == 33):
            self.__BCU_TypeNo = Value

    def getMask(self,Index):
        if(Index == 1):
            return self.__MaskID
        elif(Index == 2):
            return self.__MaskVersion
        elif(Index == 3):
            return self.__UserRamStart
        elif(Index == 4):
            return self.__UserRamEnd
        elif(Index == 5):
            return self.__UserEEpromStart
        elif(Index == 6):
            return self.__UserEEpromEnd
        elif(Index == 7):
            return self.__RunErrorAddress
        elif(Index == 8):
            return self.__Address_Tab_Addr
        elif(Index == 9):
            return self.__AssocTab_Addr
        elif(Index == 10):
            return self.__CommsTab_Addr
        elif(Index == 11):
            return self.__Manufact_Data_Addr
        elif(Index == 12):
            return self.__Manufact_Data_Size
        elif(Index == 13):
            return self.__Manufact_ID_Addr
        elif(Index == 14):
            return self.__Rout_Addr
        elif(Index == 15):
            return self.__Manufact_ID_Protetect
        elif(Index == 16):
            return self.__Mask_Version_Name
        elif(Index == 17):
            return self.__Mask_EEpromData
        elif(Index == 18):
            return self.__Mask_Data_Length
        elif(Index == 19):
            return self.__Address_Tab
        elif(Index == 20):
            return self.__Assoc_Tab
        elif(Index == 21):
            return self.__App_Program
        elif(Index == 22):
            return self.__PEI_Program
        elif(Index == 23):
            return self.__Load_Control_Addr
        elif(Index == 24):
            return self.__Run_Control_Addr
        elif(Index == 25):
            return self.__ExtMemoryStart
        elif(Index == 26):
            return self.__ExtMemoryEnd
        elif(Index == 27):
            return self.__AppProgramRCS
        elif(Index == 28):
            return self.__PEIProgramRCS
        elif(Index == 29):
            return self.__PortADDR
        elif(Index == 30):
            return self.__Port_Addr_Protect
        elif(Index == 31):
            return self.__Medium_TypeNo
        elif(Index == 32):
            return self.__Medium_TypeNo2
        elif(Index == 33):
            return self.__BCU_TypeNo


#**********************************************************************
    #Handling MASK_ID
    def setMaskID(self,M_ID):
        self.__MaskID = M_ID

    def getMaskID(self):
        return self.__MaskID
#**********************************************************************
    #Handling MASK_VERSION
    def setMaskVersion(self,Version):
        self.__MaskVersion = Version

    def getMaskVersion(self):
        return self.__MaskVersion

#**********************************************************************
    #Handling USER_RAM_START
    def setUserRamStart(self,RamStart):
        self.__UserRamStart = RamStart

    def getUserRamStart(self):
        return self.__UserRamStart

#**********************************************************************
    #Handling USER_RAM_END
    def setUserRamEnd(self,RamEnd):
        self.__UserRamEnd = RamEnd

    def getUserRamEnd(self):
        return self.__UserRamEnd

#**********************************************************************
    #Handling USER_EEPROM_START
    def setUserEEpromStart(self,EEPromStart):
        self.__UserEEpromStart = EEPromStart

    def getUserEEpromStart(self):
        return self.__UserEEpromStart

#**********************************************************************
    #Handling USER_EEPROM_END
    def setUserEEpromEnd(self,EEPromEnd):
        self.__UserEEpromEnd = EEPromEnd

    def getUserEEpromEnd(self):
        return self.__UserEEpromEnd

#**********************************************************************
    #Handling RUN_ERROR_ADDRESS
    def setRunErrorAddr(self,RunErrorAddr):
        self.__RunErrorAddress = RunErrorAddr

    def getRunErrorAddr(self):
        return self.__RunErrorAddress

#**********************************************************************
    # ADDRESS_TAB_ADDRESS
    def setAddrTabAddr(self,AddrTab):
        self.__Address_Tab_Addr = AddrTab

    def getAddrTabAddr(self):
        return self.__Address_Tab_Addr

#**********************************************************************
    # ASSOCTABPTR_ADDRESS
    def setAssocTabAddr(self,AssocTab):
        self.__AssocTab_Addr = AssocTab

    def getAssocTabAddr(self):
        return self.__AssocTab_Addr

#**********************************************************************
    #COMMSTABPTR_ADDRESS
    def setCommsTabAddr(self,CommsTab):
        self.__CommsTab_Addr = CommsTab

    def getCommsTabAddr(self):
        return self.__CommsTab_Addr

#**********************************************************************
    #MANUFACTURER_DATA_ADDRESS
    def setManufactDataAddr(self,ManufactDataAddr):
        self.__Manufact_Data_Addr = ManufactDataAddr

    def getManufactDataAddr(self):
        return self.__Manufact_Data_Addr

#**********************************************************************
    #MANUFACTURER_DATA_SIZE
    def setManufactDataSize(self,ManufactDataSize):
        self.__Manufact_Data_Size = ManufactDataSize

    def getManufactDataSize(self):
        return self.__Manufact_Data_Size

#**********************************************************************
    #MANUFACTURER_ID_ADDRESS
    def setManufactIDAddr(self,ManufactID):
        self.__Manufact_ID_Addr = ManufactID

    def getManufactIDAddr(self):
        return self.__Manufact_ID_Addr

#**********************************************************************
    #ROUTECNT_ADDRESS
    def setRoutAddr(self,RouteAddr):
        self.__Rout_Addr = RouteAddr

    def getRoutAddr(self):
        return self.__Rout_Addr

#**********************************************************************
    #MANUFACTURER_ID_PROTECTED
    def setManufactIDProtect(self,ManufactIDProtect):
        self.__Manufact_ID_Protetect = ManufactIDProtect

    def getManufactIDProtect(self):
        return self.__Manufact_ID_Protetect

#**********************************************************************
    #MASK_VERSION_NAME
    def setMaskVersionName(self,MaskVersionName):
        self.__Mask_Version_Name = MaskVersionName

    def getMaskVersionName(self):
        return self.__Mask_Version_Name

#**********************************************************************
    #MASK_EEPROM_DATA
    def setMaskEEpromData(self,MaskEEpromData):
        self.__Mask_EEpromData = MaskEEpromData

    def getMaskEEpromData(self):
        return self.__Mask_EEpromData

#**********************************************************************
    #MASK_DATA_LENGTH
    def setMaskDataLength(self,MaskDataLength):
        self.__Mask_Data_Length = MaskDataLength

    def getMaskDataLength(self):
        return self.__Mask_Data_Length

#**********************************************************************

    #ADDRESS_TAB_LCS
    def setAddressTab(self,AddressTab):
        self.__Address_Tab = AddressTab

    def getAddressTab(self):
        return self.__Address_Tab

#**********************************************************************
    #ASSOC_TAB_LCS
    def setAssocTab(self,AssocTab):
        self.__Assoc_Tab = AssocTab

    def getAssocTab(self):
        return self.__Assoc_Tab

#**********************************************************************
    #APPLICATION_PROGRAM_LCS
    def setAppProgram(self,AppProgram):
        self.__App_Program = AppProgram

    def getAppProgram(self):
        return self.__App_Program

#**********************************************************************
    #PEI_PROGRAM_LCS
    def setPEIProgram(self,PEIProgram):
        self.__PEI_Program = PEIProgram

    def getPEIProgram(self):
        return self.__PEI_Program

#**********************************************************************
    #LOAD_CONTROL_ADDRESS
    def setLoadControlAddr(self,LoadControlAddr):
        self.__Load_Control_Addr = LoadControlAddr

    def getLoadControlAddr(self):
        return self.__Load_Control_Addr

#**********************************************************************
    #RUN_CONTROL_ADDRESS
    def setRunControlAddr(self,RunControlAddr):
        self.__Run_Control_Addr = RunControlAddr

    def getRunControlAddr(self):
        return self.__Run_Control_Addr

#**********************************************************************
    #EXTERNAL_MEMORY_START
    def setExtMemoryStart(self,ExtMemStart):
        self.__ExtMemoryStart = ExtMemStart

    def getExtMemoryStart(self):
        return self.__ExtMemoryStart

#**********************************************************************
    #EXTERNAL_MEMORY_END
    def setExtMemoryEnd(self,ExtMemEnd):
        self.__ExtMemoryEnd = ExtMemEnd

    def getExtMemoryEnd(self):
        return self.__ExtMemoryEnd
#**********************************************************************
    #APPLICATION_PROGRAM_RCS
    def setAppProgramRCS(self,AppProgRCS):
        self.__AppProgramRCS = AppProgRCS

    def getAppProgramRCS(self):
        return self.__AppProgramRCS

#**********************************************************************
    #PEI_PROGRAM_RCS
    def setPEIProgramRCS(self,PEIProgRCS):
        self.__PEIProgramRCS = PEIProgRCS

    def getPEIProgramRCS(self):
        return self.__PEIProgramRCS
#**********************************************************************
    #PORT_A_DDR
    def setPortA_Addr(self,PortAAddr):
        self.__PortADDR = PortAAddr

    def getPortA_Addr(self):
        return self.__PortADDR
#**********************************************************************
    #PORT_ADDRESS_PROTECTED
    def setPortAddrProtected(self,PortAddrProtected):
        self.__Port_Addr_Protect = PortAddrProtected

    def getPortAddrProtected(self):
        return self.__Port_Addr_Protect

#**********************************************************************
    #MEDIUM_TYPE_NUMBER
    def setMediumTypeNo(self,MediumTypeNo):
        self.__Medium_TypeNo = MediumTypeNo

    def getMediumTypeNo(self):
        return self.__Medium_TypeNo
#**********************************************************************
    #MEDIUM_TYPE_NUMBER2
    def setMediumTypeNo2(self,MediumTypeNo2):
        self.__Medium_TypeNo2 = MediumTypeNo2
    def getMediumTypeNo2(self):
        return self.__Medium_TypeNo2

#**********************************************************************
    #BCU_TYPE_NUMBER
    def setBCUTypeNo(self,BCUTypeNo):
        self.__BCU_TypeNo = BCUTypeNo

    def getBCUTypeNo(self):
        return self.__BCU_TypeNo

#**********************************************************************
