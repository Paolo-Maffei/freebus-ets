#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_Device.py
#Version: V0.1 , 12.05.2009
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

##general class for containing device data

class FB_Device:

    __LogObj = None
    __ProjObj = None

    ##Constructor
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param ProjObj: current Project Object
    def __init__(self,LogObj, ProjObj):
        self.__LogObj = LogObj
        self.__ProjObj = ProjObj


    def WriteProductDetails(self):
        pass