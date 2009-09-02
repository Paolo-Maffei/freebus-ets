#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_EIBConnection.py
#Version: V0.1 , 28.08.2009
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================

from Global import Global
import socket
import jpype

class FB_EIBConnection(object):

    _individualAddress = None
    _connected = False

    __name = ""                 #name of connection
    __type = 0                  #init Connectiontype
    __isDefault = False         #Defaultconnection
    __COMPort = 0               #index of combo 0 = COM 1
    __ipName = ""
    __ipIP = "192.168.10.1"
    __ipPort = 3671
    __id = 0

    ##Constructor for EIBConnection.
    def __init__(self):
        self.__name = "neue Verbindung"
        self.__isDefault = True
        self.__id = Global.CreateGUID()


    def getID(self):
        return self.__id

    ##set the name of the new connection
    #@param name: new name
    def setName(self,name):
        self.__name = name

    ##get the name of this connection
    #@return: name
    def getName(self):
        return self.__name

    ##set the type of the connection
    #@param type: index of the typebox, corresponding with enumeration
    def setType(self,type):
        self.__type = type

    ##get the type of this connection
    #@return: index of type / enum.value
    def getType(self):
        return self.__type

    ##set the flag as default connection
    #@param isDefault: connection is default connection
    def setDefault(self,isDefault):
        self.__isDefault = isDefault

    ##get the flag to indicate the default connection
    #@return: default-flag
    def getDefault(self):
        return self.__isDefault

    ##set the serial comport
    #@param ComPort:
    def setCOM(self,ComPort):
        self.__COMPort = ComPort

    ##get the enum-value of the comport
    #@return:
    def getCOM(self):
        return self.__COMPort

    #---------------------------------------------------------------
    ##set (host)name of the ip-connection
    #@param ipName:
    def setIpName(self,ipName):
        self.__ipName = ipName

    ##get the hostname of the ip-connection
    #@return:
    def getIpName(self):
        return self.__ipName

    ##set the ip of the ip-connection
    #@param ipName:
    def setIP(self,ip):
        self.__ipIP = ip

    ##get the ip of the ip-connection
    #@return:
    def getIP(self):
        return self.__ipIP

    ##set the port-number of the ip-connection
    #@param port:
    def setIPPort(self,port):
        self.__ipPort = port

    ##get the port-number of the ip-connection
    #@return:
    def getIPPort(self):
        return self.__ipPort

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

    def doConnect(self):
        if self.__type == 0:    #EIBNet/IP
            self.ConnectIP()
        elif self.__type == 1:    #RS232 FT1.2
            pass





    def ConnectIP(self):
        #create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((self.__ipIP, self.__ipPort))
        #get a CRI - connection request information
        CRIclass = jpype.JClass("tuwien.auto.calimero.knxnetip.util.CRI")
        HPAIclass = jpype.JClass("tuwien.auto.calimero.knxnetip.util.HPAI")

        CRI = CRIclass.createRequest(2,[])
        #HPAI = HPAIclass(HPAIclass.IPV4_TCP,socket.gethostname(),3671)
        #socket.getaddrinfo(host, port)
        #HPAI = HPAIclass(2,socket.gethostname())
        #print HPAI


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------


    ##Call this method to add an EIBframeListener for receiving a frame
    ##@param efl the EIBFrameListener
    def addEIBFrameListener(self, efl):
        pass
        #check for double listeners
        #for cnt in range(len(self.listeners)):
        #    if listeners[cnt] == efl:
        #        return
        #self._listeners.append(efl)

    ##Remove a EIBFrameListener
    #@param efl the instance of the Listener you want to remove
    def removeEIBFrameListener(self,efl):
        pass
        #for cnt in range(len(self.listeners)):
        #   if listeners[cnt] == efl:
        #       del listeners[cnt]
        #       return

    ##Returns the individual (physical) address of the EIB interface
    #@return the individual (physical) address of the EIB interface
    def getIndividualAddress(self):
        return self._individualAddress


    def isConnected(self):
        return self._connected

    def setConnected(self,connected):
        self._connected = connected


