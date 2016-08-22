import json
import xml.etree.ElementTree as ET

def LoadFile(fileName):
  return file.open(fileName)

json_data=open('out.json').read()
data = json.loads(json_data)


for project in data:
  print project
  
  displayCenter="378604,7226208"
  sidetitle=project
  headertitle=project
  displaycenterepsgcode="epsg:32633"
  displayprojectionepsgcode=displaycenterepsgcode
  displaysetscale=10
  mapbackgroundcolor="#FFFFFF"
  defaultmunicipality="1804"
  displaymaptype=0
  minimizebuttons="false"
  sak="false"
  showheader="false"
  headericon=""
  showcoordsportable="true"
  displayprojectionprefix="Euref89 UTM"
  defaultkommune="1804"
  searchadresse=17
  searchsted=9
  searchmatr=15
  searchkoord=15
  webservicesUsesinglegiurl="false"

  mapgroups=0
  for group in data[project]["layers"]:
    maplayerGroupid=mapgroups
    maplayerIndex=mapgroups
    maplayerName=group
    
    print '\t' + group
    for layer in data[project]["layers"][group]:
      print '\t\t' + data[project]["layers"][group][layer]["name"]

    mapgroups+=1
