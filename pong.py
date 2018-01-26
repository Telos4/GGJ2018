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
WINDOWHEIGHT = 400
WINDOWWIDTH = 400
pos = [WINDOWWIDTH//2,WINDOWHEIGHT//2]
length = 400

def terminate():
    subprocess.call("killall -s 9 python2",shell=True)
    pygame.quit()
    sys.exit()

def drawPlayer():
    clearscreen()
    line(pos[0],pos[1],pos[0]+length,pos[1]+length)


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                terminate()
            print("keydown")
            pos[0] += 5;
            pos[1] += 5;
    drawPlayer()


ser.close()
