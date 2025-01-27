# rgbxmastree

Code examples for the RGB Xmas Tree

## Getting started

Start by downloading the xmas tree file. Open a terminal and type:

```bash
wget https://bit.ly/2Lr9CT3 -O tree.py
```

Install the `colorzero` package
```
sudo apt update
sudo apt install python-colorzero python3-colorzero
```

When you write your own Python code, make sure you keep this file in the same
folder.

Open a Python shell or IDE (like Mu, Thonny or IDLE) and import `RGBXmasTree`:

```python
from tree import RGBXmasTree
```

Initialise your tree:

```python
from tree import RGBXmasTree

tree = RGBXmasTree()
```

## Change the brightness

You can change the brightness from 0 to 1 - the default is 0.5:

```python
from tree import RGBXmasTree

tree = RGBXmasTree(brightness=0.1)
```

You'll find that 1 is _extremely bright_ and even 0.1 is plenty bright enough if
the tree is on your desk :)

## Change the colour

You can set the colour of all the LEDs together using RGB values (all 0-1):

```python
from tree import RGBXmasTree

tree = RGBXmasTree()

tree.color = (1, 0, 0)
```

Alternatively you can use the `colorzero` library:

```python
from tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

tree.color = Color('red')
```

You can write a loop to repeatedly cycle through red, green and blue:

```python
from tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

for color in colors:
    tree.color = color
    sleep(1)
```

## Individual control

You can also control each LED individually, for example turn each one red, one
at a time:

```python
from tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()

for pixel in tree:
    pixel.color = (1, 0, 0)
    sleep(1)
```

To control a specific pixel, you can access it by its index number (0-24):

```python
tree[0].color = (0, 1, 0)
```

## Examples

## RGB cycle

Cycle through red, green and blue, changing all pixels together

- [rgb.py](examples/rgb.py)

### One-by-one

Cycle through red, green and blue, changing pixel-by-pixel

- [onebyone.py](examples/onebyone.py)

### Hue cycle

Cycle through hues forever

- [huecycle.py](examples/huecycle.py)

### Random sparkles

Randomly sparkle all the pixels

- [randomsparkles.py](examples/randomsparkles.py)

### Cheerlights (via HTTP) by ajgbarnes

Subscribes to the colour changes from Cheerlights. CheerLights is an “Internet of Things” project created by Hans Scharler that allows people's lights all across the world to synchronize to one color set by Twitter.  To change the colour, from your Twitter account send a message to @Cheerlights using on of the valid colours described on this page https://cheerlights.com/cheerlights-api/

To run this 
```
python3 cheerlights-http.py
```

- [cheerlights-http.py](cheerlights-http.py)

### Cheerlights History (via HTTP) by ajgbarnes

Similar to Cheerlights (via HTTP) but lights a new led / bauble each time a new colour comes through

To run this 
```
python3 cheerlights-history-http.py
```

- [cheerlights-history-http.py](cheerlights-history-http.py)

### Cheerlights (via MQTT) by ajgbarnes

Similar to Cheerlights (via HTTP) but subscribes to the MQTT feed so you never miss a colour update. MQTT queues them so you get an update every 30 seconds rather than rapidly as they happen.  

To run this 
```
pip3 install paho-mqtt
python3 cheerlights-mqtt.py
```

To autostart this on boot of the Raspberry Pi
```
sudo pip3 install paho-mqtt
python3 /path/to/files/cheerlights.py &
```

- [cheerlights-mqtt.py](cheerlights-mqtt.py)

### Cheerlights History (via MQTT) by ajgbarnes

Similar to Cheerlights (via MQTT) but lights a new led / bauble each time a new colour comes through

To run this 
```
python3 cheerlights-history-mqtt.py
```

- [cheerlights-history-mqtt.py](cheerlights-history-mqtt.py)
