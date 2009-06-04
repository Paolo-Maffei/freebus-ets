#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_AdressLogic.py
#Version: V0.1 , 04.06.2009
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

import os
from xml.dom import minidom
from xml.dom.minidom import *

#from xml.dom.minidom import getDOMImplementation

##general class for handling the entire adresslogic within the project
class FB_AdressLogic:

    __LogObj = None
    __ProjectObj = None
    __ArchModel = None    #obj of the architectural structure of the project

    ##Constructor for new Project
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param projectname: Path and name of project
    def __init__(self, LogObj, ProjectObj):
        self.__LogObj = LogObj
        self.__ProjectObj = ProjectObj
        self.__ArchModel = self.__ProjectObj.getArchModel()

