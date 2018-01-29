# Oszipong for the GGJ2018
Our project for the Global Game Jam 2018 was to implement the classic pong game to play on an oscilloscope. The oscilloscope (analog, x-y-mode) is connected to a microcontroller (Teensy 3.2) and DAC (digital analog converter, MCP 4922) to display lines mimicking classical vector displays. 

Two players may play this game competitively, trying to force the ball in the enemy's zone, while obstacles, i.e., lines, appear randomly on the screen in mid-game such that the ball ricochets on them. Then, the ball adds a momentum to the obstacle in order to move it. Additionally, we can draw arbitrary text on the oscilloscope and use this for various notifications like the score. 


# Requirements:
## Hardware:
- oscilloscope (analog, x-y-mode)
- Teensy 3.2
- MCP 4922

## Software:
- Arduino IDE with teensy plugin
- Python 3 with pygame, numpy and pyserial modules


# Instructions:
- To start the game use: python3 pong.py


# References:
We got our inspiration from the following article in the 'Make':
https://www.heise.de/select/make/2017/5/1509043825945640
