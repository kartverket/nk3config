#!/usr/bin/python 
import json
import xml.etree.ElementTree as ET
import project
import maplayer
import wms

def LoadFile(fileName):
  return file.open(fileName)

json_data=open('out.json').read()
data = json.loads(json_data)

for ansikt in data:
  print ansikt
  projectConfig=project.Project()
  projectConfig.sidetitle=ansikt
  projectConfig.headertitle=ansikt
  groupid=0
  baselayer=data[ansikt]["baselayers"]
  for group in data[ansikt]["groups"]:
    maplayerConfig=maplayer.Maplayer()
    maplayerConfig.groupid=groupid
    maplayerConfig.index=groupid
    maplayerConfig.name=group
    projectConfig.maplayer.append(maplayerConfig)
    print '\t' + group
    for layerName in data[ansikt]["groups"][group]:
      layer=data[ansikt]["groups"][group][layerName]
      print '\t\t' + layer["name"]
      if(layer["template"] == 'layers/wms'):
        print '\t\tWMS'
        wmsConfig=wms.Wms()
        wmsConfig.type="overlay"
        wmsConfig.groupid=groupid
        wmsConfig.url=layer["url"] + " " + layer["layers"]
        wmsConfig.opencacheurl="Map/GetMap?" + layer["url"] + " " + layer["layers"]
        wmsConfig.grouptitle=group
        wmsConfig.name=layer["name"]
        wmsConfig.params["Layers"]=layer["layers"]
        wmsConfig.Layers["Layer"]["title"]=layer["layers"]
        wmsConfig.Layers["Layer"]["name"]=layer["layers"]
        if ("getfeature" in layer.keys()):
          print "\t\tgetfeature: " + str(layer["getfeature"])
          wmsConfig.Layers["Layer"]["queryable"]=layer["getfeature"]
        print wmsConfig.GetXml().text

      elif(layer["template"] == 'layers/wmts'):
        print '\t\tWMTS'

      else:
        print '\t\t' + layer["template"]

    groupid+=1
