import xml.etree.ElementTree as ET

class Wms():
  def __init__(self):
    self.type="type"
    self.guid="guid"
    self.name="name"
    self.display="false"
    self.gatekeeper="false"
    self.hidden="false"
    self.opencacheurl="Map/GetMap?http://wms.geonorge.no/skwms1/wms.topo2?LAYERS=topo2"
    self.url="http://wms.geonorge.no/skwms1/wms.topo2?"
    self.zindex=0
    self.groupid=0
    self.grouptitle="grouptitle"

    self.options={}
    self.options["isbaselayer"]="false"
    self.options["minscale"]=1000
    self.options["opacity"]=1
    self.options["singletile"]="false"
    self.options["transitioneffect"]="resize"
    self.options["visibility"]="false"

    self.params={}
    self.params["format"]="image/png"
    self.params["layers"]="topo2"
    self.params["bgcolor"]="0x000000"
    self.params["transparent"]="true"

    self.Layers={}
    self.Layers["Layer"]={}
    self.Layers["Layer"]["title"]="topografisk norgeskart 2"
    self.Layers["Layer"]["name"]="topografisk norgeskart 2"
    self.Layers["Layer"]["queryable"]="false"

  def GetXml(self):
    element=ET.Element("type")
    element.text=self.type
    return element
