import pygame, sys
from pygame.locals import *
import serial

ser=serial.Serial('/dev/ttyACM0', 115200, timeout=10)


def line(a,b,c,d):
    ser.write(((a<<48)+(b<<32)+(c<<16)+(d)).to_bytes(8,'big'))
    return

def clearscreen():
    line(65535,0,0,0)



OSZI = False # outbut is Oszi or Pygame
pygame.init()

BGCOLOR = (100,50,50)
WINDOWHEIGHT = 4000
WINDOWWIDTH = 4000
pos = [WINDOWWIDTH//2,WINDOWHEIGHT//2]
length = 400

def drawPlayer():
    clearscreen()
    line(pos[0],pos[1],pos[0]+length,pos[1]+length)


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print("keydown")
            pos[0] += 5;
            pos[1] += 5;
    drawPlayer()


ser.close()
