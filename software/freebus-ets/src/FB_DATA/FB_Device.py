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

from random import randint


##general class for containing device data

class FB_Device:

    __LogObj = None
    __ProjObj = None
    __InstanceID = None

    __ProductID = None
    __ProgramID = None


    ##Constructor
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param ProjObj: current Project Object
    def __init__(self,LogObj, ProjObj):
        self.__LogObj = LogObj
        self.__ProjObj = ProjObj

        self.__InstanceID = self.CreateGUID()


    def WriteProductDetails(self):
        pass

    def CreateGUID(self):
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