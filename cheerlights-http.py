from tree import RGBXmasTree
from colorzero import Color
import requests
import time

refreshInterval = 30
bright=0.1
colorUrl = "http://api.thingspeak.com/channels/1417/field/2/last.json"

def on_connect(client, obj, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("cheerlightsRGB")
	
def on_message(client, obj, msg):
    colorValue = msg.payload.decode('UTF-8')
    print(colorValue)
    tree.color=Color(colorValue)

def on_log(client, obj, level, msg):
    print(msg)

tree = RGBXmasTree(brightness=bright)


while True:
    r = requests.get(url=colorUrl)
    print(r)
    color = r.json()['field2']
    print(color)
    tree.color=Color(color)
    time.sleep(refreshInterval)

