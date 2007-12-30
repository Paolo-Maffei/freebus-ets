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

    __ManName = ""  #MANUFACTURER_NAME
    __ManID = ""    #MANUFACTURER_ID

    def __init__(self):
        pass

#**********************************************************************
    #MANUFACTURER_NAME
    def setManufactName(self,M_Name):
        self.__ManName = M_Name

    def getManufactName(self):
        return self.__ManName
#**********************************************************************
    #MANUFACTURER_ID
    def setManufactID(self,M_ID):
        self.__Manufacturer_ID = M_ID

    def getManufactID(self):
        return self.__Manufacturer_ID

