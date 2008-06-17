#-*- coding: iso-8859-1 -*-
#!/usr/bin/
#===============================================================================
#Source File: Testaufruf.py
#Version: V0.1 vom 25.12.2007
#Autor: Jerome Leisner
#===============================================================================

#Path-structure
#Installation-Path
#    ->    Dist (name of directory of setup procedure
#    ->    Logging
#    ->    src
#            -> GUI
#            -> Image

import os
import sys

from Global import Global
from XML import FB_XMLConverter
from XML import FB_XML_PRODUCT
from XML import FB_XMLDataModel
from LOG import Logging
from GUI import FB_MainFrame




LogFileName = Global.LogPath + 'MainFrame.log'
Options = 0

LOG_MainFrame = Logging.Logging("FB_MainFrame",LogFileName,Options)

FBMain = FB_MainFrame.FB_MainFrame(LOG_MainFrame)
FBMain.main()

