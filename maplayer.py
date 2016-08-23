import xml.etree.ElementTree as ET

class Maplayer():
  def __init__(self):
    self.params={}
    self.params["name"]=""
    self.params["groupid"]="0"
    self.params["index"]="0"
    self.params["vectorlayer"]=""
    self.params["overlaylayer"]=""

  def GetXml(self):
    maplayer=ET.Element("maplayer")
    for key in self.params.keys():
     element=ET.SubElement(maplayer, key)
     element.text=self.params[key]
    return maplayer

