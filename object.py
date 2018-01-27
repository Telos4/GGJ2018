import numpy as np

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
        self.vel = 0.0
        self.movedir = np.array([0.0, 0.0])

    def move(self):
        self.start = self.start + self.movedir
        self.end = self.end + self.movedir

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
        self.movedir = np.array([random(),random()])
        self.velBallDefault = 20
        self.vel = self.velBallDefault
    def move(self,obstacleList):
        posOld = self.pos
        posNew = posOld + self.movedir/np.linalg.norm(self.movedir)*self.vel
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
                if min(y0,y1) < y < max(y0,y1): # if collision occurs

                    # push obstacle out of the way
                    obst.vel += self.vel
                    obst.movedir = self.movedir

                    a = posNew-cross
                    b = np.array([x1-x0,y1-y0])
                    b = b/np.linalg.norm(b)
                    X = np.dot(a,b)*b
                    posMirror = 2*cross+2*X-posNew
                    posNew = posMirror
                    self.movedir = posMirror-cross
                    self.vel *= 1.1


        self.pos = posNew


        if self.pos[1] < 0:
            self.pos[1] = -self.pos[1]
            self.movedir[1] = -self.movedir[1]
        if self.pos[1] > self.renderer.windowheight:
            self.pos[1] = 2 * self.renderer.windowheight - self.pos[1]
            self.movedir[1] = -self.movedir[1]
        for i in range(2):
            self.pos[i] = int(self.pos[i]+0.5)



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
