import pygame, sys
from pygame.locals import *
import time
import numpy as np
from game import Pong

import renderer
import letters
import pygame, sys
from pygame.locals import *
import time
import numpy as np
playerList = []

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j

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
    ponggame = Pong(renderer)
    pass


gamerunning = True
while gamerunning:    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            ponggame.terminate()
        if event.type == KEYDOWN:
            for p in ponggame.players:
                if event.key in p.controls:
                    p.changeVel(1, event.key)
        if event.type == KEYUP:
            for p in ponggame.players:
                if event.key in p.controls:
                    p.changeVel(-1, event.key)
    for i in ponggame.score:
        if i == 2:
            ponggame.text_renderer.WORD("GAMEOVER",3)
            ponggame.ball.velMax = 0
            #gamerunning = False
            #time.sleep(10)  
    ponggame.update() 
      
    #text_renderer.WORD("GLOBALGAMEJAM",3)
    #pygame.display.update()
    time.sleep(1/60)
