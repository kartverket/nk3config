import xml.etree.ElementTree as ET

class Project():
  def __init__(self):
    self.params={}
    self.params["displayCenter"]="378604,7226208"
    self.params["displaycenterepsgcode"]="EPSG:25833"
    self.params["displayprojectionepsgcode"]=self.params["displaycenterepsgcode"]
    self.params["mapbackgroundcolor"]="#FFFFFF"

  def GetXml(self):
    project=ET.Element("project")
    project.attrib["lon"]=self.params["displayCenter"].split(',')[0]
    project.attrib["lat"]=self.params["displayCenter"].split(',')[1]
    project.attrib["zoom"]="5"
    project.attrib["mapepsg"]=self.params["displaycenterepsgcode"]
    for key in self.params.keys():
     element=ET.SubElement(project, key)
     element.text=self.params[key]
    return project
