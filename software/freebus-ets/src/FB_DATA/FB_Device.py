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
        clen = len(chars) - 1      # Anzahl verf�gbarer Ziffern (Nullbasiert)
        parts = [8, 4, 4, 4, 12]   # L�ngen der einzelnen GUID-Abschnitte

        # Liste mit den einzelnen GUID-Abschnitten
        guid = []

        # p ist die L�nge jedes einzelnen Abschnitts
        for p in parts:
            # Aktuelle Abschnitt initialisieren
            gpart = ''
            # Iteriere von 0 bis zur L�nge des aktuellen Abschnitts
            for c in range(0, p):
            # f�ge ein zuf�lliges Zeichen aus chars zum aktuellen Abschnitt hinzu
                gpart += chars[randint(0, clen)]
        # h�nge den Abschnitt an die GUID-Liste an
        guid.append(gpart)

        return guid[0]