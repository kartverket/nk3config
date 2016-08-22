#!/usr/bin/python 
import json
import xml.etree.ElementTree as ET
import project
import maplayer

def LoadFile(fileName):
  return file.open(fileName)

json_data=open('out.json').read()
data = json.loads(json_data)

for ansikt in data:
  print ansikt
  projectConfig=project.Project()
  projectConfig.sidetitle=ansikt
  projectConfig.headertitle=ansikt
  mapgroups=0
  baselayer=data[ansikt]["baselayers"]
  for group in data[ansikt]["groups"]:
    maplayerConfig=maplayer.Maplayer()
    maplayerConfig.groupid=mapgroups
    maplayerConfig.index=mapgroups
    maplayerConfig.name=group
    projectConfig.maplayer.append(maplayerConfig)
    print '\t' + group
    for layer in data[ansikt]["groups"][group]:
      print '\t\t' + data[ansikt]["groups"][group][layer]["name"]
      if(data[ansikt]["groups"][group][layer]["template"] == 'layers/wms'):
        print '\t\tWMS'
      elif(data[ansikt]["groups"][group][layer]["template"] == 'layers/wmts'):
        print '\t\tWMTS'
      else:
        print '\t\tVector'

    mapgroups+=1
