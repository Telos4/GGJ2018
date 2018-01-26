import pygame, sys
from pygame.locals import *
import subprocess
import serial

ser=serial.Serial('/dev/cu.usbmodem3297371', 115200, timeout=10)


def line(a,b,c,d):
    ser.write(((a<<48)+(b<<32)+(c<<16)+(d)).to_bytes(8,'big'))

def clearscreen():
    line(65535,0,0,0)



OSZI = False # outbut is Oszi or Pygame
pygame.init()

BGCOLOR = (100,50,50)
pos = [200,200]

def drawPlayer():
    clearscreen()
    line(pos[0],pos[1],pos[0]+30,pos[1]+30)




while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pos[0] += 5;
            pos[1] += 5;
    drawPlayer()


ser.close()