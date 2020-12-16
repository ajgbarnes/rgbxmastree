from tree import RGBXmasTree
from colorzero import Color
import requests
import time

refreshInterval = 30

bright=0.1
colorUrl = "http://api.thingspeak.com/channels/1417/field/2/last.json"

currentLED = 0
currentColor = '#000000'

tree = RGBXmasTree(brightness=bright)

tree.color=Color('#000000')

while True:
    r = requests.get(url=colorUrl)
    color = r.json()['field2']
    print(color)
    if(color != currentColor):
       tree[currentLED].color=Color(color)
       currentColor = color
       currentLED = (currentLED +1)%25
    time.sleep(refreshInterval)
