from tree import RGBXmasTree
from colorzero import Color
import requests
import time

refreshInterval = 30

bright=0.1
feedUrl = "http://api.thingspeak.com/channels/1417/feed.json"

currentColor = '#000000'

tree = RGBXmasTree(brightness=bright)

tree.color=Color('#000000')

while True:
    try: 
        f=requests.get(url=feedUrl)
        length=len(f.json()['feeds'])
        for x in range(25):
            pos=(length-x)-1
            color=f.json()['feeds'][pos]['field2']
            tree[x].color=Color(color)
    except Exception:
        pass
    time.sleep(refreshInterval)
