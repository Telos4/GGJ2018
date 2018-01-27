import pygame
import numpy as np
from pygame.locals import *

class Renderer():
    def __init__(self, serial=None, oszi=False, windowwidth=4000, windowheight=4000, scalingfactor=10):
        self.windowwidth = windowwidth
        self.windowheight = windowheight
        self.scalingfactor = scalingfactor
        #self.barsize = windowheight//5
        self.barsize = windowheight//2
        self.oszi = oszi
        self.serial = serial
        
        self.bgcolor = (0,0,0)
        self.linecolor = (0,255,0)
        
        pygame.init()
        self.displaysurf = pygame.display.set_mode((self.windowwidth // self.scalingfactor, self.windowheight // self.scalingfactor))

    def line(self, start_pos,end_pos):
        sx = int(abs(start_pos[0]))
        sy = int(abs(start_pos[1]))
        ex = int(abs(end_pos[0]))
        ey = int(abs(end_pos[1]))
        if self.oszi:
            self.serial.write(((sx<<48)+(sy<<32)+(ex<<16)+(ey)).to_bytes(8,'big'))
        pygame.draw.line(self.displaysurf,self.linecolor,np.array(start_pos)/self.scalingfactor,np.array(end_pos)/self.scalingfactor)

    def rectangle(self, upLeft,downRight):
        self.line(upLeft,[upLeft[0],downRight[1]])
        self.line([upLeft[0],downRight[1]],downRight)
        self.line(downRight,[downRight[0],upLeft[1]])
        self.line([downRight[0],upLeft[1]],upLeft)

    def clearscreen(self):
        if self.oszi:
            self.line([65535,0],[0,0])
        self.displaysurf.fill(self.bgcolor)
