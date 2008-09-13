#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_Prod2Progr.py
#Version: V0.1 , 03.02.2008
#Version: V0.2 , 04.06.2008
#Version: V0.3 , 20.07.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Product to Program ID's
class FB_Prod2Prog:


    __Prod2Prog_ID = 0            #PROD2PROG_ID
    __Product_ID = 0              #PRODUCT_ID
    __Program_ID = 0              #PROGRAM_ID
    __Prod2Prog_Status = ""       #PROD2PROG_STATUS                NEU
    __PEIProgrID = 0              #PEI_PROGRAM_ID                  NEU
    __Prod2Prog_Status_Code = 0   #PROD2PROG_STATUS_CODE
    __Reg_Number = ""             #REGISTRATION_NUMBER
    __Reg_Year = ""               #REGISTRATION_YEAR
    __Orig_Reg_Number = ""        #ORIGINAL_REGISTRATION_NUMBER
    __Orig_Reg_Year = ""          #ORIGINAL_REGISTRATION_YEAR
    __Expiration_Date = ""        #EXPIRATION_DATE                 NEU
    __Reg_TS = ""                 #REGISTRATION_TS
    __Reg_Date = ""               #REGISTRATION_DATE               NEU
    __Reg_Comment = ""            #REGISTRATION_COMMENT            NEU
    __Reg_Medium_Type = ""        #REGISTRATION_MEDIUM_TYPE        NEU
    __DCY_F_Individual = 0.0      #DCY_F_INDIVIDUAL                NEU
    __DCY_G_Individual = 0.0      #DCY_G_INDIVIDUAL                NEU
    __DCY_F_Group = 0.0           #DCY_F_GROUP                     NEU
    __DCY_G_Group = 0.0           #DCY_G_GROUP                     NEU
    __Signature = ""              #Signature                       NEU

    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__Prod2Prog_ID,self.__Product_ID,self.__Program_ID,self.__Prod2Prog_Status, self.__PEIProgrID,
                self.__Prod2Prog_Status_Code,self.__Reg_Number,self.__Reg_Year,self.__Orig_Reg_Number,self.__Orig_Reg_Year,
                self.__Expiration_Date, self.__Reg_TS,self.__Reg_Date, self.__Reg_Comment,self.__Reg_Medium_Type, self.__DCY_F_Individual,
                self.__DCY_G_Individual, self.__DCY_F_Group, self.__DCY_G_Group, self.__Signature)


        return List


    def setProd2Prog(self,Index, Value):
        if(Index == 1):
            self.__Prod2Prog_ID = Value
        elif(Index == 2):
            self.__Product_ID = Value
        elif(Index == 3):
            self.__Program_ID = Value
        elif(Index == 4):
            self.__Prod2Prog_Status = Value
        elif(Index == 5):
            self.__PEIProgrID = Value
        elif(Index == 6):
            self.__Prod2Prog_Status_Code = Value
        elif(Index == 7):
            self.__Reg_Number = Value
        elif(Index == 8):
            self.__Reg_Year = Value
        elif(Index == 9):
            self.__Orig_Reg_Number = Value
        elif(Index == 10):
            self.__Orig_Reg_Year = Value
        elif(Index == 11):
            self.__Expiration_Date = Value
        elif(Index == 12):
            self.__Reg_TS = Value
        elif(Index == 13):
            self.__Reg_Date = Value
        elif(Index == 14):
            self.__Reg_Comment = Value
        elif(Index == 15):
            self.__Reg_Medium_Type = Value
        elif(Index == 16):
            self.__DCY_F_Individual = Value
        elif(Index == 17):
            self.__DCY_G_Individual = Value
        elif(Index == 18):
            self.__DCY_F_Group = Value
        elif(Index == 19):
            self.__DCY_G_Group = Value
        elif(Index == 20):
            self.__Signature = Value


    def getProd2Prog(self,Index):
        if(Index == 1):
            return self.__Prod2Prog_ID
        elif(Index == 2):
            return self.__Product_ID
        elif(Index == 3):
            return self.__Program_ID
        elif(Index == 4):
            return self.__Prod2Prog_Status
        elif(Index == 5):
            return self.__PEIProgrID
        elif(Index == 6):
            return self.__Prod2Prog_Status_Code
        elif(Index == 7):
            return self.__Reg_Number
        elif(Index == 8):
            return self.__Reg_Year
        elif(Index == 9):
            return self.__Orig_Reg_Number
        elif(Index == 10):
            return self.__Orig_Reg_Year
        elif(Index == 11):
            return self.__Expiration_Date
        elif(Index == 12):
            return self.__Reg_TS
        elif(Index == 13):
            return self.__Reg_Date
        elif(Index == 14):
            return self.__Reg_Comment
        elif(Index == 15):
            return self.__Reg_Medium_Type
        elif(Index == 16):
            return self.__DCY_F_Individual
        elif(Index == 17):
            return self.__DCY_G_Individual
        elif(Index == 18):
            return self.__DCY_F_Group
        elif(Index == 19):
            return self.__DCY_G_Group
        elif(Index == 20):
            return self.__Signature

#**********************************************************************
    #Handling PROD2PROG_ID
    def setProd2ProgID(self,PP_ID):
        self.__Prod2Prog_ID = PP_ID

    def getProd2ProgID(self):
        return self.__Prod2Prog_ID

#**********************************************************************
    #Handling Product ID
    def setProductID(self,P_ID):
        self.__Product_ID = P_ID

    def getProductID(self):
        return self.__Product_ID
#**********************************************************************
    #Handling PROGRAM_ID
    def setProgramID(self,Pr_ID):
        self.__Program_ID = Pr_ID

    def getProgramID(self):
        return self.__Program_ID
#**********************************************************************
    #PROD2PROG_STATUS
    def setProd2ProgStatus(self,Status):
        self.__Prod2Prog_Status = Status

    def getProd2ProgStatus(self):
        return self.__Prod2Prog_Status

#**********************************************************************
    #PEI_PROGRAM_ID
    def setPEIProgramID(self,PEI_ID):
        self.__PEIProgrID = PEI_ID

    def getPEIProgramID(self):
        return self.__PEIProgrID
#**********************************************************************
    #Handling PROD2PROG_STATUS_CODE
    def setProd2ProgStatusCode(self,S_Code):
        self.__Prod2Prog_Status_Code = S_Code

    def getProd2ProgStatusCode(self):
        return self.__Prod2Prog_Status_Code

#**********************************************************************
    #Handling REGISTRATION_NUMBER
    def setRegNumber(self,R_Number):
        self.__Reg_Number = R_Number

    def getRegNumber(self):
        return self.__Reg_Number

#**********************************************************************

    #Handling REGISTRATION_YEAR
    def setRegYear(self,R_Year):
        self.__Reg_Year = R_Year

    def getRegYear(self):
        return self.__Reg_Year

#**********************************************************************

    #Handling ORIGINAL_REGISTRATION_NUMBER
    def setOrigRegNumber(self,Orig_RegNumber):
        self.__Orig_Reg_Number = Orig_RegNumber

    def getOrigRegNumber(self):
        return self.__Orig_Reg_Number

#**********************************************************************
    #Handling ORIGINAL_REGISTRATION_YEAR
    def setOrigRegYear(self,Orig_RegYear):
        self.__Orig_Reg_Year = Orig_RegYear

    def getOrigRegYear(self):
        return self.__Orig_Reg_Year
#**********************************************************************
    #EXPIRATION_DATE
    def setExpirationDate(self,ExpDate):
        self.__Expiration_Date = ExpDate

    def getExpirationDate(self):
        return self.__Expiration_Date

#**********************************************************************
    #Handling REGISTRATION_TS
    def setRegTS(self,RegTS):
        self.__Reg_TS = RegTS

    def getRegTS(self):
        return self.__Reg_TS

#**********************************************************************
   #REGISTRATION_DATE
    def setRegDate(self,RegDate):
        self.__Reg_Date = RegDate

    def getRegDate(self):
        return self.__Reg_Date

#**********************************************************************
   #REGISTRATION_COMMENT
    def setRegComment(self,RegComment):
        self.__Reg_Comment = RegComment

    def getRegComment(self):
        return self.__Reg_Comment

#**********************************************************************
    #REGISTRATION_MEDIUM_TYPE
    def setRegMediumType(self,RegMediumType):
        self.__Reg_Medium_Type = RegMediumType

    def getRegMediumType(self):
        return self.__Reg_Medium_Type

#**********************************************************************
    #DCY_F_INDIVIDUAL
    def setDCY_F_IND(self,DCY_F):
        self.__DCY_F_Individual = DCY_F

    def getDCY_F_IND(self):
        return self.__DCY_F_Individual

#**********************************************************************
    #DCY_G_INDIVIDUAL
    def setDCY_G_IND(self,DCY_G):
        self.__DCY_G_Individual = DCY_G

    def getDCY_G_IND(self):
        return self.__DCY_G_Individual

#**********************************************************************
    #DCY_F_GROUP
    def setDCY_F_Group(self,DCY_F_Group):
        self.__DCY_F_Group = DCY_F_Group

    def getDCY_F_Group(self):
        return self.__DCY_F_Group
#**********************************************************************
   #DCY_G_GROUP
    def setDCY_G_Group(self,DCY_G_Group):
        self.__DCY_G_Group = DCY_G_Group

    def getDCY_G_Group(self):
        return self.__DCY_G_Group
#**********************************************************************
  #Signature
    def setSignature(self,Signature):
        self.__Signature = Signature

    def getSignature(self):
        return self.__Signature
#**********************************************************************


