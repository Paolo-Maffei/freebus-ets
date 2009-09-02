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
from random import randint
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
from enum import Enum

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


ConTypes = Enum("Eibnet", "sFT12")
ConTypesText = Enum("Eibnet/IP", "RS232 FT1.2")
COM = Enum("COM 1", "COM 2", "COM 3", "COM 4", "COM 5", "COM 6", "COM 7", "COM 8")

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------  some helping functions --------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def CreateGUID():
        chars = '0123456789abcdef' # Hexadezimalziffern
        clen = len(chars) - 1      # Anzahl verfügbarer Ziffern (Nullbasiert)
        parts = [8, 4, 4, 4, 12]   # Längen der einzelnen GUID-Abschnitte

        # Liste mit den einzelnen GUID-Abschnitten
        guid = []

        # p ist die Länge jedes einzelnen Abschnitts
        for p in parts:
            # Aktuelle Abschnitt initialisieren
            gpart = ''
            # Iteriere von 0 bis zur Länge des aktuellen Abschnitts
            for c in range(0, p):
            # füge ein zufälliges Zeichen aus chars zum aktuellen Abschnitt hinzu
                gpart += chars[randint(0, clen)]
        # hänge den Abschnitt an die GUID-Liste an
        guid.append(gpart)

        return guid[0]
