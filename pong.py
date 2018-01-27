import pygame, sys
from pygame.locals import *
import time
import numpy as np

try:
    oszi_params = open('oszi_params.txt', 'r')
    print(oszi_params)

    import serial
    for line in oszi_params:
        if line[0] != "#":
            try:
                serial_port = line.rstrip()
                ser = serial.Serial(serial_port, 115200, timeout=10)
                break
            except:
                print("trying next configuration")
    OSZI = True
except:
    print("Oscilloscope not connected!")
    OSZI = False # output is Oszi or Pygame



BGCOLOR = (0,0,0)
LINECOLOR = (000,255,000)
WINDOWHEIGHT = 4000
WINDOWWIDTH = 4000
SCALING_FACTOR = 10 # how much larger is the osci-display compared to the pygame surface
BARSIZE = WINDOWHEIGHT//5
pos = [WINDOWWIDTH//2,WINDOWHEIGHT//2]
length = 100
velBallDefault = 10

playerList = []
playerLeftPos = [0,(WINDOWHEIGHT-BARSIZE)//2]
playerRightPos = [WINDOWWIDTH-1,(WINDOWHEIGHT-BARSIZE)//2]

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j


class PLAYER:
    pos = []
    movedir = 0
    controls = []
    vel = 20
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
        self.pos[1] += self.movedir*self.vel
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] >= WINDOWHEIGHT-BARSIZE:
            self.pos[1] = WINDOWHEIGHT-BARSIZE-1
    def draw(self):
        line(self.pos,[self.pos[0],self.pos[1]+BARSIZE])

class BALL():
    pos = []
    size = [5,5]
    movedir = [0,0]
    velMax = velBallDefault
    def __init__(self):
        self.pos = np.array([WINDOWWIDTH/2,WINDOWHEIGHT/2])
        self.movedir = np.array([4,3])
    def move(self):
        self.pos += self.movedir/np.linalg.norm(self.movedir)*self.velMax
        if self.pos[1] < 0:
            self.pos[1] = -self.pos[1]
            self.movedir[1] = -self.movedir[1]
        if self.pos[1] > WINDOWHEIGHT:
            self.pos[1] = 2 * WINDOWHEIGHT - self.pos[1]
            self.movedir[1] = -self.movedir[1]
        for i in range(2):
            self.pos[i] = int(self.pos[i]+0.5)
    def draw(self):
        rectangle(self.pos,np.array(self.pos) + np.array(self.size))
    def reset(self,dir):
        self.pos = [WINDOWWIDTH//2,WINDOWHEIGHT//2]
        self.movedir = dir
        self.velMax = velBallDefault



# init Game
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH//SCALING_FACTOR , WINDOWHEIGHT//SCALING_FACTOR))
playerList.append(PLAYER(True))
playerList.append(PLAYER(False))
ball = BALL()
score = [0,0]

def line(start_pos,end_pos):
    sx = int(start_pos[0])
    sy = int(start_pos[1])
    ex = int(end_pos[0])
    ey = int(end_pos[1])
    if OSZI:
        ser.write(((sx<<48)+(sy<<32)+(ex<<16)+(ey)).to_bytes(8,'big'))
    pygame.draw.line(DISPLAYSURF,LINECOLOR,np.array(start_pos)/SCALING_FACTOR,np.array(end_pos)/SCALING_FACTOR)

def rectangle(upLeft,downRight):
    line(upLeft,[upLeft[0],downRight[1]])
    line([upLeft[0],downRight[1]],downRight)
    line(downRight,[downRight[0],upLeft[1]])
    line([downRight[0],upLeft[1]],upLeft)

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
    ball.draw()

def doGameStep():
    global ball
    global score
    for p in playerList:
        p.move()
    ball.move()
    if ball.pos[0] < 0:
        if ball.pos[1] in range(playerList[0].pos[1],playerList[0].pos[1]+BARSIZE):
            ball.pos[0] = -ball.pos[0]
            ball.movedir[0] = -ball.movedir[0]
            ball.velMax *= 1.1
        else:
            score[0] += 1
            ball.reset([-1,2*(np.random.random()-0.5)])
    if ball.pos[0] > WINDOWWIDTH:
        if ball.pos[1] in range(playerList[1].pos[1],playerList[1].pos[1]+BARSIZE):
            ball.pos[0] = 2*WINDOWWIDTH-ball.pos[0]
            ball.movedir[0] = -ball.movedir[0]
            ball.velMax *= 1.1
        else:
            score[1] += 1
            ball.reset([1,int(np.random.random()-0.5)])




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
