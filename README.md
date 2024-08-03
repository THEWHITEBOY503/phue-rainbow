# phue-rainbow
Introduce a cascade of colors to your room via [phue](https://github.com/studioimaginaire/phue?tab=readme-ov-file#installation) and Phillips Hue!

## Installation
Clone the repository:
```bash
git clone https://github.com/THEWHITEBOY503/phue-rainbow.git
cd phue-rainbot
```
Install dependencies:
`pip install phue logging`


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

## Sponsor
This is free, open source software I wrote in my spare time when I was bored and sick one day, and I'm very happy to offer a free solution to a problem Phillips introduced after the fact. If you find this program useful to you that you feel like donating, you should consider sponsoring me on GitHub by clicking that neat little button on the sidebar! Alternatively, I ask that you consider sponsoring one of the developers of phue instead! While I can't find a way to donate directly to the phue team, there are several developers on the team who probably have sponsorships open. 
