import pygame, sys
from pygame.locals import *
import time
import numpy as np

from game import Pong

import renderer
import letters


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
    #playerList.append(PLAYER(True, renderer))
    #playerList.append(PLAYER(False, renderer))
    #ball = BALL(renderer)
    #score = [0, 0]

    ponggame = Pong(renderer)
    #

    while True:
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


        ponggame.update()
        #text_renderer.WORD('AAAAA', 1)


        time.sleep(1/60)
