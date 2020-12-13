from tree import RGBXmasTree
from colorzero import Color
import paho.mqtt.client as mqtt

bright=0.25

def on_connect(client, obj, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("cheerlightsRGB")
	
def on_message(client, obj, msg):
    colorValue = msg.payload.decode('UTF-8')
    print(colorValue)
    tree.color=Color(colorValue)
    print(msg.topic)

def on_log(client, obj, level, msg):
    print(msg)

tree = RGBXmasTree(brightness=bright)

client = mqtt.Client()
client.on_connect  = on_connect
client.on_message = on_message
#client.on_log = on_log

client.connect("mqtt.cheerlights.com", 1883, 60)
client.subscribe("cheerlightsRGB")

client.loop_forever()
