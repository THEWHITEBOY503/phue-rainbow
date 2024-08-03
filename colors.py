#!/usr/bin/python
from phue import Bridge
import logging
import sys
import time as t
import colorsys

logging.basicConfig()
with open('ip.txt', 'r') as file:
    ip_a = file.read().strip()
br = Bridge(ip_a)
with open('ID.txt', 'r') as idfile:
  data = idfile.read()
data = data.strip('[] \n')
lights = [int(x) for x in data.split(',')]

def rainbow():
    # Cycle through the hues (0-1 in steps of 0.01)
    for hue in [i*0.1 for i in range(100)]:
        # Convert the hue to RGB
        R, G, B = colorsys.hsv_to_rgb(hue, 1, 1)
        # The RGB values will be in the range [0, 1], you might want to scale them to [0, 255]
        R, G, B = int(R * 255), int(G * 255), int(B * 255)
        yield [R,G,B]

def rgb_to_xy(RGB):
    # Normalize RGB values to the range 0-1
    R,G,B = RGB
    R = R / 255.0
    G = G / 255.0
    B = B / 255.0

    # Apply gamma correction
    R = pow((R + 0.055) / (1.0 + 0.055), 2.4) if (R > 0.04045) else (R / 12.92)
    G = pow((G + 0.055) / (1.0 + 0.055), 2.4) if (G > 0.04045) else (G / 12.92)
    B = pow((B + 0.055) / (1.0 + 0.055), 2.4) if (B > 0.04045) else (B / 12.92)

    # Convert to XYZ space
    X = R * 0.664511 + G * 0.154324 + B * 0.162028
    Y = R * 0.283881 + G * 0.668433 + B * 0.047685
    Z = R * 0.000088 + G * 0.072310 + B * 0.986039

    # Convert to xy space
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)

    return [x,y]

while True:
    for RGB in rainbow():
        xy = rgb_to_xy(RGB)
        print(xy)
        # Adjust transitiontime=X change the fade time of the light. 
        br.set_light(lights, 'xy', xy, transitiontime=3)
        # Adjust this to change the pause between color steps.
        t.sleep(0.1)

