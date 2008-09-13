#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_Prod2ProgrXMLHandler.py
#Version: V0.1 , 03.01.2008
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 15.06.2008
#Version: V0.4 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#
#===============================================================================

from FB_DATA import FB_Prod2Progr


##Products, Applications, Communications-objects
class FB_Prod2ProgrXMLHandler():

    __LogObj = None
    __prod2Prog = []      #List of Instances
    __prod = None         #prviate object for
    __isProd2Prog = False

    __isProd2Prog_ID = False           #PROD2PROG_ID
    __isProduct_ID = False             #PRODUCT_ID
    __isProgram_ID = False             #PROGRAM_ID
    __isProd2Prog_Status = False       #PROD2PROG_STATUS                NEU
    __isPEIProgrID = False             #PEI_PROGRAM_ID                  NEU
    __isProd2Prog_Status_Code = False  #PROD2PROG_STATUS_CODE
    __isReg_Number = False             #REGISTRATION_NUMBER
    __isReg_Year = False               #REGISTRATION_YEAR
    __isOrig_Reg_Number = False        #ORIGINAL_REGISTRATION_NUMBER
    __isOrig_Reg_Year = False          #ORIGINAL_REGISTRATION_YEAR
    __isExpiration_Date = False        #EXPIRATION_DATE                 NEU
    __isReg_TS = False                 #REGISTRATION_TS
    __isReg_Date = False               #REGISTRATION_DATE               NEU
    __isReg_Comment = False            #REGISTRATION_COMMENT            NEU
    __isReg_Medium_Type = False        #REGISTRATION_MEDIUM_TYPE        NEU
    __isDCY_F_Individual = False       #DCY_F_INDIVIDUAL                NEU
    __isDCY_G_Individual = False       #DCY_G_INDIVIDUAL                NEU
    __isDCY_F_Group = False            #DCY_F_GROUP                     NEU
    __isDCY_G_Group = False            #DCY_G_GROUP                     NEU
    __isSignature = False              #Signature                       NEU


    def __init__(self, LogObj):
        self.__LogObj = LogObj
        self.__prod = FB_Prod2Progr.FB_Prod2Prog()
        self.__prod2Prog = []    #init List

    #return List of Instances of type FB_Prod2Progr
    def getProduct2ProgramList(self):
        return self.__prod2Prog


    def startDocument(self):
        try:
            pass

        except SAXException:
            print "SAXError"

    def endDocument(self):
        try:
            pass

        except SAXException:
            print "SAXError"

    def startElement(self, eName, attrs):
        try:

            if(eName == "product_to_program"):
                self.__isProd2Prog = True

            elif(eName == "PROD2PROG_ID"):
                if(self.__isProd2Prog == True):
                    self.__isProd2Prog_ID = True

            elif(eName == "PRODUCT_ID"):
                if(self.__isProd2Prog == True):
                    self.__isProduct_ID = True

            elif(eName == "PROGRAM_ID"):
                if(self.__isProd2Prog == True):
                    self.__isProgram_ID = True

            elif(eName == "PROD2PROG_STATUS"):
                if(self.__isProd2Prog == True):
                    self.__isProd2Prog_Status = True

            elif(eName == "PEI_PROGRAM_ID"):
                if(self.__isProd2Prog == True):
                    self.__isPEIProgrID = True

            elif(eName == "PROD2PROG_STATUS_CODE"):
                if(self.__isProd2Prog == True):
                    self.__isProd2Prog_Status_Code = True

            elif(eName == "REGISTRATION_NUMBER"):
                if(self.__isProd2Prog == True):
                    self.__isReg_Number = True

            elif(eName == "REGISTRATION_YEAR"):
                if(self.__isProd2Prog == True):
                    self.__isReg_Year = True

            elif(eName == "ORIGINAL_REGISTRATION_NUMBER"):
                if(self.__isProd2Prog == True):
                    self.__isOrig_Reg_Number = True

            elif(eName == "ORIGINAL_REGISTRATION_YEAR"):
                if(self.__isProd2Prog == True):
                    self.__isOrig_Reg_Year = True

            elif(eName == "EXPIRATION_DATE"):
                if(self.__isProd2Prog == True):
                    self.__isExpiration_Date = True

            elif(eName == "REGISTRATION_TS"):
                if(self.__isProd2Prog == True):
                    self.__isReg_TS = True

            elif(eName == "REGISTRATION_DATE"):
                if(self.__isProd2Prog == True):
                    self.__isReg_Date = True

            elif(eName == "REGISTRATION_COMMENT"):
                if(self.__isProd2Prog == True):
                    self.__isReg_Comment = True

            elif(eName == "REGISTRATION_MEDIUM_TYPE"):
                if(self.__isProd2Prog == True):
                    self.__isReg_Medium_Type = True

            elif(eName == "DCY_F_INDIVIDUAL"):
                if(self.__isProd2Prog == True):
                    self.__isDCY_F_Individual = True

            elif(eName == "DCY_G_INDIVIDUAL"):
                if(self.__isProd2Prog == True):
                    self.__isDCY_G_Individual = True

            elif(eName == "DCY_F_GROUP"):
                if(self.__isProd2Prog == True):
                    self.__isDCY_F_Group = True

            elif(eName == "DCY_G_GROUP"):
                if(self.__isProd2Prog == True):
                    self.__isDCY_G_Group = True

            elif(eName == "Signature"):
                if(self.__isProd2Prog == True):
                    self.__isSignature = True

        except SAXException:
            print "Error again"

    def endElement(self,eName):
        #print eName
        if(eName == "product_to_program"):
            self.__isProd2Prog = False

            self.__prod2Prog.append(self.__prod)
            del self.__prod
            self.__prod = FB_Prod2Progr.FB_Prod2Prog()

        elif(eName == "PROD2PROG_ID"):
            if(self.__isProd2Prog == True):
                self.__isProd2Prog_ID = False

        elif(eName == "PRODUCT_ID"):
            if(self.__isProd2Prog == True):
                self.__isProduct_ID = False

        elif(eName == "PROGRAM_ID"):
            if(self.__isProd2Prog == True):
                self.__isProgram_ID = False

        elif(eName == "PROD2PROG_STATUS"):
            if(self.__isProd2Prog == True):
                self.__isProd2Prog_Status = False

        elif(eName == "PEI_PROGRAM_ID"):
            if(self.__isProd2Prog == True):
                self.__isPEIProgrID = False

        elif(eName == "PROD2PROG_STATUS_CODE"):
            if(self.__isProd2Prog == True):
                self.__isProd2Prog_Status_Code = False

        elif(eName == "REGISTRATION_NUMBER"):
            if(self.__isProd2Prog == True):
                self.__isReg_Number = False

        elif(eName == "REGISTRATION_YEAR"):
            if(self.__isProd2Prog == True):
                self.__isReg_Year = False

        elif(eName == "ORIGINAL_REGISTRATION_NUMBER"):
            if(self.__isProd2Prog == True):
                self.__isOrig_Reg_Number = False

        elif(eName == "ORIGINAL_REGISTRATION_YEAR"):
            if(self.__isProd2Prog == True):
                self.__isOrig_Reg_Year = False

        elif(eName == "EXPIRATION_DATE"):
            if(self.__isProd2Prog == True):
                self.__isExpiration_Date = False

        elif(eName == "REGISTRATION_TS"):
            if(self.__isProd2Prog == True):
                self.__isReg_TS = False

        elif(eName == "REGISTRATION_DATE"):
            if(self.__isProd2Prog == True):
                self.__isReg_Date = False

        elif(eName == "REGISTRATION_COMMENT"):
            if(self.__isProd2Prog == True):
                self.__isReg_Comment = False

        elif(eName == "REGISTRATION_MEDIUM_TYPE"):
            if(self.__isProd2Prog == True):
                self.__isReg_Medium_Type = False

        elif(eName == "DCY_F_INDIVIDUAL"):
            if(self.__isProd2Prog == True):
                self.__isDCY_F_Individual = False

        elif(eName == "DCY_G_INDIVIDUAL"):
            if(self.__isProd2Prog == True):
                self.__isDCY_G_Individual = False

        elif(eName == "DCY_F_GROUP"):
            if(self.__isProd2Prog == True):
                self.__isDCY_F_Group = False

        elif(eName == "DCY_G_GROUP"):
            if(self.__isProd2Prog == True):
                self.__isDCY_G_Group = False

        elif(eName == "Signature"):
            if(self.__isProd2Prog == True):
                self.__isSignature = False

    def characters(self ,char):

        strValue = char.encode( "iso-8859-1" )

        #print char.encode( "iso-8859-1" )
        if(self.__isProd2Prog_ID == True):
            self.__prod.setProd2ProgID(self.IsNumber(strValue))

        elif(self.__isProduct_ID == True):
            self.__prod.setProductID(self.IsNumber(strValue))

        elif(self.__isProgram_ID == True):
            self.__prod.setProgramID(self.IsNumber(strValue))

        elif(self.__isProd2Prog_Status == True):
            self.__prod.setProd2ProgStatus(self.IsString(strValue))

        elif(self.__isPEIProgrID == True):
            self.__prod.setPEIProgramID(self.IsNumber(strValue))

        elif(self.__isProd2Prog_Status_Code == True):
            self.__prod.setProd2ProgStatusCode(self.IsNumber(strValue))

        elif(self.__isReg_Number == True):
            self.__prod.setRegNumber(self.IsString(strValue))

        elif(self.__isReg_Year == True):
            self.__prod.setRegYear(self.IsString(strValue))

        elif(self.__isOrig_Reg_Number == True):
            self.__prod.setOrigRegNumber(self.IsString(strValue))

        elif(self.__isOrig_Reg_Year == True):
            self.__prod.setOrigRegYear(self.IsString(strValue))

        elif(self.__isExpiration_Date == True):
            self.__prod.setExpirationDate(self.IsString(strValue))

        elif(self.__isReg_TS == True):
            self.__prod.setRegTS(self.IsString(strValue))

        elif(self.__isReg_Date == True):
            self.__prod.setRegDate(self.IsString(strValue))

        elif(self.__isReg_Comment == True):
            self.__prod.setRegComment(self.IsString(strValue))

        elif(self.__isReg_Medium_Type == True):
            self.__prod.setRegMediumType(self.IsString(strValue))

        elif(self.__isDCY_F_Individual == True):
            self.__prod.setDCY_F_IND(self.IsNumber(strValue))

        elif(self.__isDCY_G_Individual == True):
            self.__prod.setDCY_G_IND(self.IsNumber(strValue))

        elif(self.__isDCY_F_Group == True):
            self.__prod.setDCY_F_Group(self.IsNumber(strValue))

        elif(self.__isDCY_G_Group == True):
            self.__prod.setDCY_G_Group(self.IsNumber(strValue))

        elif(self.__isSignature == True):
            self.__prod.setSignature(self.IsString(strValue))


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
