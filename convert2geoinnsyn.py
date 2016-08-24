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

cacheUrlStart="http://gatekeeper"
cacheUrlEnd=".geonorge.no/BaatGatekeeper/gk/gk.cache?LAYERS="
json_data=open('out.json').read()
data = json.loads(json_data)
projects=[]

for ansikt in data:
  projectHeader={
  "ProjectName":ansikt,"SiteTitle":ansikt,"HeaderIcon":"","HeaderTitle":ansikt
  }
  projects.append(projectHeader)
  print ansikt
  configXml=ET.Element('config')
  projectConfig=project.Project()
  projectConfig.sidetitle=ansikt
  projectConfig.headertitle=ansikt
  projectXml=projectConfig.GetXml()
  configXml.append(projectXml)
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
        print '\t\t' + layer["template"]
        wmsConfig=wms.Wms()
        
        if (layer["template"] == 'layers/wmts'):
          layerKey="layer"
          wmsConfig.params["url"]=cacheUrlStart + "1" + cacheUrlEnd + layer[layerKey] + "|" + cacheUrlStart + "2" + cacheUrlEnd + layer[layerKey]
          wmsConfig.params["type"]="map"
          wmsConfig.params["visibility"]="true"
          wmsConfig.params["options"]["isbaselayer"]="true"


        else:
          wmsConfig.params["url"]=layer["url"].replace('?','') + "?LAYERS=" + layer[layerKey]
          wmsConfig.params["options"]["singletile"]="true"
          wmsConfig.params["type"]="overlay"
          wmsConfig.params["groupid"]=str(groupid)


        wmsConfig.params["opencacheurl"]="Map/GetMap?" + cacheUrlStart + "1" + cacheUrlEnd + layer[layerKey]
        wmsConfig.params["params"]["layers"]=layer[layerKey]
        wmsConfig.params["Layers"]["Layer"]["title"]=layer[layerKey]
        wmsConfig.params["Layers"]["Layer"]["name"]=layer[layerKey]
        wmsConfig.params["grouptitle"]=str(group)
        wmsConfig.params["name"]=layer["name"]
        wmsConfig.params["guid"]=str(groupid) + "." + layer["name"]
        if ("getfeature" in layer.keys()):
#          print "\t\tgetfeature: " + str(layer["getfeature"])
          wmsConfig.params["Layers"]["Layer"]["queryable"]=str(layer["getfeature"])

        configXml.append(wmsConfig.GetXml())
#        print minidom.parseString(ET.tostring(projectConfig.GetXml())).toprettyxml(indent="   ")
#        ET.dump(wmsConfig.GetXml())

#      elif(layer["template"] == 'layers/wmts'):
#        print '\t\tWMTS'

#      else:
#        print '\t\t' + layer["template"]

    groupid+=1

  projextXmlFile=open('norgeskart3/MapServices/' + ansikt + '.xml','w')
  projextXmlFile.write(minidom.parseString(ET.tostring(configXml)).toprettyxml(indent="   "))
file=open('norgeskart3/MapServices/__projects.json','w')
file.write(json.dumps(projects))
