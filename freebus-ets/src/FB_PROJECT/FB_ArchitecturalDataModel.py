#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_ArchitecturalDataModel.py
#Version: V0.1 , 27.01.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================


from xml.dom import minidom
from xml.dom.minidom import *
from XML.FB_XMLDataModel import FB_XMLDataModel #import class as base class


##general class for handling project data which are based on XML
class FB_ArchitecturalDataModel(FB_XMLDataModel):


    __LogObj = None
    __DOMObj = None
    __ROOT_ID="project-1"
    __PROJECT_PREFIX="project"
    __BUILDING_PREFIX="building"
    __FLOOR_PREFIX="floor"
    __ROOM_PREFIX="room"
    __JUNCTION_BOX_PREFIX="junctionbox"

    ##Constructor
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param projectname: Path and name of project
    def __init__(self, LogObj, projectname):
        FB_XMLDataModel.__init__(self,LogObj,projectname)

        self.__LogObj = LogObj
        Document = self.getDOMObj()

        #archNode = Document.appendChild(Document.createElement("architectural-data"))
        #find mainnode "architectural-data"
        archNode = Document.documentElement
        pNode = archNode.appendChild(Document.createElement("project"))

        pNode.setAttribute("id", self.__ROOT_ID)
        pNode.appendChild(Document.createElement("name")).appendChild(Document.createTextNode(projectname))
        pNode.appendChild(Document.createElement("comment"))
        pNode.appendChild(Document.createElement("directoryname")).appendChild(Document.createTextNode(self.makeProjectDirectoryName()))
        pNode.appendChild(Document.createElement("preffered-bus-system"))

        #save to file
        OutFileObj = open(projectname,"w")
        String = Document.toxml(encoding = "ISO-8859-1")
        OutFileObj.write(String)
        OutFileObj.close()

          #return name

    def makeProjectDirectoryName(self):
        name = self.getProjectName()
        name = name.replace(" ", "_")

        return name
