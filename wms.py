import xml.etree.ElementTree as ET

class Wms():
  def __init__(self):
    self.params={}
    self.params["type"]="type"
    self.params["guid"]="guid"
    self.params["name"]="name"
    self.params["display"]="false"
    self.params["gatekeeper"]="false"
    self.params["hidden"]="false"
    self.params["opencacheurl"]="Map/GetMap?http://wms.geonorge.no/skwms1/wms.topo2?LAYERS=topo2"
    self.params["url"]="http://wms.geonorge.no/skwms1/wms.topo2?"
    self.params["zindex"]="0"
    self.params["groupid"]="0"
    self.params["grouptitle"]="grouptitle"

    self.params["options"]={}
    self.params["options"]["isbaselayer"]="false"
    self.params["options"]["minscale"]="1000"
    self.params["options"]["opacity"]="1"
    self.params["options"]["singletile"]="false"
    self.params["options"]["transitioneffect"]="resize"
    self.params["options"]["visibility"]="false"

    self.params["params"]={}
    self.params["params"]["format"]="image/png"
    self.params["params"]["layers"]="topo2"
    self.params["params"]["bgcolor"]="0x000000"
    self.params["params"]["transparent"]="true"

    self.params["Layers"]={}
    self.params["Layers"]["Layer"]={}
    self.params["Layers"]["Layer"]["title"]="topografisk norgeskart 2"
    self.params["Layers"]["Layer"]["name"]="topografisk norgeskart 2"
    self.params["Layers"]["Layer"]["queryable"]="false"

  def looper(self,dictionary,element):
    for key in dictionary.keys():
      subElement=ET.SubElement(element,key)
      if isinstance(dictionary[key], dict):
        subElement.insert(0,looper(dictionary[key], subElement))
      else:
        subElement.text=dictionary[key]
    return subElement

  def GetXml(self):
    wms=ET.Element("wms")
    #wms.insert(0,self.looper(wms, self.params))
    #return wms
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


