#!/usr/bin/python
import json
import yaml
import urllib
import pprint


def GetYaml(url):
  stream=urllib.urlopen(url).read()
  try:
    if '---' in stream:
      return yaml.load(stream.split('---')[1])
    return yaml.load(stream)
  except yaml.YAMLError as exc:
    print(exc)

def GetYamlNodes(yaml, name):
  nodes = []
  for node in yaml:
    nodes.append(node[name])
  return nodes

def GetLayers(layers):
  i=0
  for layer in layers:
    layerUrl=base + branch + '/themes/' + layer + '.yaml'
    layerYaml=GetYaml(layerUrl)
    layerGroup=layerYaml["layerGroup"]
    if layerGroup not in ansikter[branch]["groups"].keys():
      ansikter[branch]["groups"][layerYaml["layerGroup"]]={}
    ansikter[branch]["groups"][layerYaml["layerGroup"]][i]=layerYaml
    i+=1

def GetBaseLayers():
  baselayers=GetYamlNodes(indexYaml["baselayers"], "template")
  return baselayers 

json_data=open('ansikter.json').read()
data = json.loads(json_data)
ansikter = {}


for ansikt in data["ansikter"]:
  print "Ansikt: " + ansikt

  branch=data["ansikter"][ansikt]
  ansikter[branch] = {}

  base=data["urls"]["rawbase"]

  indexYaml=GetYaml(base + branch + data["urls"]["index"])
#  secondaryYaml=GetYaml(secondary=base + branch + data["urls"]["secondary"])

  ansikter[branch]["baselayers"]=GetBaseLayers()
  overlays=GetYamlNodes(indexYaml["overlays"], "include")
  ansikter[branch]["groups"] = {}

  GetLayers(overlays)
#  break
 
pprint.pprint(ansikter)
file=open('out.json','w')
file.write(json.dumps(ansikter))
#  secondary=base + branch + data["urls"]["secondary"]
#  Get(secondary)
