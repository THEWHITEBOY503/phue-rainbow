# phue-rainbow
Introduce a cascade of colors to your room via [phue](https://github.com/studioimaginaire/phue?tab=readme-ov-file#installation) and Phillips Hue!

## Installation
Clone the repository:
```bash
git clone https://github.com/THEWHITEBOY503/phue-rainbow.git
cd phue-rainbow
```
Install dependencies:
`pip install phue logging`
OR
`pip install requirements.txt`


Refer to the example script in the phue repository for more info.

## Setup
- You will need to know the IP address of your Hue bridge. You can find it by going to your Hue app, and going to **Settings -> My hue system -> Click the (i) button next to your bridge -> IP Address**
- Now, edit `ip.txt` with the appropriate IP.
- Then, pair your hub with `python connect.py`.
- You should be prompted to push the button on your Hue hub. 
- Success, now you're paired to your hub! (If it didn't work, double check your IP, and make sure your python environment is on the same network as the bridge.)
- Run `python getlight.py` to return a list of your lights. Make note of the ID's of the light you want to control.
- Edit ID.txt to have the IDs of the light. For example, for lights 1, 2, and 3, I'd write `[1,2,3]`.
- Execute your desired file with `python file.py`!

## ...desired file? Which do I choose?
You see, there's a couple different effects I've laid out. 

- `colors.py` - Cycles through the rainbow in order. Ya know, ROYGBIV! Or something similar to it. 
- `rainbow.py` - Generates a random color based on RGB value and sends it to the group of lights.
- `rainbowXY.py` - Generates a random color based on XY colorspace value and sends it to the group of lights.
- `flash.py` - Generates a new random color for each light in the group of lights using the RGB algorithm.
- `flashXY.py` - Generates a new random color for each light in the group of lights using the XY algorithm. 

## Why have two algorithms?
Because of whatever this is.
![XY color space](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/CIE1931xy_CIERGB.svg/1280px-CIE1931xy_CIERGB.svg.png)
This is XY color space, and for reasons unknown to me, phue expects XY inputs. So, one algorithm generates a random decimal between 0 and 1 for both the X and Y axis. (This could probably use some fine tuning, I have no idea how color spaces work.)

On the other hand, RGB color is a bit more manageable, and with it we get 16,777,216 colors! So, those scripts generate a number between 0 and 255 three times, one for red, green, and blue. Then, a function converts it to the XY color space with some math, and sends it to the light.

## Sponsor
This is free, open source software I wrote in my spare time when I was bored and sick one day, and I'm very happy to offer a free solution to a problem Phillips introduced after the fact. If you find this program useful enough to you that you feel like donating, you should consider sponsoring me on GitHub by clicking that neat little button on the sidebar! Alternatively, I ask that you consider sponsoring one of the developers of phue instead! While I can't find a way to donate directly to the phue team, there are several developers on the team who probably have sponsorships open. 
