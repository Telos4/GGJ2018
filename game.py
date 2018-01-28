from object import *
import pygame, sys
from pygame.locals import *
import letters
import time


class Game:
    def __init__(self, renderer):
        # List of all displayed objects
        self.objects = []
        self.players = []

        self.renderer = renderer
        self.text_renderer = letters.TEXT(renderer,[200,50])
        self.credits_renderer = letters.TEXT(renderer,[120,50])
        self.imag_renderer = letters.TEXT(renderer,[1000,150])

        self.score = [0,0]

    def render(self):
        self.renderer.clearscreen()

        for object in self.objects:
            object.draw()
        self.renderer.update()


leftUps = [K_w, K_d]
leftDowns = [K_s, K_f]
rightUps = [K_UP, K_k]
rightDowns = [K_DOWN, K_j]

# player class for handling player input
class PLAYER:
    def __init__(self,left, renderer):
        self.renderer = renderer
        playerLeftPos = [0,(self.renderer.windowheight-self.renderer.barsize)//2]
        playerRightPos = [self.renderer.windowwidth-1,(self.renderer.windowheight-self.renderer.barsize)//2]
        self.movedir = 0
        self.controls = []
        self.vel = 100
        if left:
            self.pos = playerLeftPos
            self.controls = [leftUps,leftDowns]
        else:
            self.pos = playerRightPos
            self.controls = [rightUps,rightDowns]
        self.player_object = LineObject(self.pos, self.renderer)

    def changeVel(self,dir,key):
        if key in self.controls[0]: #accelerate up
            self.movedir -= 1*dir
        if key in self.controls[1]: #accelerate down
            self.movedir += 1*dir
    def move(self):
        self.pos[1] += self.movedir*self.vel
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] >= self.renderer.windowheight-self.renderer.barsize:
            self.pos[1] = self.renderer.windowheight-self.renderer.barsize-1


class Pong(Game):
    def __init__(self, renderer, obstaclebool):
        Game.__init__(self,renderer)
        self.obstaclebool = obstaclebool
        self.players.append(PLAYER(True, renderer))
        self.players.append(PLAYER(False, renderer))

        for player in self.players:
            self.objects.append(player.player_object)

        self.ball = BALL(renderer=renderer)
        self.objects.append(self.ball)
        self.obstacleList = []

    def terminate(self):
        pygame.quit()
        sys.exit()

    def doGameStep(self):
        for p in self.players:
            p.move()
        for o in self.obstacleList:
            o.move()
        self.ball.move(self.obstacleList)

        for player in range(2):
            behind = False
            if player == 0:
                if self.ball.pos[0] < 0:
                    behind = True
            if player == 1:
                if self.ball.pos[0] > self.renderer.windowwidth:
                    behind = True
            if behind:
                y0 = self.ball.pos[1]-(self.ball.pos[0]-player*self.renderer.windowwidth)*self.ball.movedir[1]/self.ball.movedir[0]
                ypl = self.players[player].pos[1]
                if  ypl < y0 < ypl+self.renderer.barsize:
                    soundcoll = pygame.mixer.Sound("collision.wav")
                    pygame.mixer.Channel(2).play(soundcoll)
                    self.ball.movedir = self.dirAfterCollisionPlayer(player,y0)
                    self.ball.pos = np.array([player*self.renderer.windowwidth,y0])
                    self.ball.vel = min(self.ball.vel * self.ball.speedup, self.ball.velMax)
                else:
                    self.afterScore(player)

    def dirAfterCollisionPlayer(self,player,y0):
        #y0 = self.ball.pos[1]-(self.ball.pos[0]-player*self.renderer.windowwidth)*self.ball.movedir[1]/self.ball.movedir[0]
        middle = self.players[player].pos[1]+self.renderer.barsize/2
        nDFM  = (y0-middle)/self.renderer.barsize #normed distance from middle
        reflected_direction = np.array([(1-2*player)*np.cos(0.9*np.pi*nDFM),np.sin(0.9*np.pi*nDFM)])
        return reflected_direction

    def afterScore(self,winner):
        global obstaclebool
        self.score[winner] += 1
        ww = self.renderer.windowwidth
        start = np.array([np.random.randint(ww/3,ww*2./3.),np.random.randint(ww/3,2*ww/3.)])
        dir = np.array([random(),random()])
        length = ww/3
        end = start + length*dir/np.linalg.norm(dir)
        if self.obstaclebool == True:
            self.obstacleList.append(OBSTACLE(self.renderer,start,end))
        self.ball.reset([-1+2*winner, random()])
        self.drawscore()
        self.renderer.update()
        time.sleep(3)


    def update(self):
        self.doGameStep()
        self.render()
        for obst in self.obstacleList:
            obst.draw()

        for i in self.score:
            if i == 2:
                self.renderer.clearscreen()
                pygame.mixer.Channel(1).fadeout(500)
                gameoversound = pygame.mixer.Sound("gameover.wav")
                pygame.mixer.Channel(3).play(gameoversound, loops = -1)
                self.text_renderer.WORD("GAMEOVER", 3)
                self.ball.vel = 0
                self.renderer.update()
                time.sleep(10)
                pygame.mixer.Channel(3).fadeout(2000)
                time.sleep(2)

                #imaginaerraum screen
                self.renderer.clearscreen()
                self.imag_renderer.WORD("ir",1)
                self.renderer.update()
                time.sleep(5)


                #credit screen
                self.renderer.clearscreen()
                self.credits_renderer.WORD("NICO STUHLMUELLER",2)
                self.credits_renderer.WORD("SIMON PIRKELMANN",3)
                self.credits_renderer.WORD("CLEMENS BUCHACHER",4)
                self.credits_renderer.WORD("DANIEL HEINLEIN",5)
                self.credits_renderer.WORD("SOFIE KRIETENSTEIN",6)
                self.credits_renderer.WORD("STEPHAN MESSLINGER",7)
                self.renderer.update()
                time.sleep(5)


                return False

        self.renderer.update()
        return True

    def drawscore(self):
        strscore = str(self.score[1])+":"+str(self.score[0])
        drscore = self.text_renderer.WORD(strscore,1)


