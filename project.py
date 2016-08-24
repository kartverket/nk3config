import xml.etree.ElementTree as ET

class Project():
  def __init__(self):
    self.params={}
    self.params["displayCenter"]="378604,7226208"
    self.params["sidetitle"]="sideTitle"
    self.params["headertitle"]="headerTitle"
    self.params["displaycenterepsgcode"]="EPSG:32633"
    self.params["displayprojectionepsgcode"]=self.params["displaycenterepsgcode"]
    self.params["displaysetscale"]="10"
    self.params["mapbackgroundcolor"]="#FFFFFF"
    self.params["defaultmunicipality"]="1804"
    self.params["displaymaptype"]="0"
    self.params["minimizebuttons"]="false"
    self.params["sak"]="false"
    self.params["showheader"]="false"
    self.params["headericon"]=""
    self.params["showcoordsportable"]="true"
    self.params["displayprojectionprefix"]="Euref89 UTM"
    self.params["defaultkommune"]="1804"
    self.params["searchadresse"]="17"
    self.params["searchsted"]="9"
    self.params["searchmatr"]="15"
    self.params["searchkoord"]="15"
    self.params["webservicesUsesinglegiurl"]="false"

  def GetXml(self):
    project=ET.Element("project")
    project.attrib["lon"]=self.params["displayCenter"].split(',')[0]
    project.attrib["lat"]=self.params["displayCenter"].split(',')[1]
    project.attrib["zoom"]=self.params["displaysetscale"]
    project.attrib["mapepsg"]=self.params["displaycenterepsgcode"]
    for key in self.params.keys():
     element=ET.SubElement(project, key)
     element.text=self.params[key]
    return project
