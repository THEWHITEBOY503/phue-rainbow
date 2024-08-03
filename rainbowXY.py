#!/usr/bin/python
from phue import Bridge
import logging
import sys
import random
import time as t

logging.basicConfig()
with open('ip.txt', 'r') as file:
      ip_a = file.read().strip()
b = Bridge(ip_a)
with open('ID.txt', 'r') as idfile:
     data = idfile.read()
data = data.strip('[] \n')
lights = [int(x) for x in data.split(',')]
# Make sure the lights are turned on! 
for light in lights:
        b.set_light(light, 'on', True)

while True:
     one = random.random()
     two = random.random()
     for light in lights:
          b.set_light(light, 'xy', [one,two])
          t.sleep(0.1)
