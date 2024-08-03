#!/usr/bin/python
from phue import Bridge
import logging
import sys
import time as t
import random

logging.basicConfig()
with open('ip.txt', 'r') as file:
    ip_a = file.read().strip()
br = Bridge(ip_a)
with open('ID.txt', 'r') as idfile:
  data = idfile.read()
data = data.strip('[] \n')
lights = [int(x) for x in data.split(',')]
def randomnum():
    num = random.randrange(256)
    return num

def generate():
    r = randomnum()
    g = randomnum()
    b = randomnum()
    print(f"r: {r}, g: {g}, b: {b}")
    return [r,g,b]

def rgb_to_xy(R, G, B):
    # Normalize RGB values to the range 0-1
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

    return [x, y]

while True:
    for light in lights:
        rgb = generate()
        br.set_light(light, 'xy', rgb_to_xy(*rgb))
        t.sleep(.1)
