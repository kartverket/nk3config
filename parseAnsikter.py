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

def ReadLayers(layers):
  i=0
  for layer in layers:
    layerUrl=base + branch + '/themes/' + layer + '.yaml'
    layerYaml=GetYaml(layerUrl)
    layerGroup=layerYaml["layerGroup"]
    if layerGroup not in ansikter[ansikt]["layers"].keys():
      ansikter[ansikt]["layers"][layerYaml["layerGroup"]]={}
    ansikter[ansikt]["layers"][layerYaml["layerGroup"]][i]=layerYaml
    i+=1

json_data=open('ansikter.json').read()
data = json.loads(json_data)
ansikter = {}


for ansikt in data["ansikter"]:
  print "Ansikt: " + ansikt

  ansikter[ansikt] = {}

  branch=data["ansikter"][ansikt]
  base=data["urls"]["rawbase"]
  ansikter[ansikt]["index"]=base + branch + data["urls"]["index"]

  indexYaml=GetYaml(ansikter[ansikt]["index"])

  ansikter[ansikt]["baselayers"]=GetYamlNodes(indexYaml["baselayers"], "template")
  overlays=GetYamlNodes(indexYaml["overlays"], "include")
  ansikter[ansikt]["layers"] = {}

  ReadLayers(overlays)
  break
 
pprint.pprint(ansikter)

#  secondary=base + branch + data["urls"]["secondary"]
#  Get(secondary)
