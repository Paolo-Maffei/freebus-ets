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
from configobj import ConfigObj            #for application settings

#from pysqlite2 import dbapi2 as sqlite3
import sqlite3

LogFileName = Global.LogPath + 'MainFrame.log'
Options = 0

#Databaseconnection
config = ConfigObj(Global.settingFile)

Global.DatabaseConnection = sqlite3.connect(config['Database'])
Global.DatabaseConnection.text_factory = str

#probably will never be None -> sqlite creats a database if its not connectable...
if(Global.DatabaseConnection == None):
    msgbox = gtk.MessageDialog(parent = self.__window, buttons = gtk.BUTTONS_OK,
                                           flags = gtk.DIALOG_MODAL, type = gtk.MESSAGE_WARNING,
                                           message_format = Global.ERROROPENDATABASE )

    msgbox.set_title(Global.ERROROPENDATABASETITLE)
    result = msgbox.run()
    msgbox.destroy()


LOG_MainFrame = Logging.Logging("FB_MainFrame",LogFileName,Options)


FBMain = FB_MainFrame.FB_MainFrame(LOG_MainFrame)
FBMain.main()

