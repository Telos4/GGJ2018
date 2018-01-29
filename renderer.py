import pygame
import numpy as np
from pygame.locals import *

class Renderer():
    def __init__(self, serial=None, oszi=False, windowwidth=4000, windowheight=4000, scalingfactor=10):
        self.windowwidth = windowwidth
        self.windowheight = windowheight
        self.scalingfactor = scalingfactor
        #self.barsize = windowheight//5
        self.barsize = int(windowheight//3)
        self.oszi = oszi
        self.serial = serial
        
        self.bgcolor = (0,0,0)
        self.linecolor = (0,255,0)

        self.lastpos = (0,0)
        
        pygame.init()
        self.displaysurf = pygame.display.set_mode((self.windowwidth // self.scalingfactor, self.windowheight // self.scalingfactor))

    def _lineto(self, end_pos, draw=True):
        ex = int(abs(end_pos[0]))
        ey = int(abs(end_pos[1]))
        if ex < 0 or ex >=2**12:
            print("WW: ex is wrong in ", end_pos)
            ex=0
        if ey < 0 or ey >=2**12:
            print("WW: ey is wrong in ", end_pos)
            ey=0
        if self.oszi:
            t=(ex<<16)+ey
            if draw:
                t+=1<<12
            self.serial.write(t.to_bytes(4,'little'))

    def lineto(self, end_pos, draw=True):
        self._lineto(end_pos, draw)
        if draw:
            pygame.draw.line(self.displaysurf,self.linecolor,np.array(self.lastpos)/self.scalingfactor,np.array(end_pos)/self.scalingfactor)
        self.lastpos=end_pos

    def line(self, start_pos,end_pos):
        # if self.lastpos[0] == start_pos[0] and self.lastpos[1] == start_pos[1]:
        #     self.lineto(end_pos)
        #     self.lastpos=end_pos
        # elif self.lastpos[0] == end_pos[0] and self.lastpos[1] == end_pos[1]:
        #     self.lineto(start_pos)
        #     self.lastpos=start_pos
        # else:
        #   self.lineto(start_pos, False)
        #   self.lineto(end_pos)
        #   self.lastpos = end_pos
        self.lineto(start_pos, False)
        self.lineto(end_pos)
        self.lastpos = end_pos
        pygame.draw.line(self.displaysurf,self.linecolor,np.array(start_pos)/self.scalingfactor,np.array(end_pos)/self.scalingfactor)

    def rectangle(self, upLeft,downRight):
        self.line(upLeft,[upLeft[0],downRight[1]])
        self.line([upLeft[0],downRight[1]],downRight)
        self.line(downRight,[downRight[0],upLeft[1]])
        self.line([downRight[0],upLeft[1]],upLeft)

    def update(self):
        if self.oszi:
            self.serial.write((1<<31).to_bytes(4,'little'))
        pygame.display.update()

    def clearscreen(self):
        self.lastpos=(0,0)
        if self.oszi:
            self.serial.write((1<<29).to_bytes(4,'little'))
        self.displaysurf.fill(self.bgcolor)


if __name__ == "__main__":
    import serial
    ser = serial.Serial('/dev/cu.usbmodem3297371', 115200, timeout=10)
    renderer = Renderer(serial=ser, oszi=True)
    renderer.clearscreen()

    ##renderer.line((0,0),(4095,4095))


    for i in range(0,4095,100):
        renderer.line((4094/2,4094/2),(3500,i))


