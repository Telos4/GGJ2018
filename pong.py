import pygame, sys
from pygame.locals import *
OSZI = False # outbut is Oszi or Pygame
if OSZI:
    import serial


pygame.init()

BGCOLOR = (100,50,50)
LINECOLOR = (000,255,000)
WINDOWHEIGHT = 400
WINDOWWIDTH = 400
pos = [WINDOWWIDTH//2,WINDOWHEIGHT//2]
length = 100


if OSZI:
    ser=serial.Serial('/dev/ttyACM0', 115200, timeout=10)


def line(start_pos,end_pos):
    if OSZI:
        ser.write(((start_pos[0]<<48)+(start_pos[1]<<32)+(end_pos[0]<<16)+(end_pos[1])).to_bytes(8,'big'))
    pygame.draw.line(DISPLAYSURF,LINECOLOR,start_pos,end_pos)

def clearscreen():
    line([65535,0],[0,0])



def terminate():
    pygame.quit()
    sys.exit()

def drawPlayer():
    clearscreen()
    line(pos,[pos[0]+length,pos[1]+length])


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            terminate()
        if event.type == KEYDOWN:
            print("keydown")
            pos[0] += 5;
            pos[1] += 5;
    drawPlayer()
    pygame.display.update()


if OSZI:
    ser.close()
