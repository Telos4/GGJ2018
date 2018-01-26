import pygame, sys
from pygame.locals import *
import time
OSZI = False # output is Oszi or Pygame
if OSZI:
    import serial



BGCOLOR = (100,50,50)
LINECOLOR = (000,255,000)
WINDOWHEIGHT = 400
WINDOWWIDTH = 400
BARSIZE = WINDOWHEIGHT//5
pos = [WINDOWWIDTH//2,WINDOWHEIGHT//2]
length = 100

playerList = []
playerLeftPos = [0,(WINDOWHEIGHT-BARSIZE)//2]
playerRightPos = [WINDOWWIDTH-1,(WINDOWHEIGHT-BARSIZE)//2]

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j

if OSZI:
    ser=serial.Serial('/dev/ttyACM0', 115200, timeout=10)


class player:
    pos = []
    movedir = 0
    controls = []
    def __init__(self,left):
        movedir = 0
        if left:
            self.pos = playerLeftPos
            self.controls = [leftUp,leftDown]
        else:
            self.pos = playerRightPos
            self.controls = [rightUp,rightDown]
    def changeVel(self,dir,key):
        if key == self.controls[0]: #accelerate up
            self.movedir -= 1*dir
        if key == self.controls[1]: #accelerate down
            self.movedir += 1*dir
    def move(self):
        self.pos[1] += self.movedir*2
    def draw(self):
        line(self.pos,[self.pos[0],self.pos[1]+BARSIZE])


# init Game
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))
playerList.append(player(True))
playerList.append(player(False))

def line(start_pos,end_pos):
    if OSZI:
        ser.write(((start_pos[0]<<48)+(start_pos[1]<<32)+(end_pos[0]<<16)+(end_pos[1])).to_bytes(8,'big'))
    pygame.draw.line(DISPLAYSURF,LINECOLOR,start_pos,end_pos)

def clearscreen():
    if OSZI:
        line([65535,0],[0,0])
    DISPLAYSURF.fill(BGCOLOR)

def terminate():
    pygame.quit()
    sys.exit()

def drawGame():
    clearscreen()
    for player in playerList:
        player.draw()

def doGameStep():
    for p in playerList:
        p.move()



while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            terminate()
        if event.type == KEYDOWN:
            for p in playerList:
                if event.key in p.controls:
                    p.changeVel(1, event.key)
        if event.type == KEYUP:
            for p in playerList:
                if event.key in p.controls:
                    p.changeVel(-1, event.key)

    doGameStep()
    drawGame()
    pygame.display.update()
    time.sleep(1/60)


if OSZI:
    ser.close()
