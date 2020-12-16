from tree import RGBXmasTree
from colorzero import Color
import requests
import time

refreshInterval = 30
bright=0.1
colorUrl = "http://api.thingspeak.com/channels/1417/field/2/last.json"

tree = RGBXmasTree(brightness=bright)


while True:
    r = requests.get(url=colorUrl)
    print(r)
    color = r.json()['field2']
    print(color)
    tree.color=Color(color)
    time.sleep(refreshInterval)

