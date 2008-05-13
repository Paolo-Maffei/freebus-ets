#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_InstallationDataModel.py
#Version: V0.1 , 12.05.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================


from xml.dom import minidom
from xml.dom.minidom import *
from XML.FB_XMLDataModel import FB_XMLDataModel #import class as base class
import os


##general class for handling project data which are based on XML
class FB_InstallationDataModel(FB_XMLDataModel):


    __LogObj = None
    __DOMObj = None
    __ROOT_ID = ""
    __instDocument = None
    __PATH = ""         #Project Path
    __sensorsNode = None
    __actuatorsNode = None
    __passiveNode = None

    ##Constructor
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param projectname: Path and name of project
    def __init__(self, LogObj, InstDocument,projectname, new):
        #FB_XMLDataModel.__init__(self,LogObj,InstDocument,projectname)

        self.__LogObj = LogObj
        self.__instDocument = InstDocument

        #archNode = Document.appendChild(Document.createElement("architectural-data"))
        #find mainnode "installation-components"
        if(new == True):
            instNode = self.__instDocument.documentElement

            activeNode = instNode.appendChild(self.__instDocument.createElement("active-components"))
            self.__sensorsNode = activeNode.appendChild(self.__instDocument.createElement("sensors"))
            self.__actuatorsNode = activeNode.appendChild(self.__instDocument.createElement("actuators"))
            self.__passiveNode = instNode.appendChild(self.__instDocument.createElement("passive-components"))

            OutFileObj = open("installation.xml","w")
            String = self.__instDocument.toxml(encoding = "ISO-8859-1")
            OutFileObj.write(String)
            OutFileObj.close()


#****************************************************************************
    def SaveInstmodel(self):
        os.chdir(self.getProjectPath())
        OutFileObj = open("installation.xml","w")
        String = self.__instDocument.toxml(encoding = "ISO-8859-1")
        OutFileObj.write(String)
        OutFileObj.close()
