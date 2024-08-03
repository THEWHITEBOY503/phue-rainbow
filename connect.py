#!/usr/bin/python

from phue import Bridge
with open('ip.txt', 'r') as file:
    ip_a = file.read().strip()
br = Bridge(ip_a)

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
br.connect()