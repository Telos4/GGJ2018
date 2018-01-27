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


class BALL(Object):
    movedir = [0,0]

    def __init__(self,  renderer, pos=[0,0], size=[5,5]):
        Object.__init__(self,pos=pos, renderer=renderer)
        self.pos = np.array([self.renderer.windowwidth/2,self.renderer.windowheight/2])
        self.size = size
        self.movedir = np.array([random(),random()])
        self.velBallDefault = 10
        self.velMax = self.velBallDefault

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

class LineObject(Object):
    def __init__(self, pos, renderer):
        Object.__init__(self, pos=pos, renderer=renderer)

    def draw(self):
        self.renderer.line(self.pos,[self.pos[0],self.pos[1]+self.renderer.barsize])