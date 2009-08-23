#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: Global.py
#Version: V0.1 , 16.03.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

#Global deklarations used in entire ets

#add Directory Structure
#GUI Path
import os

import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade

GUIPath = "..\\GUI_Res\\"
ImagePath = "..\\GUI_Res\\"
LogPath = "..\\Logging\\"
dataPath = "..\\data\\"
Database = "..\\data\\Freebus.db"
settingFile = "..\\data\\settings.txt"
GladeFile = "freebus.glade"


Prefix = [" ", "Project","Building","Floor", "Room", "Junction"]
DatabaseConnection = None        #general Databaseobjects

#DragNDrop Idendifier
DND_PROJECT = 1
DND_BUILDING = 2
DND_FLOOR = 3
DND_ROOM = 4
DND_JUNCTION = 5

QUITTWITHOUTSAVE = U"Das Projekt wurde noch nicht gespeichert. \nMöchten Sie Ihre Daten jetzt speichern oder sofort beenden?"
QUITMSGTITLE = U"Warnung vor Datenverlust"

DATATBASEEXIST = U"Es gibt bereits eine Datenbank mit diesem Namen. Möchsten Sie diese überschreiben ?"
DATATBASEEXISTTITLE = U"Datenbank bereits vorhanden"

ERROROPENDATABASE = U"Die in der settings-Datei angegebene Datenbank konnte nicht geöffnet werden! Überprüfen Sie die Einstellungen."
ERROROPENDATABASETITLE = U"Datenbank nicht vorhanden"

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------  some helping functions --------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


