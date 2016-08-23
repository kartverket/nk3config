#!/usr/bin/python 
import json
import xml.etree.ElementTree as ET
import project
import maplayer
import wms
from xml.dom import minidom
#import pprint

def LoadFile(fileName):
  return file.open(fileName)

cacheUrl="http://gatekeeper1.geonorge.no/BaatGatekeeper/gk/gk.cache?"
json_data=open('out.json').read()
data = json.loads(json_data)

for ansikt in data:
  print ansikt
  projectConfig=project.Project()
  projectConfig.sidetitle=ansikt
  projectConfig.headertitle=ansikt
  projectXml=projectConfig.GetXml()

  groupid=0
  baselayer=data[ansikt]["baselayers"]
  for group in data[ansikt]["groups"]:
    maplayerConfig=maplayer.Maplayer()
    maplayerConfig.params["groupid"]=str(groupid)
    maplayerConfig.params["index"]=str(groupid)
    maplayerConfig.params["name"]=group
    projectXml.append(maplayerConfig.GetXml())
#    projectConfig.params["maplayer"].append(maplayerConfig)
    print '\t' + group
    for layerName in data[ansikt]["groups"][group]:
      layerKey="layers"
      layer=data[ansikt]["groups"][group][layerName]
#      print '\t\t' + layer["name"]
      if((layer["template"] == 'layers/wms') or (layer["template"] == 'layers/wmts')):
#        print '\t\tWMS'
        wmsConfig=wms.Wms()
        wmsConfig.params["groupid"]=str(groupid)
        
        if (layer["template"] == 'layers/wmts'):
          layerKey="layer"
          wmsConfig.params["url"]=cacheUrl + " " + layer[layerKey]
          wmsConfig.params["type"]="map"
        else:
          wmsConfig.params["url"]=layer["url"] + " " + layer[layerKey]
          wmsConfig.params["type"]="overlay"
        wmsConfig.params["opencacheurl"]="Map/GetMap?" + wmsConfig.params["url"]
        wmsConfig.params["params"]["Layers"]=layer[layerKey]
        wmsConfig.params["Layers"]["Layer"]["title"]=layer[layerKey]
        wmsConfig.params["Layers"]["Layer"]["name"]=layer[layerKey]
        wmsConfig.params["grouptitle"]=str(group)
        wmsConfig.params["name"]=layer["name"]
        if ("getfeature" in layer.keys()):
#          print "\t\tgetfeature: " + str(layer["getfeature"])
          wmsConfig.params["Layers"]["Layer"]["queryable"]=str(layer["getfeature"])

        projectXml.append(wmsConfig.GetXml())
#        print minidom.parseString(ET.tostring(projectConfig.GetXml())).toprettyxml(indent="   ")
#        ET.dump(wmsConfig.GetXml())

#      elif(layer["template"] == 'layers/wmts'):
#        print '\t\tWMTS'

#      else:
#        print '\t\t' + layer["template"]

    groupid+=1

  projextXmlFile=open('xml/' + ansikt + '.xml','w')
  projextXmlFile.write(minidom.parseString(ET.tostring(projectXml)).toprettyxml(indent="   "))
