#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source Datei: FB_MaskXMLHandler.py
#Version: V0.1 , 25.12.2007
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 15.06.2008
#Version: V0.4 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================

from FB_DATA import FB_Mask

##Class for Extracting Applications from FB-XML Productfiles
class FB_MaskXMLHandler():

    __LogObj = None
    __isMask = False          #Mask found ?

    __Mask = None
    __MaskList = []      #List of Instances with Apllications (FB_Applications)

    #Sub-Nodes of application_program
    __isMaskID = False                #MASK_ID
    __isMaskVersion = False           #MASK_VERSION
    __isUserRamStart = False          #USER_RAM_START
    __isUserRamEnd = False            #USER_RAM_END
    __isUserEEpromStart = False       #USER_EEPROM_START
    __isUserEEpromEnd = False         #USER_EEPROM_END
    __isRunErrorAddress = False       #RUN_ERROR_ADDRESS
    __isAddress_Tab_Addr = False      #ADDRESS_TAB_ADDRESS
    __isAssocTab_Addr = False         #ASSOCTABPTR_ADDRESS
    __isCommsTab_Addr = False         #COMMSTABPTR_ADDRESS
    __isManufact_Data_Addr = False    #MANUFACTURER_DATA_ADDRESS
    __isManufact_Data_Size = False    #MANUFACTURER_DATA_SIZE
    __isManufact_ID_Addr = False      #MANUFACTURER_ID_ADDRESS
    __isRout_Addr = False             #ROUTECNT_ADDRESS
    __isManufact_ID_Protetect = False #MANUFACTURER_ID_PROTECTED
    __isMask_Version_Name = False     #MASK_VERSION_NAME
    __isMaskEEpromData = False        #MASK_EEPROM_DATA
    __isMask_Data_Length = False      #MASK_DATA_LENGTH
    __isAddress_Tab = False           #ADDRESS_TAB_LCS
    __isAssoc_Tab = False             #ASSOC_TAB_LCS
    __isApp_Program = False           #APPLICATION_PROGRAM_LCS
    __isPEI_Program = False           #PEI_PROGRAM_LCS
    __isLoad_Control_Addr = False     #LOAD_CONTROL_ADDRESS
    __isRun_Control_Addr = False      #RUN_CONTROL_ADDRESS
    __isExtMemoryStart = False        #EXTERNAL_MEMORY_START    NEU
    __isExtMemoryEnd = False          #EXTERNAL_MEMORY_END      NEU
    __isAppProgramRCS = False         #APPLICATION_PROGRAM_RCS  NEU
    __isPEIProgramRCS = False         #PEI_PROGRAM_RCS          NEU
    __isPortADDR = False              #PORT_A_DDR               NEU
    __isPort_Addr_Protect = False     #PORT_ADDRESS_PROTECTED
    __isMedium_TypeNo = False         #MEDIUM_TYPE_NUMBER
    __isMedium_TypeNo2 = False        #MEDIUM_TYPE_NUMBER2      NEU
    __isBCU_TypeNo = False            #BCU_TYPE_NUMBER



    #Constructor for FB_MaskXMLHandler.
    def __init__(self, LogObj):
        self.__LogObj = LogObj
        self.__Mask = FB_Mask.FB_Mask()
        self.__MaskList = []    #init List

    #return List of Instances of type FB_Mask
    def getMaskList(self):
         return self.__MaskList

    def startDocument(self):
        try:
            #self.__LogObj.NewLog("startDocument: " ,0)
            pass

        except SAXException:
            pass

    def endDocument(self):
        try:
            #self.__LogObj.NewLog("endDocument: " ,0)
            pass

        except SAXException:
            pass

    def startElement(self, eName, attrs):

        try:
            #self.__LogObj.NewLog("startElement: " ,0)
        #Look at SubNodes mask
            if(eName == "mask"):
                self.__isMask = True

            elif(eName == "MASK_ID"):
                if(self.__isMask == True):
                    self.__isMaskID = True

            elif(eName == "MASK_VERSION"):
                if(self.__isMask == True):
                    self.__isMaskVersion = True

            elif(eName == "USER_RAM_START"):
                if(self.__isMask == True):
                    self.__isUserRamStart = True

            elif(eName == "USER_RAM_END"):
                if(self.__isMask == True):
                    self.__isUserRamEnd = True

            elif(eName == "USER_EEPROM_START"):
                if(self.__isMask == True):
                    self.__isUserEEpromStart = True

            elif(eName == "USER_EEPROM_END"):
                if(self.__isMask == True):
                    self.__isUserEEpromEnd = True

            elif(eName == "RUN_ERROR_ADDRESS"):
                if(self.__isMask == True):
                    self.__isRunErrorAddress = True

            elif(eName == "ADDRESS_TAB_ADDRESS"):
                if(self.__isMask == True):
                    self.__isAddress_Tab_Addr = True

            elif(eName == "ASSOCTABPTR_ADDRESS"):
                if(self.__isMask == True):
                    self.__isAssocTab_Addr = True

            elif(eName == "COMMSTABPTR_ADDRESS"):
                if(self.__isMask == True):
                    self.__isCommsTab_Addr = True

            elif(eName == "MANUFACTURER_DATA_ADDRESS"):
                if(self.__isMask == True):
                    self.__isManufact_Data_Addr = True

            elif(eName == "MANUFACTURER_DATA_SIZE"):
                if(self.__isMask == True):
                    self.__isManufact_Data_Size = True

            elif(eName == "MANUFACTURER_ID_ADDRESS"):
                if(self.__isMask == True):
                    self.__isManufact_ID_Addr = True

            elif(eName == "ROUTECNT_ADDRESS"):
                if(self.__isMask == True):
                    self.__isRout_Addr = True

            elif(eName == "MANUFACTURER_ID_PROTECTED"):
                if(self.__isMask == True):
                    self.__isManufact_ID_Protetect = True

            elif(eName == "MASK_VERSION_NAME"):
                if(self.__isMask == True):
                    self.__isMask_Version_Name = True

            elif(eName == "MASK_EEPROM_DATA"):
                if(self.__isMask == True):
                    self.__isMaskEEpromData = True

            elif(eName == "MASK_DATA_LENGTH"):
                if(self.__isMask == True):
                    self.__isMask_Data_Length = True

            elif(eName == "ADDRESS_TAB_LCS"):
                if(self.__isMask == True):
                    self.__isAddress_Tab = True

            elif(eName == "ASSOC_TAB_LCS"):
                if(self.__isMask == True):
                    self.__isAssoc_Tab = True

            elif(eName == "APPLICATION_PROGRAM_LCS"):
                if(self.__isMask == True):
                    self.__isApp_Program = True

            elif(eName == "PEI_PROGRAM_LCS"):
                if(self.__isMask == True):
                    self.__isPEI_Program = True

            elif(eName == "LOAD_CONTROL_ADDRESS"):
                if(self.__isMask == True):
                    self.__isLoad_Control_Addr = True

            elif(eName == "RUN_CONTROL_ADDRESS"):
                if(self.__isMask == True):
                    self.__isRun_Control_Addr = True

            elif(eName == "EXTERNAL_MEMORY_START"):
                if(self.__isMask == True):
                    self.__isExtMemoryStart = True

            elif(eName == "EXTERNAL_MEMORY_END"):
                if(self.__isMask == True):
                    self.__isExtMemoryEnd = True

            elif(eName == "APPLICATION_PROGRAM_RCS"):
                if(self.__isMask == True):
                    self.__isAppProgramRCS = True

            elif(eName == "PEI_PROGRAM_RCS"):
                if(self.__isMask == True):
                    self.__isPEIProgramRCS = True

            elif(eName == "PORT_A_DDR"):
                if(self.__isMask == True):
                    self.__isPortADDR = True

            elif(eName == "PORT_ADDRESS_PROTECTED"):
                if(self.__isMask == True):
                    self.__isPort_Addr_Protect = True

            elif(eName == "MEDIUM_TYPE_NUMBER"):
                if(self.__isMask == True):
                    self.__isMedium_TypeNo = True

            elif(eName == "MEDIUM_TYPE_NUMBER2"):
                if(self.__isMask == True):
                    self.__isMedium_TypeNo2 = True

            elif(eName == "BCU_TYPE_NUMBER"):
                if(self.__isMask == True):
                    self.__isBCU_TypeNo = True


        except SAXException:
            print "Error again"

    def endElement(self,eName):

        try:
             #self.__LogObj.NewLog("endElement: " ,0)
            if(eName == "mask"):
                self.__isMask=False
                #add Instanz to the list
                self.__MaskList.append(self.__Mask)
                del self.__Mask
                self.__Mask = FB_Mask.FB_Mask()

              #Look at SubNodes of Mask
            elif(eName == "MASK_ID"):
                if(self.__isMask == True):
                    self.__isMaskID = False

            elif(eName == "MASK_VERSION"):
                if(self.__isMask == True):
                    self.__isMaskVersion = False

            elif(eName == "USER_RAM_START"):
                if(self.__isMask == True):
                    self.__isUserRamStart = False

            elif(eName == "USER_RAM_END"):
                if(self.__isMask == True):
                    self.__isUserRamEnd = False

            elif(eName == "USER_EEPROM_START"):
                if(self.__isMask == True):
                    self.__isUserEEpromStart = False

            elif(eName == "USER_EEPROM_END"):
                if(self.__isMask == True):
                    self.__isUserEEpromEnd = False

            elif(eName == "RUN_ERROR_ADDRESS"):
                if(self.__isMask == True):
                    self.__isRunErrorAddress = False

            elif(eName == "ADDRESS_TAB_ADDRESS"):
                if(self.__isMask == True):
                    self.__isAddress_Tab_Addr = False

            elif(eName == "ASSOCTABPTR_ADDRESS"):
                if(self.__isMask == True):
                    self.__isAssocTab_Addr = False

            elif(eName == "COMMSTABPTR_ADDRESS"):
                if(self.__isMask == True):
                    self.__isCommsTab_Addr = False

            elif(eName == "MANUFACTURER_DATA_ADDRESS"):
                if(self.__isMask == True):
                    self.__isManufact_Data_Addr = False

            elif(eName == "MANUFACTURER_DATA_SIZE"):
                if(self.__isMask == True):
                    self.__isManufact_Data_Size = False

            elif(eName == "MANUFACTURER_ID_ADDRESS"):
                if(self.__isMask == True):
                    self.__isManufact_ID_Addr = False

            elif(eName == "ROUTECNT_ADDRESS"):
                if(self.__isMask == True):
                    self.__isRout_Addr = False

            elif(eName == "MANUFACTURER_ID_PROTECTED"):
                if(self.__isMask == True):
                    self.__isManufact_ID_Protetect = False

            elif(eName == "MASK_VERSION_NAME"):
                if(self.__isMask == True):
                    self.__isMask_Version_Name = False

            elif(eName == "MASK_EEPROM_DATA"):
                if(self.__isMask == True):
                    self.__isMaskEEpromData = False

            elif(eName == "MASK_DATA_LENGTH"):
                if(self.__isMask == True):
                    self.__isMask_Data_Length = False

            elif(eName == "ADDRESS_TAB_LCS"):
                if(self.__isMask == True):
                    self.__isAddress_Tab = False

            elif(eName == "ASSOC_TAB_LCS"):
                if(self.__isMask == True):
                    self.__isAssoc_Tab = False

            elif(eName == "APPLICATION_PROGRAM_LCS"):
                if(self.__isMask == True):
                    self.__isApp_Program = False

            elif(eName == "PEI_PROGRAM_LCS"):
                if(self.__isMask == True):
                    self.__isPEI_Program = False

            elif(eName == "LOAD_CONTROL_ADDRESS"):
                if(self.__isMask == True):
                    self.__isLoad_Control_Addr = False

            elif(eName == "RUN_CONTROL_ADDRESS"):
                if(self.__isMask == True):
                    self.__isRun_Control_Addr = False

            elif(eName == "EXTERNAL_MEMORY_START"):
                if(self.__isMask == True):
                    self.__isExtMemoryStart = False

            elif(eName == "EXTERNAL_MEMORY_END"):
                if(self.__isMask == True):
                    self.__isExtMemoryEnd = False

            elif(eName == "APPLICATION_PROGRAM_RCS"):
                if(self.__isMask == True):
                    self.__isAppProgramRCS = False

            elif(eName == "PEI_PROGRAM_RCS"):
                if(self.__isMask == True):
                    self.__isPEIProgramRCS = False

            elif(eName == "PORT_A_DDR"):
                if(self.__isMask == True):
                    self.__isPortADDR = False


            elif(eName == "PORT_ADDRESS_PROTECTED"):
                if(self.__isMask == True):
                    self.__isPort_Addr_Protect = False

            elif(eName == "MEDIUM_TYPE_NUMBER"):
                if(self.__isMask == True):
                    self.__isMedium_TypeNo = False

            elif(eName == "MEDIUM_TYPE_NUMBER2"):
                if(self.__isMask == True):
                    self.__isMedium_TypeNo2 = False

            elif(eName == "BCU_TYPE_NUMBER"):
                if(self.__isMask == True):
                    self.__isBCU_TypeNo = False



        except SAXException:
            print "Error again"

    def characters(self ,char):
        #print char
 #       self.__LogObj.NewLog("char: " + char.encode( "iso-8859-1" ) ,0)
        strValue = char.encode( "iso-8859-1" )

        if(self.__isMaskID == True):
            self.__Mask.setMaskID(self.IsNumber(strValue))

        elif(self.__isMaskVersion == True):
            self.__Mask.setMaskVersion(self.IsNumber(strValue))

        elif(self.__isUserRamStart == True):
            self.__Mask.setUserRamStart(self.IsNumber(strValue))

        elif(self.__isUserRamEnd == True):
            self.__Mask.setUserRamEnd(self.IsNumber(strValue))

        elif(self.__isUserEEpromStart == True):
            self.__Mask.setUserEEpromStart(self.IsNumber(strValue))

        elif(self.__isUserEEpromEnd == True):
            self.__Mask.setUserEEpromEnd(self.IsNumber(strValue))

        elif(self.__isRunErrorAddress == True):
            self.__Mask.setRunErrorAddr(self.IsNumber(strValue))

        elif(self.__isAddress_Tab_Addr == True):
            self.__Mask.setAddrTabAddr(self.IsNumber(strValue))

        elif(self.__isAssocTab_Addr == True):
            self.__Mask.setAssocTabAddr(self.IsNumber(strValue))

        elif(self.__isCommsTab_Addr == True):
            self.__Mask.setCommsTabAddr(self.IsNumber(strValue))

        elif(self.__isManufact_Data_Addr == True):
            self.__Mask.setManufactDataAddr(self.IsNumber(strValue))

        elif(self.__isManufact_Data_Size == True):
            self.__Mask.setManufactDataSize(self.IsNumber(strValue))

        elif(self.__isManufact_ID_Addr == True):
            self.__Mask.setManufactIDAddr(self.IsNumber(strValue))

        elif(self.__isRout_Addr == True):
            self.__Mask.setRoutAddr(self.IsNumber(strValue))

        elif(self.__isManufact_ID_Protetect == True):
            self.__Mask.setManufactIDProtect(self.IsNumber(strValue))

        elif(self.__isMask_Version_Name == True):
            self.__Mask.setMaskVersionName(self.IsString(strValue))

        elif(self.__isMaskEEpromData == True):
            self.__Mask.setMaskEEpromData(self.IsString(strValue))

        elif(self.__isMask_Data_Length == True):
            self.__Mask.setMaskDataLength(self.IsNumber(strValue))

        elif(self.__isAddress_Tab == True):
            self.__Mask.setAddressTab(self.IsNumber(strValue))

        elif(self.__isAssoc_Tab == True):
            self.__Mask.setAssocTab(self.IsNumber(strValue))

        elif(self.__isApp_Program == True):
            self.__Mask.setAppProgram(self.IsNumber(strValue))

        elif(self.__isPEI_Program == True):
            self.__Mask.setPEIProgram(self.IsNumber(strValue))

        elif(self.__isLoad_Control_Addr == True):
            self.__Mask.setLoadControlAddr(self.IsNumber(strValue))

        elif(self.__isRun_Control_Addr == True):
            self.__Mask.setRunControlAddr(self.IsNumber(strValue))

        elif(self.__isExtMemoryStart == True):
            self.__Mask.setExtMemoryStart(self.IsNumber(strValue))

        elif(self.__isExtMemoryEnd == True):
            self.__Mask.setExtMemoryEnd(self.IsNumber(strValue))

        elif(self.__isAppProgramRCS == True):
            self.__Mask.setAppProgramRCS(self.IsNumber(strValue))

        elif(self.__isPEIProgramRCS == True):
            self.__Mask.setPEIProgramRCS(self.IsNumber(strValue))

        elif(self.__isPortADDR == True):
            self.__Mask.setPortA_Addr(self.IsNumber(strValue))

        elif(self.__isPort_Addr_Protect == True):
            self.__Mask.setPortAddrProtected(self.IsNumber(strValue))

        elif(self.__isMedium_TypeNo == True):
            self.__Mask.setMediumTypeNo(self.IsNumber(strValue))

        elif(self.__isBCU_TypeNo == True):
            self.__Mask.setBCUTypeNo(self.IsNumber(strValue))

   #check for Number in parsed value
    def IsNumber(self,strValue):
        #print strValue
        if(strValue.isdigit() == True):
            return strValue
        else:
            return "0"

    #check for String in parsed value
    def IsString(self,strValue):

        Value = strValue.replace('\\r\\n',' ')
        Value = Value.replace('\\rn', ' ')
        Value = Value.replace("'", ' ')
        return Value

