import numpy as np
import pygame
from pygame.locals import *

class Object():
    def __init__(self, pos, renderer, name=''):
        self.pos = pos
        self.name = name
        self.renderer = renderer

    def draw(self):
        #self.renderer.render_object(self)
        pass

def random():
    return 2*(np.random.random()-0.5)

class OBSTACLE(Object):
    start = []
    end = []
    def __init__(self,renderer,start,end):
        Object.__init__(self,None,renderer)
        self.start = start
        self.end = end

        self.movedir = np.array([0.0, 0.0])
        self.velMax = 30
        self.vel = 0

    def move(self):
        self.start = self.start + self.movedir * self.vel
        self.end = self.end + self.movedir * self.vel

        if min(self.start[1], self.end[1]) < 0:
            self.movedir[1] = -self.movedir[1]
        if max(self.start[1],self.end[1]) > self.renderer.windowheight:
            self.movedir[1] = -self.movedir[1]
        if min(self.start[0],self.end[0]) < 0:
            self.movedir[0] = -self.movedir[0]
        if max(self.start[0],self.end[0]) > self.renderer.windowwidth:
            self.movedir[0] = -self.movedir[0]

    def draw(self):
        self.renderer.line(self.start,self.end)



class BALL(Object):
    movedir = [0,0]

    def __init__(self,  renderer, pos=[0,0], size=[5,5]):
        Object.__init__(self,pos=pos, renderer=renderer)

        self.pos = np.array([self.renderer.windowwidth/2,self.renderer.windowheight/2])
        self.size = size

        self.velBallDefault = 20


        # physical parameters of the ball
        self.vel = self.velBallDefault
        self.mass = 1.0
        self.movedir = np.array([random(), random()])

        if self.renderer.oszi == True:
            self.velMax = 100
        else:
            self.velMax = 50
        self.speedup = 1.25  # how much faster does the ball get on a collision

    def move(self,obstacleList):
        posOld = self.pos
        posNew = posOld + self.movedir/np.linalg.norm(self.movedir)*self.vel

        # collision with obstacles:
        u0 = posOld[0]
        v0 = posOld[1]
        u1 = posNew[0]
        v1 = posNew[1]
        mb = (v1-v0)/(u1-u0)

        # find closest colliding object
        min_distance = 1.0e+9
        min_collision_object = None
        for obst in obstacleList:
            x0 = obst.start[0]
            y0 = obst.start[1]
            x1 = obst.end[0]
            y1 = obst.end[1]
            mo = (y1 - y0) / (x1 - x0)
            x = (y0 - v0 + mb * u0 - mo * x0) / (mb - mo)
            y = y0 + mo * (x - x0)
            cross = np.array([x, y])
            current_distance = np.linalg.norm(cross - posOld)
            if min(u0,u1) < x < max(u0,u1):
                if min(y0,y1) < y < max(y0,y1): # if collision occurs remember the object
                    if current_distance < min_distance:
                        min_distance = current_distance
                        min_collision_object = obst

        # if a collision occurred handle it
        if not (min_collision_object == None):
            coll_obstacle = pygame.mixer.Sound("audio/collision_obstacle.wav")
            pygame.mixer.Channel(4).play(coll_obstacle)
            obst = min_collision_object
            x0 = obst.start[0]
            y0 = obst.start[1]
            x1 = obst.end[0]
            y1 = obst.end[1]
            mo = (y1 - y0) / (x1 - x0)
            x = (y0 - v0 + mb * u0 - mo * x0) / (mb - mo)
            y = y0 + mo * (x - x0)
            cross = np.array([x, y])

            # push obstacle out of the way
            obst.vel = min(obst.vel + 0.05 * self.vel, obst.velMax)
            obst.movedir += self.movedir
            obst.movedir/=np.linalg.norm(obst.movedir)

            #print("collission\n")

            a = posNew-cross
            b = np.array([x1-x0,y1-y0])
            b = b/np.linalg.norm(b)
            X = np.dot(a,b)*b
            posMirror = 2*cross+2*X-posNew
            posNew = posMirror
            self.movedir = posMirror-cross

            # collision with obstacle speedup and enforcing of maximum velocity
            self.vel = min(self.vel * self.speedup, self.velMax)


        self.pos = posNew


        if self.pos[1] < 0:
            if self.pos[0] < 0:
                self.edgecollision(0,0)
                self.pos[0] = -1
            elif self.pos[0] > self.renderer.windowwidth:
                self.edgecollision(self.renderer.windowwidth,0)
                self.pos[0] = self.renderer.windowwidth 
            else:
                self.pos[1] = -self.pos[1]
            self.movedir[1] = -self.movedir[1]
        if self.pos[1] > self.renderer.windowheight:
            if self.pos[0] < 0:
                self.edgecollision(0,self.renderer.windowheight)
                self.pos[0] = -1
            elif self.pos[0] > self.renderer.windowwidth:
                self.edgecollision(self.renderer.windowwidth,self.renderer.windowheight)
                self.pos[0] = self.renderer.windowwidth 
            else:
                self.pos[1] = 2 * self.renderer.windowheight - self.pos[1]
            self.movedir[1] = -self.movedir[1]
        # for i in range(2):
            # self.pos[i] = int(self.pos[i]+0.5)

    def edgecollision(self,x,y):
        print("doublecoll")
        v = self.vel / np.linalg.norm(self.movedir)
        vx = v * self.movedir[0]
        vy = v * self.movedir[1]
        vvec = np.array([vx,vy])
        r0 = self.pos-vvec
        ts = (y-r0[1])/vy
        xs = r0[0]+(y-r0[0])*vx/vy
        t = (x - xs)/(vx)
        yfinal = y - vy/vx *(x-xs)
        self.pos[1] = yfinal
        #self.movedir[1]=0
        print(yfinal)

    def draw(self):
        self.renderer.line(self.pos, np.array(self.pos) - self.vel * np.array(self.movedir)/(np.linalg.norm(self.movedir)))
        self.renderer.rectangle(self.pos,np.array(self.pos) + np.array(self.size))

    def reset(self,dir):
        self.pos = [self.renderer.windowheight/2,self.renderer.windowheight/2]
        self.movedir = dir
        self.vel = self.velBallDefault

class LineObject(Object):
    def __init__(self, pos, renderer):
        Object.__init__(self, pos=pos, renderer=renderer)

    def draw(self):
        self.renderer.line(self.pos,[self.pos[0],self.pos[1]+self.renderer.barsize])

class LineEffect(Object):
    def __init__(self, pos, pos2, renderer):
        Object.__init__(self, pos=pos, renderer=renderer)
        self.pos2 = pos2
        self.counter = 0
        self.counter_max = 5

    def draw(self):
        self.counter += 1
        self.renderer.line(self.pos,self.pos2)
