import xml.etree.ElementTree as ET

class Wms():
  def __init__(self):
    self.params={}
    self.params["type"]="type"
    self.params["guid"]="guid"
    self.params["name"]="name"
    self.params["gatekeeper"]="true"

    self.params["options"]={}
    self.params["options"]["isbaselayer"]="false"
    self.params["options"]["singletile"]="false"
    self.params["options"]["visibility"]="false"

    self.params["params"]={}
    self.params["params"]["format"]="image/png"
    self.params["params"]["layers"]="topo2" #used by WMS

    self.params["Layers"]={}
    self.params["Layers"]["Layer"]={}
    self.params["Layers"]["Layer"]["title"]="topografisk norgeskart 2"
    self.params["Layers"]["Layer"]["name"]="topografisk norgeskart 2"
    self.params["Layers"]["Layer"]["queryable"]="false"

  def GetXml(self):
    wms=ET.Element("wms")
    for name in self.params.keys():
      if(name=="type"):
        wms.attrib[name]=self.params[name]
        continue
      element=ET.SubElement(wms,name)
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
    return wms


