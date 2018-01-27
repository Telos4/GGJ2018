from object import *
import pygame, sys
from pygame.locals import *
import letters


class Game:
    def __init__(self, renderer):
        # List of all displayed objects
        self.objects = []
        self.players = []

        self.renderer = renderer
        self.text_renderer = letters.TEXT(renderer)

        self.score = [0,0]

    def render(self):
        self.renderer.clearscreen()

        for object in self.objects:
            object.draw()

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j


# player class for handling player input
class PLAYER:
    def __init__(self,left, renderer):
        self.renderer = renderer
        playerLeftPos = [0,(self.renderer.windowheight-self.renderer.barsize)//2]
        playerRightPos = [self.renderer.windowwidth-1,(self.renderer.windowheight-self.renderer.barsize)//2]
        self.movedir = 0
        self.controls = []
        self.vel = 20
        if left:
            self.pos = playerLeftPos
            self.controls = [leftUp,leftDown]
        else:
            self.pos = playerRightPos
            self.controls = [rightUp,rightDown]
        self.player_object = LineObject(self.pos, self.renderer)

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


class Pong(Game):
    def __init__(self, renderer):
        Game.__init__(self,renderer)
        self.players.append(PLAYER(True, renderer))
        self.players.append(PLAYER(False, renderer))

        for player in self.players:
            self.objects.append(player.player_object)

        self.ball = BALL(renderer=renderer)
        self.objects.append(self.ball)


    def terminate(self):
        pygame.quit()
        sys.exit()

    def doGameStep(self):
        for p in self.players:
            p.move()
        self.ball.move()

        if self.ball.pos[0] < 0:
            if self.ball.pos[1] in range(self.players[0].pos[1], self.players[0].pos[1] + self.renderer.barsize):
                self.ball.pos[0] = -self.ball.pos[0]
                self.ball.movedir[0] = -self.ball.movedir[0]
                self.ball.velMax *= 1.1
            else:
                self.score[0] += 1
                self.ball.reset([-1, random()])
        if self.ball.pos[0] > self.renderer.windowwidth:
            if self.ball.pos[1] in range(self.players[1].pos[1], self.players[1].pos[1] + self.renderer.barsize):
                self.ball.pos[0] = 2 * self.renderer.windowwidth - self.ball.pos[0]
                self.ball.movedir[0] = -self.ball.movedir[0]
                self.ball.velMax *= 1.1
            else:
                self.score[1] += 1
                self.ball.reset([1, random()])

    def update(self):
        self.doGameStep()
        self.render()
        self.drawscore()

        for i in self.score:
            if i == 0:
                self.text_renderer.WORD("GAMEOVEROVEROVE", 3)
                self.ball.velMax = 500

        pygame.display.update()

    def drawscore(self):
        strscore = str(self.score[1])+":"+str(self.score[0])
        drscore = self.text_renderer.WORD(strscore,1)


