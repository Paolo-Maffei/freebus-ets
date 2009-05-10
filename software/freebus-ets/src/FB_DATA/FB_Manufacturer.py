#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_Product.py
#Version: V0.1 , 18.11.2007
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##Class for Handling of Freebus-Manufacturer-Data which based from FB XML Product-Files
class FB_Manufacturer:

    __ManID = None     #MANUFACTURER_ID
    __ManName = None   #MANUFACTURER_NAME
    __AddrID = None    #ADDRESS_ID

    def __init__(self):
        pass

    #returns List of all values in a correct sql format
    def getSQLValueList(self):

        List = (self.__ManID,self.__ManName,self.__AddrID)

        return List

    def setManufacturer(self,Index, Value):
        if(Index == 1):
            self.__ManID = Value
        elif(Index == 2):
            self.__ManName = Value
        elif(Index == 3):
            self.__AddrID = Value


    def getManufacturer(self,Index):
        if(Index == 1):
            return self.__ManID
        elif(Index == 2):
            return self.__ManName
        elif(Index == 3):
            return self.__AddrID

#**********************************************************************
    #MANUFACTURER_NAME
    def setManufactName(self,M_Name):
        self.__ManName = M_Name

    def getManufactName(self):
        return self.__ManName
#**********************************************************************
    #MANUFACTURER_ID
    def setManufactID(self,M_ID):
        self.__ManID = M_ID

    def getManufactID(self):
        return self.__ManID

#**********************************************************************
    #ADDRESS_ID
    def setAddressID(self,A_ID):
        self.__AddrID = A_ID

    def getAddressID(self):
        return self.__AddrID

