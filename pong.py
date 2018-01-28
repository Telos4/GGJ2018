from game import Pong

import renderer
import pygame
from pygame.locals import *
import time
import math

playerList = []

leftUp = K_d
leftDown = K_f
rightUp = K_k
rightDown = K_j

if __name__ == "__main__":

    obstaclebool = True
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
    ponggame = Pong(renderer,obstaclebool)
    pass

    splashscreen = False
    gamerunning = True
    modscreen = True
    backsoundbool = True

    while gamerunning:
        t_end = time.time() + 1
        if splashscreen == True:
            renderer.clearscreen()
            sound = pygame.mixer.Sound("GGJ18.wav")
            pygame.mixer.Channel(3).play(sound, loops = -1)
            while time.time()<t_end:
                value = []
                for t in range(0,200):
                    renderer.clearscreen()
                    ponggame.text_renderer.WORD("GLOBALGAMEJAM",2)
                    ponggame.text_renderer.WORD("2018",3)
                    discretization = 50
                    for n in range(0,discretization):
                        value.append([n*renderer.windowwidth/discretization,int(math.sin(n*0.75+0.5*t)*500*math.sin(0.1*n-0.1*t))+3000])
                    renderer.lineto(value[0], False)
                    for n in range(1,discretization):
                        renderer.lineto(value[n],True)
                    #renderer.lineto([0, 0], False)
                    value = []
                    renderer.update()
                    time.sleep(2.0/60.0)
               
            #time.sleep(5)


            #Hilfsscreen
            renderer.clearscreen()
            ponggame.text_renderer.WORD("PLAYER 1",1)
            ponggame.text_renderer.WORD("UP W  DOWN S",2)
            ponggame.text_renderer.WORD("PLAYER 2",4)
            ponggame.text_renderer.WORD("UP  DOWN",5)
            renderer.update()
            time.sleep(5)

            #Modscreen
            pygame.event.clear()
            renderer.clearscreen()
            ponggame.text_renderer.WORD("MODES", 1)
            ponggame.text_renderer.WORD("NORMAL 1", 3)
            ponggame.text_renderer.WORD("OBSTACLES 2", 4)
            renderer.update()

            while modscreen == True:

                #ponggame.text_renderer.WORD("OBSTACLES SQUARES   3",4)
                #event = pygame.event.wait()
                for event in pygame.event.get():
                    if event.type == KEYUP and event.key == K_1:
                        obstaclebool = False
                        modscreen = False

                    elif event.type == KEYUP and event.key == K_2:
                        obstaclebool = True
                        modscreen = False


            ponggame = Pong(renderer,obstaclebool)
            pass

            pygame.mixer.Channel(3).fadeout(3000)

            renderer.clearscreen()
            ponggame.text_renderer.WORD("3",3)
            renderer.update()
            time.sleep(1)
            renderer.clearscreen()
            ponggame.text_renderer.WORD("2",3)
            renderer.update()
            time.sleep(1)
            renderer.clearscreen()
            ponggame.text_renderer.WORD("1",3)
            renderer.update()
            time.sleep(1)
            splashscreen = False

            if backsoundbool:
                backsoundbool = False
                background_sound = pygame.mixer.Sound("background.wav")
                pygame.mixer.Channel(1).play(background_sound, loops = -1)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                ponggame.terminate()
            if event.type == KEYDOWN:
                for p in ponggame.players:
                    if event.key in p.controls[0] or event.key in p.controls[1]:
                        p.changeVel(1, event.key)
            if event.type == KEYUP:
                for p in ponggame.players:
                    if event.key in p.controls[0] or event.key in p.controls[1]:
                        p.changeVel(-1, event.key)

        gamerunning = ponggame.update()

        time.sleep(1/60)
