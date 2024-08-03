from phue import Bridge
with open('ip.txt', 'r') as file:
    ip_a = file.read().strip()
br = Bridge(ip_a)
lights = br.get_light_objects('id')
for light in lights:
    print('name: ', lights[light].name, 'ID: ', light)