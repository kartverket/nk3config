#!/usr/bin/python 
# -*- coding: utf-8 -*-

import json
import xml.etree.ElementTree as ET
import project
import maplayer
import wms
from HTMLParser import HTMLParser
from xml.dom import minidom
#import pprint

def LoadFile(fileName):
  return file.open(fileName)

projectsFolder="../configService/projects/"
cacheUrlStart="https://gatekeeper"
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
    print '\t' + group
    for layerName in data[ansikt]["groups"][group]:
      layerKey="layers"
      layer=data[ansikt]["groups"][group][layerName]
      if((layer["template"] == 'layers/wms') or (layer["template"] == 'layers/wmts')):
        print '\t\t' + layer["template"]
        wmsConfig=wms.Wms()
        
        if (layer["template"] == 'layers/wmts'):
          layerKey="layer"
          if "url" in layer.keys():
            url=layer["url"].replace('?','') + '?LAYERS=' + layer[layerKey]
            wmsConfig.params["url"]=url
          else:
            wmsConfig.params["url"]=cacheUrlStart + "1" + cacheUrlEnd + layer[layerKey] + "|" + cacheUrlStart + "2" + cacheUrlEnd + layer[layerKey]
          wmsConfig.params["type"]="map"
          wmsConfig.params["options"]["isbaselayer"]="true"


        else:
          wmsConfig.params["url"]=layer["url"]
          wmsConfig.params["options"]["singletile"]="true"
          wmsConfig.params["type"]="overlay"
          wmsConfig.params["groupid"]=str(groupid)


        wmsConfig.params["params"]["layers"]=layer[layerKey]
        wmsLayerTitle=HTMLParser().unescape(layer['name'])
        wmsConfig.params["Layers"]["Layer"]["title"]=wmsLayerTitle
        wmsLayerName=HTMLParser().unescape(layer[layerKey])
        wmsConfig.params["Layers"]["Layer"]["name"]=wmsLayerName
        wmsConfig.params["grouptitle"]=str(group)
        layerName=HTMLParser().unescape(layer["name"])
        wmsConfig.params["name"]=layerName
        wmsConfig.params["guid"]=str(groupid) + "." + layer[layerKey]
        if ("getfeature" in layer.keys()):
          wmsConfig.params["Layers"]["Layer"]["queryable"]=str(layer["getfeature"])
        if (layerName.encode('utf-8') in ['Fly­bilder','Elektron. Sjøkart', 'Fly­bilete'] ): 
          wmsConfig.params['options']["isbaselayer"]="true"
        configXml.append(wmsConfig.GetXml())

    groupid+=1

  projextXmlFile=open(projectsFolder + ansikt + '.xml','w')
  xmlstr=minidom.parseString(ET.tostring(configXml, 'utf-8')).toprettyxml(indent="   ")
  projextXmlFile.write(xmlstr.encode('utf-8'))
file=open(projectsFolder + '__projects.json','w')
file.write(json.dumps(projects))
