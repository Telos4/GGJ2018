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

    obstaclebool = False
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

    splashscreen = True
    gamerunning = True
    modscreen = True

    while gamerunning:
        t_end = time.time() + 1
        if splashscreen == True:
            renderer.clearscreen()
            sound = pygame.mixer.Sound("GGJ18.wav")
            sound.play()
            while time.time()<t_end:
                value = []
                for t in range(0,500):
                    renderer.clearscreen()
                    ponggame.text_renderer.WORD("GLOBALGAMEJAM",2)
                    ponggame.text_renderer.WORD("2018",3)
                    for n in range(0,40):
                        value.append([n*100,int(math.sin(n*0.5+0.01*t)*500)+3000])
                    for n in range(0,39):
                        renderer.line(value[n],value[n+1])
                    value = []
                    pygame.display.update()
               
            #time.sleep(5)


            #Hilfsscreen
            renderer.clearscreen()
            ponggame.text_renderer.WORD("PLAYER 1",1)
            ponggame.text_renderer.WORD("UP D  DOWN F",2)
            ponggame.text_renderer.WORD("PLAYER 2",4)
            ponggame.text_renderer.WORD("UP J  DOWN K",5)
            pygame.display.update()
            time.sleep(5)

            #Modscreen
            pygame.event.clear()
            
            while modscreen == True:
                renderer.clearscreen()
                ponggame.text_renderer.WORD("MODS",1)
                ponggame.text_renderer.WORD("NORMAL 1",3)
                ponggame.text_renderer.WORD("OBSTACLES 2",4)
                #ponggame.text_renderer.WORD("OBSTACLES SQUARES   3",4)
                pygame.display.update()
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
