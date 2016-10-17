import xml.etree.ElementTree as ET

class Vector():
  def __init__(self):
    self.params={}
    self.params["type"]="overlay"
    self.params["guid"]="guid"
    self.params["name"]="name"
#    self.params["gatekeeper"]="true"
    self.params['epsg']="EPSG:4326"

    self.params["options"]={}
#    self.params["options"]["isbaselayer"]="false"
#    self.params["options"]["singletile"]="false"
    self.params["options"]["visibility"]="false"

    self.params["params"]={}
    self.params["params"]["format"]="application/json"
#    self.params["params"]["layers"]="topo2" #used by WMS

#    self.params["Layers"]={}
#    self.params["Layers"]["Layer"]={}
#    self.params["Layers"]["Layer"]["title"]="topografisk norgeskart 2"
#    self.params["Layers"]["Layer"]["name"]="topografisk norgeskart 2"

  def GetXml(self):
    vector=ET.Element("vector")
    for name in self.params.keys():
      if(name=="type"):
        vector.attrib[name]=self.params[name]
        continue
      element=ET.SubElement(vector,name)
      if isinstance(self.params[name], dict):
        for subName in self.params[name].keys():
          subElement=ET.SubElement(element,subName)
          if isinstance(self.params[name][subName], dict):
            for subSubName in self.params[name][subName]:
              subSubElement=ET.SubElement(subElement,subSubName)
              subSubElement.text=self.params[name][subName][subSubName]
          else:
            subElement.text=self.params[name][subName]
      else:
        element.text=self.params[name]
    return vector


