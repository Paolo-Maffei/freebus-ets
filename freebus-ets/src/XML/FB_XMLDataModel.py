#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_XMLDataModel.py
#Version: V0.1 , 22.01.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================


from xml.dom import minidom
from xml.dom.minidom import *


##general class for handling project data which are based on XML
class FB_XMLDataModel:

    __LogObj = None
    __DOMObj = None

    ##Constructor for an empty
    #@param LogObj: Log-File-Object to log all events within this inctance
    #@param projectname: Path and name of project
    def __init__(self,LogObj, projectname):
        self.__LogObj = LogObj
        #create an DOMObj
        Start = """<?xml version=\"1.0\" ?>\n
                <architectural-data></architectural-data>"""
        self.__DOMObj = minidom.parseString(Start)


    ##return the current DOM-Object
    def getDOMObj(self):
        return self.__DOMObj

    ##sets a document
    def setDOMObj(self,document):
        self.__DOMObj = document

    #remove data with the given ID
    def removeData(self,ID):
        Node=self.getDataRootNode(ID)
        Parent = Node.ParentNode()
        Parent.removeChild(Node)

    #get the name of a Node
    def getName(self,ID):
        Node = self.getDataRootNode(ID)
        return  "" #this.readDOMNodeValue(Node, new StringTokenizer("name", "/"));

    #set the name of Node
    def setName(self,ID,Name):
        Node = self.getDataRootNode(ID)
         #this.writeDOMNodeValue(n, new StringTokenizer("name", "/"), name);

    #get comment
    def getComment(self, ID):
        Node = self.getDataRootNode(ID)
        return "" #this.readDOMNodeValue((Element)n, new StringTokenizer("comment", "/"));

    #set comment
    def setComment(self,ID,Comment):
        Node = self.getDataRootNode(ID)
        #this.writeDOMNodeValue(n, new StringTokenizer("comment", "/"), comment);


    ##Return the id list for all child nodes with namen name from the given stat node
    #@param node the start node
    #@param childname the child node name
    #@return the id String collection
    def getIDList(self,Node,ChildName):
        NodeList = Node.getElementsByTagName(Childname)

        IDList = []
        for i in range(len(NodeList)):
            Element = NodeList.item(i)
            if(Element.hasAttribute("id")):
                IDList.append(Element.getAttribute("id"))

        return IDList

    ##Create a new standard child data node. This node includes a name with id and a comment tag.
    #@param tagname the child root tag name
    #@return the DOM Element
    def createChild(self,TagName):
        Element = self.__DOMObj.createElement(TagName)

        id = tagname+"-" + self.getNewID(TagName)  # get id for the child
        Element.setAttribute("id", id)

        Element.appendChild(self.__DOMObj.createElement("name"))
        Element.appendChild(self.__DOMObj.createElement("comment"))

        return Element

    ##@return the child id for the given child node
    def getChildID(self, ChildNode):
        return ChildNode.getAttribute("id")

    ##Returns an ID number for a new child node
    def getNewID(self, TagName):
        NodeList = self.__DOMObj.getElementsByTagName(TagName)

        # calculate maximum value
        max=0

        for i in range(len(NodeList)):
            Element = NodeList.item(i)
            if(Element.hasAttribute("id")):
                idstr = Element.getAttribute("id")
                prefix = TagName + "-"
                number = idstr.replace(prefix, "")
                if(int(number) > max):
                    max = int(number)
        return max + 1    # return maximum + 1


    ##Returns the root node with the given id
    def getDataRootNode(self,ID):
        drNode = None

        end = ID.find('-')         #find first character "-"

        NodeName = ""

        if(end <> -1):
            NodeName = ID[0, end]
        else:
            NodeName = ID

        NodeList = self.__DOMObj.getElementsByTagName(NodeName)

        if(len(NodeList) > 0):
            for i in range(len(NodeList)):
                Node = NodeList.item(i)
                attr = Node.getAttributes()

                if(attr <> ""):
                    idNode = None
                    idNode = attr.getNamedItem("id")
                    if(idNode <> None):
                        if(idNode.getNodeValue() == ID):
                            drNode = Node
                            break

        return drNode

    #Writes the node value for the node given in the StringTokenizer path. If no such node exists it will created.
    #@param n path root node
    #@param path path to the node
    #@param value the value that will be written
    def writeDOMNodeValue(self, Node, Path, Value):
        self.writeNodeValue(Node, Path, Value)
        self.__DOMObj.normalize()


    #Recursively DFS method for writing node values. If no such nod exists the method creates them.
    def writeNodeValue(self, Node, Path, Value):
        pass
#        if(n.getChildNodes()==null)
#                Node ne=n.appendChild(n.getOwnerDocument().createElement(next)); // build tag
#                writeNodeValue(ne, path, value);

#            else
#                NodeList nl=n.getChildNodes();
 #               boolean found=false;

  #              for(int i=0; i<nl.getLength(); i++)
   #                 if(nl.item(i).getNodeName().equals(next))
    #                    found=true;
     #                   writeNodeValue(nl.item(i), path, value);
     #                   break;
#                if(!found)
#                    Node nu=n.appendChild(n.getOwnerDocument().createElement(next));
#                    writeNodeValue(nu, path, value);
#        else // end of path
#            if(n.hasChildNodes())
#                if(n.getChildNodes().item(0).getNodeType()==Node.TEXT_NODE)
#                    n.getChildNodes().item(0).setNodeValue(value);
#                    return;
#                else

 #                   n.appendChild(n.getOwnerDocument().createTextNode(value));

#                    return;
#            else
#                n.appendChild(n.getOwnerDocument().createTextNode(value));
#                return;

