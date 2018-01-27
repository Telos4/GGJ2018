import pygame, sys
from pygame.locals import *
import time
import numpy as np

import renderer
import letters

playerList = []

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j


def random():
    return 2*(np.random.random()-0.5)

class PLAYER:
    pos = []
    movedir = 0
    controls = []
    vel = 20
    def __init__(self,left, renderer):
        self.renderer = renderer
        playerLeftPos = [0,(self.renderer.windowheight-self.renderer.barsize)//2]
        playerRightPos = [self.renderer.windowwidth-1,(self.renderer.windowheight-self.renderer.barsize)//2]
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
        if self.pos[1] >= self.renderer.windowheight-self.renderer.barsize:
            self.pos[1] = self.renderer.windowheight-self.renderer.barsize-1
    def draw(self):
        self.renderer.line(self.pos,[self.pos[0],self.pos[1]+self.renderer.barsize])

class BALL():
    pos = []
    size = [5,5]
    movedir = [0,0]
    velBallDefault = 10
    velMax = velBallDefault
    def __init__(self, renderer):
        self.renderer = renderer
        self.pos = np.array([self.renderer.windowwidth/2,self.renderer.windowheight/2])
        self.movedir = np.array([random(),random()])
    def move(self):
        self.pos += self.movedir/np.linalg.norm(self.movedir)*self.velMax
        if self.pos[1] < 0:
            self.pos[1] = -self.pos[1]
            self.movedir[1] = -self.movedir[1]
        if self.pos[1] > self.renderer.windowheight:
            self.pos[1] = 2 * self.renderer.windowheight - self.pos[1]
            self.movedir[1] = -self.movedir[1]
        for i in range(2):
            self.pos[i] = int(self.pos[i]+0.5)
    def draw(self):
        self.renderer.rectangle(self.pos,np.array(self.pos) + np.array(self.size))
    def reset(self,dir):
        self.pos = [self.renderer.windowheight/2,self.renderer.windowheight/2]
        self.movedir = dir
        self.velMax = self.velBallDefault




def terminate():
    pygame.quit()
    sys.exit()

def drawGame(renderer):
    renderer.clearscreen()
    for player in playerList:
        player.draw()
    ball.draw()

def doGameStep(renderer):
    global ball
    global score
    for p in playerList:
        p.move() 
    ball.move()
    if ball.pos[0] < 0:
        if ball.pos[1] in range(playerList[0].pos[1],playerList[0].pos[1]+renderer.barsize):
            ball.pos[0] = -ball.pos[0]
            ball.movedir[0] = -ball.movedir[0]
            ball.velMax *= 1.1
        else:
            score[0] += 1
            ball.reset([-1,random()])
    if ball.pos[0] > renderer.windowwidth:
        if ball.pos[1] in range(playerList[1].pos[1],playerList[1].pos[1]+renderer.barsize):
            ball.pos[0] = 2*renderer.windowwidth-ball.pos[0]
            ball.movedir[0] = -ball.movedir[0]
            ball.velMax *= 1.1
        else:
            score[1] += 1
            ball.reset([1,random()])



if __name__ == "__main__":

    oszi = False
    ser = None
    try:
        oszi_params = open('oszi_params.txt', 'r')
        print(oszi_params)

        import serial

        for line in oszi_params:
            if line[0] != "#":
                try:
                    serial_port = line.rstrip()
                    ser = serial.Serial(serial_port, 115200, timeout=10)
                    oszi = True
                    break
                except:
                    print("trying next configuration")
    except:
        print("Oscilloscope not connected!")
    renderer = renderer.Renderer(serial=ser, oszi=oszi)
    # init Game
    playerList.append(PLAYER(True, renderer))
    playerList.append(PLAYER(False, renderer))
    ball = BALL(renderer)
    score = [0, 0]

    text_renderer = letters.TEXT(renderer)
    pass

def drawscore():
    strscore = str(score[1])+":"+str(score[0])
    drscore = text_renderer.WORD(strscore,1)


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
    doGameStep(renderer)
    drawGame(renderer)
    drawscore()
    for i in score:
        if i == 9:
            text_renderer.WORD("GAMEOVER",3)
            ball.velMax = 0
    
    #text_renderer.WORD("GLOBALGAMEJAM",3)
    pygame.display.update()
    time.sleep(1/60)
