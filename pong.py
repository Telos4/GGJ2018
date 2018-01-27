from game import Pong

import renderer
import pygame
from pygame.locals import *
import time
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

    splashscreen = True
    gamerunning = True
    while gamerunning:

        if splashscreen == True:
            renderer.clearscreen()
            sound = pygame.mixer.Sound("GGJ18.wav")
            sound.play()
            ponggame.text_renderer.WORD("GLOBALGAMEJAM",2)
            ponggame.text_renderer.WORD("2018",3)
            pygame.display.update()
            time.sleep(0.15)
            renderer.clearscreen()
            ponggame.text_renderer.WORD("3",3)
            pygame.display.update()
            time.sleep(1)
            renderer.clearscreen()
            ponggame.text_renderer.WORD("2",3)
            pygame.display.update()
            time.sleep(1)
            renderer.clearscreen()
            ponggame.text_renderer.WORD("1",3)
            pygame.display.update()
            time.sleep(1)
            splashscreen = False

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

        gamerunning = ponggame.update()

        time.sleep(1/60)
