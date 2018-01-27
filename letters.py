import pygame

WINDOWWIDTH = 4000
WINDOWHEIGHT = 4000

LE = 20
OI = 5
OX = OI
OY = OI

def A():
    line([OX,OY],[OX,OY+2*LE])
    line([OX,OY+LE],[OX+LE,OY+LE])
    line([OX,OY],[OX+LE,OY])
    line([OX+LE,OY],[OX+LE,OY+2*LE])

def B():
    line([OX,OY],[OX,OY+2*LE])
    line([OX,OY+LE],[OX+LE,OY+LE])
    line([OX,OY],[OX+LE,OY])
    line([OX+LE,OY],[OX+LE,OY+2*LE])
    line([OX,OY+2*LE],[OX+LE,OY+2*LE])

def C():
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])

def D():
    line([OX,OY],[OX,OY+2*LE])
    line([OX,OY],[OX+LE//2,OY])
    line([OX+LE//2,OY],[OX+LE,OY+LE])
    line([OX+LE,OY+LE],[OX+LE//2,OY+2*LE])
    line([OX,OY+2*LE],[OX+LE//2,OY+2*LE])

def E():
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])
    line([OX,OY+LE], [OX+LE,OY+LE])
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])

def F():
    line([OX,OY+LE], [OX+LE,OY+LE])
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])

def G():
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])
    line([OX+LE//2,OY+LE], [OX+LE,OY+LE])
    line([OX+LE,OY+2*LE],[OX+LE, OY+LE])

def H():
    line([OX,OY],[OX,OY+2*LE])
    line([OX,OY+LE],[OX+LE,OY+LE])
    line([OX+LE,OY],[OX+LE,OY+2*LE])

def I():
    line([OX,OY], [OX,OY+2*LE])

def J():
    line([OX+LE,OY], [OX+LE,OY+2*LE])
    line([OX,OY], [OX+LE,OY])
    line([OX+LE//2,OY+2*LE], [OX+LE,OY+2*LE])

def K():
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+LE], [OX+LE,OY])
    line([OX,OY+LE], [OX+LE,OY+2*LE])

def L():
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])

def M():
    line([OX+LE,OY], [OX+LE,OY+2*LE])
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY], [OX+LE//2,OY+2*LE])
    line([OX+LE//2,OY+2*LE], [OX+LE,OY])

def N():
    line([OX,OY], [OX,OY+2*LE])
    line([OX+LE,OY], [OX+LE,OY+2*LE])
    line([OX,OY], [OX+LE,OY+2*LE])

def O():
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])
    line([OX+LE,OY], [OX+LE,OY+2*LE])

def P():
    line([OX,OY],[OX+LE,OY])
    line([OX,OY],[OX,OY+2*LE])
    line([OX+LE,OY],[OX+LE,OY+LE])
    line([OX,OY+LE],[OX+LE,OY+LE])

def Q():
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])
    line([OX+LE,OY], [OX+LE,OY+2*LE])
    line([OX+3//4*LE, OY+3//4*LE], [OX+5//4*LE, OY+5//4*LE])

def R():
    line([OX,OY], [OX+LE,OY])
    line([OX,OY], [OX,OY+2*LE])
    line([OX+LE//2,OY+LE], [OX+LE,OY+2*LE])
    line([OX,OY+LE], [OX+LE,OY+LE])
    line([OX+LE,OY], [OX+LE, OY+LE])

def S():
    line([OX,OY],[OX+LE,OY])
    line([OX,OY],[OX,OY+LE])
    line([OX,OY+LE],[OX+LE,OY+LE])
    line([OX+LE,OY+LE],[OX+LE,OY+2*LE])
    line([OX,OY+2*LE],[OX+LE,OY+2*LE])

def T():
    line([OX,OY],[OX+LE,OY])
    line([OX+LE//2,OY],[OX+LE//2,OY+2*LE])

def U():
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE,OY+2*LE])
    line([OX+LE,OY+2*LE], [OX+LE,OY+2*LE])

def V():
    line([OX,OY], [OX+LE//2, OY + 2*LE])
    line([OX+LE//2,OY+2*LE], [OX+LE, OY])

def W():
    line([OX+LE,OY], [OX+LE,OY+2*LE])
    line([OX,OY], [OX,OY+2*LE])
    line([OX,OY+2*LE], [OX+LE//2,OY])
    line([OX+LE//2,OY], [OX+LE,OY+2*LE])

def X():
    line([OX,OY], [OX+LE, OY+2*LE])
    line([OX, OY+2*LE],[OX+LE,OY])

def Y():
    line([OX,OY],[OX+LE//2, OY+LE])
    line([OX+LE//2, OY+LE], [OX + LE, OY])
    line([OX + LE//2, OY+ LE], [OX + LE//2, OY+ 2*LE])

def Z():
    line([OX,OY],[OX+LE,OY])
    line([OX, OY+2*LE],[OX+LE,OY+2*LE])
    line([OX+LE,OY],[OX,OY+2*LE])


def WORD(letters, zeile):
    global LE
    global OI
    global OX
    global OY
    OY = 3*int(int(LE)*int(int(zeile) - 1) + 2*OI)
    for i in range(len(letters)):
        letters[i]()
        OX = OX + LE + OI
    OX = OI

    


DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))

while True:
    # for event in pygame.event.get():
    #     if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
    #         terminate()
    WORD([S,P,L,A,S,H,S,C,R,E,E,N], 1)
    #WORD([A,B,C,D,E,F,G,H,I,J,K,L], 2)
    #WORD([M,N,O,P,Q,R,S,T,U,V,W,X], 3)
    #WORD([Y,Z], 4)
    WORD([G,L,O,B,A,L,G,A,M,E,J,A,M],2)
    pygame.display.update()