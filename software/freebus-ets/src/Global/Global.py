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



GUIPath = "..\\GUI\\"
ImagePath = "..\\Image\\"
LogPath = "..\\Logging\\"

Prefix = [" ", "Project","Building","Floor", "Room", "Junction"]

#DragNDrop Idendifier
DND_BUILDING = 10
DND_FLOOR = 11
DND_ROOM = 12
DND_JUNCTION = 13