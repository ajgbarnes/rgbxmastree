from tree import RGBXmasTree
from colorzero import Color
import paho.mqtt.client as mqtt

bright=0.1
currentLED = 0
defaultColor = '#000000'

tree=RGBXmasTree(brightness=bright)

def on_connect(client, obj, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("cheerlightsRGB")
	
def on_message(client, obj, msg):
    global currentLED
    color = msg.payload.decode('UTF-8')
    print(color)
    tree[currentLED].color=Color(color)
    currentLED = (currentLED + 1)%25

def on_log(client, obj, level, msg):
    print(msg)

tree.color=Color(defaultColor)

client = mqtt.Client()
client.on_connect  = on_connect
client.on_message = on_message
#client.on_log = on_log

client.connect("mqtt.cheerlights.com", 1883, 60)

client.loop_forever()
