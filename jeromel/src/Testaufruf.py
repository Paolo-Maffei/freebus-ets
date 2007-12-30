#-*- coding: iso-8859-1 -*-
#!/usr/bin/
#===============================================================================
#Source File: Testaufruf.py
#Version: V0.1 vom 25.12.2007
#Autor: Jerome Leisner
#===============================================================================

from XML import FB_XMLConverter
from XML import FB_XML
from LOG import Logging




LogFileName = "J:/Elektronik/Projekte/EIB/ETS for Freebus/Log/XMLLog.log"
Options = 0

LOG_XML = Logging.Logging("XML_Converter",LogFileName,Options)


LogFileName = "J:/Elektronik/Projekte/EIB/ETS for Freebus/Log/FB_XMLLog.log"
Options = 0

LOG_XML = Logging.Logging("FB_XML",LogFileName,Options)

file = "J:/Elektronik/Projekte/EIB/ETS for Freebus/SunXML.xml"

XML = FB_XMLConverter.FB_XMLConverter("J:/Elektronik/Projekte/EIB/ETS for Freebus/CSuntracer2.vd_", \
                                  file, LOG_XML)

#XML.convertToXML()


#"J:/Elektronik/Projekte/EIB/ETS for Freebus/SuntracerXML.xml",
FB_XML = FB_XML.FB_XML(LOG_XML)

#productList = FB_XML.getProducts(file)

#AppList = FB_XML.getApplications(file)

#create parse-object and parse xml-file -> all sub-handler will be called automatically
XMLHandler = FB_XML.parseXMLFile(file)

if(XMLHandler != -1):
    #Product-List
    productList = FB_XML.getProducts(XMLHandler)
    #Applications/Manufacturer-List
    AppManList = FB_XML.getApplications(XMLHandler)

    print productList[0].getProductName()
    print AppManList[0][0].getProgramName()
    print AppManList[1][0].getManufactName()
else:
    print "geht nicht"

#ende =  len(AppManList[0])
#print ende
#for i in range(ende):
#    print AppList[0][i].getProgramID()
#    print AppList[0][i].getSymbolID()
#    print AppList[0][i].getMaskID()
#    print AppList[0][i].getProgramName()
#    print AppList[0][i].getProgramV()
#    print AppList[0][i].getProgramVNo()
#    print AppList[0][i].getLinkable()
#    print AppList[0][i].getDeviceType()
#    print AppList[0][i].getPEIType()
#    print AppList[0][i].getAddrTabSize()
#    print AppList[0][i].getAssTabAddr()
#    print AppList[0][i].getComTabAddr()
#    print AppList[0][i].getComTabSize()
#    print AppList[0][i].getProgramSN()
#    print AppList[0][i].getAppManufacID()
#    print AppList[0][i].getEEPRPOMData()
#    print AppList[0][i].getDataLength()
#    print AppList[0][i].getS19File()
#    print AppList[0][i].getMapFile()
#    print AppList[0][i].getAssID()
#    print AppList[0][i].getHelpFileName()
#    print AppList[0][i].getContextID()
#    print AppList[0][i].getDynMng()
#    print AppList[0][i].getProgramType()
#    print AppList[0][i].getRamSize()
#    print AppList[0][i].getOrigManID()
#    print AppList[0][i].getAPIVersion()
#    print AppList[0][i].getProgramStyle()
#    print AppList[0][i].getPollingMaster()
#    print AppList[0][i].getPollingGroups()
#    print AppList[0][i].getAllowETS()
#    print AppList[0][i].getMinETS()

#ende =  len(AppList[1])
#for i in range(ende):
#    print AppList[1][i].getManufactName()
#    print AppList[1][i].getManufactID()

#ende = len(productList)

#for i in range(ende):
#    print productList[i].getProductID()
#    print productList[i].getManufactuerID()
#    print productList[i].getSymbolID()
#    print productList[i].getProductName()
#    print productList[i].getProductVersion()
#    print productList[i].getCompType()
#    print productList[i].getCompAttr()
#    print productList[i].getBusCurrent()
#    print productList[i].getProductSN()
 #   print productList[i].getCompTypeNo()
 #   print productList[i].getProductPic()
#    print productList[i].getBCUType()
#    print productList[i].getProductHandling()
#    print productList[i].getProductDLL()
 #   print productList[i].getOrigManID()


