#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ArchitecturalTreeModel.py
#Version: V0.1 , 24.02.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

class FB_ArchitecturalTreeModel:

    __LogObj = None
    __ArchModel = None

    ##Constructor
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param PrjObj: Project Object
    def __init__(self,LogObj, PrjObj):
        self.__LogObj = LogObj
