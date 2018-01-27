import pygame, sys
from pygame.locals import *
import time
import numpy as np

import renderer

playerList = []
obstacleList = []

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j


def random():
    return 2*(np.random.random()-0.5)

class OBSTACLE:
    start = []
    end = []
    def __init__(self,renderer,start,end):
        self.renderer = renderer
        self.start = start
        self.end = end
    def draw(self):
        self.renderer.line(self.start,self.end)


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
    velBallDefault = 20
    velMax = velBallDefault
    def __init__(self, renderer):
        self.renderer = renderer
        self.pos = np.array([self.renderer.windowwidth/2,self.renderer.windowheight/2])
        self.movedir = np.array([random(),random()])
        self.movedir = np.array([-1,-0.5])
    def move(self):
        posOld = self.pos
        posNew = posOld + self.movedir/np.linalg.norm(self.movedir)*self.velMax
        # collision with obstacles:
        u0 = posOld[0]
        v0 = posOld[1]
        u1 = posNew[0]
        v1 = posNew[1]
        mb = (v1-v0)/(u1-u0)
        for obst in obstacleList:
            x0 = obst.start[0]
            y0 = obst.start[1]
            x1 = obst.end[0]
            y1 = obst.end[1]
            mo = (y1-y0)/(x1-x0)
            x = (y0-v0+mb*u0-mo*x0)/(mb-mo)
            y = y0 + mo*(x-x0)
            cross = np.array([x,y])
            if min(u0,u1) < x < max(u0,u1):
                if min(y0,y1) < y < max(y0,y1):
                    a = posNew-cross
                    b = np.array([x1-x0,y1-y0])
                    b = b/np.linalg.norm(b)
                    X = np.dot(a,b)*b
                    posMirror = 2*cross+2*X-posNew
                    posNew = posMirror
                    self.movedir = posMirror-cross
                    self.velMax *= 1.1

        self.pos = posNew

        # collision with walls:
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
    for obst in obstacleList:
        obst.draw()

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
    obstacleList.append(OBSTACLE(renderer,np.array([400,300]),np.array([900,2000])))

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
        pygame.display.update()
        time.sleep(1/60)
