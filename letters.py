import renderer

class TEXT():
    #LE = 20
    #OI = 5
    #OX = OI
    #OY = OI
    def __init__(self,renderer):
        self.renderer = renderer
        self.LE = 200
        self.OI = 5
        self.OX = self.OI
        self.OY = self.OI

    def A(self):
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+2*self.LE])

    def B(self):
        self.renderer.line([OX,OY],[OX,OY+2*LE])
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])
        self.renderer.line([OX,OY],[OX+LE,OY])
        self.renderer.line([OX+LE,OY],[OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+2*LE],[OX+LE,OY+2*LE])

    def C(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])

    def D(self):
        self.renderer.line([OX,OY],[OX,OY+2*LE])
        self.renderer.line([OX,OY],[OX+LE//2,OY])
        self.renderer.line([OX+LE//2,OY],[OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY+LE],[OX+LE//2,OY+2*LE])
        self.renderer.line([OX,OY+2*LE],[OX+LE//2,OY+2*LE])

    def E(self):
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])

    def F(self):
        self.renderer.line([OX,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])

    def G(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX+LE//2,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY+2*LE],[OX+LE, OY+LE])

    def H(self):
        self.renderer.line([OX,OY],[OX,OY+2*LE])
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY],[OX+LE,OY+2*LE])

    def I(self):
        self.renderer.line([OX,OY], [OX,OY+2*LE])

    def J(self):
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX+LE//2,OY+2*LE], [OX+LE,OY+2*LE])

    def K(self):
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+LE], [OX+LE,OY])
        self.renderer.line([OX,OY+LE], [OX+LE,OY+2*LE])

    def L(self):
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])

    def M(self):
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY], [OX+LE//2,OY+2*LE])
        self.renderer.line([OX+LE//2,OY+2*LE], [OX+LE,OY])

    def N(self):
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY], [OX+LE,OY+2*LE])

    def O(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])

    def P(self):
        self.renderer.line([OX,OY],[OX+LE,OY])
        self.renderer.line([OX,OY],[OX,OY+2*LE])
        self.renderer.line([OX+LE,OY],[OX+LE,OY+LE])
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])

    def Q(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])
        self.renderer.line([OX+3//4*LE, OY+3//4*LE], [OX+5//4*LE, OY+5//4*LE])

    def R(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX+LE//2,OY+LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY], [OX+LE, OY+LE])

    def S(self):
        self.renderer.line([OX,OY],[OX+LE,OY])
        self.renderer.line([OX,OY],[OX,OY+LE])
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY+LE],[OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+2*LE],[OX+LE,OY+2*LE])

    def T(self):
        self.renderer.line([OX,OY],[OX+LE,OY])
        self.renderer.line([OX+LE//2,OY],[OX+LE//2,OY+2*LE])

    def U(self):
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX+LE,OY+2*LE], [OX+LE,OY+2*LE])

    def V(self):
        self.renderer.line([OX,OY], [OX+LE//2, OY + 2*LE])
        self.renderer.line([OX+LE//2,OY+2*LE], [OX+LE, OY])

    def W(self):
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE//2,OY])
        self.renderer.line([OX+LE//2,OY], [OX+LE,OY+2*LE])

    def X(self):
        self.renderer.line([OX,OY], [OX+LE, OY+2*LE])
        self.renderer.line([OX, OY+2*LE],[OX+LE,OY])

    def Y(self):
        self.renderer.line([OX,OY],[OX+LE//2, OY+LE])
        self.renderer.line([OX+LE//2, OY+LE], [OX + LE, OY])
        self.renderer.line([OX + LE//2, OY+ LE], [OX + LE//2, OY+ 2*LE])

    def Z(self):
        self.renderer.line([OX,OY],[OX+LE,OY])
        self.renderer.line([OX, OY+2*LE],[OX+LE,OY+2*LE])
        self.renderer.line([OX+LE,OY],[OX,OY+2*LE])


    def zero(self):
        O()

    def one(self):
        self.renderer.line([OX+LE, OY], [OX+LE,OY+2*LE])

    def two(self):
        self.renderer.line([OX,OY],[OX+LE,OY])
        self.renderer.line([OX+LE,OY],[OX+LE,OY+LE])
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])
        self.renderer.line([OX,OY+LE],[OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE],[OX+LE,OY+2*LE])

    def three(self):
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX+LE,OY], [OX+LE,OY+2*LE])

    def four(self):
        self.renderer.line([OX,OY],[OX,OY+LE])
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY],[OX+LE,OY+2*LE])

    def five(self):
        S()

    def six(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+2*LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY+2*LE],[OX+LE, OY+LE])

    def seven(self):
        one()
        self.renderer.line([OX,OY],[OX,OY+LE])

    def eight(self):
        zero()
        self.renderer.line([OX,OY+LE],[OX+LE,OY+LE])

    def nine(self):
        self.renderer.line([OX,OY], [OX+LE,OY])
        self.renderer.line([OX,OY], [OX,OY+LE])
        self.renderer.line([OX,OY+2*LE], [OX+LE,OY+2*LE])
        self.renderer.line([OX,OY+LE], [OX+LE,OY+LE])
        self.renderer.line([OX+LE,OY+2*LE],[OX+LE, OY])

    def doubledot(self):
        self.renderer.rectangle([OX+LE//2,OY+LE//4],[OX+LE//2+OI,OY+LE//4+OI])
        self.renderer.rectangle([OX+LE//2,OY+LE*3//4],[OX+LE//2+OI,OY+LE*3//4+OI])

    def WORD(self,letters, zeile):
        #LE
        #OI
        #OX
        #OY
        LE = self.LE
        OX = self.OX
        OI = self.OI
        OY = 3*int(int(LE)*int(int(zeile) - 1) + 2*OI)
        #for i in range(len(letters)):
            #letters[i]()
        for l in letters:
            if l == 'A':
                self.A()

            OX = OX + LE + OI
        OX = OI

#DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT))
#
#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
#            terminate()
#    WORD([S,P,L,A,S,H,S,C,R,E,E,N], 1)
#    #WORD([A,B,C,D,E,F,G,H,I,J,K,L], 2)
#    #WORD([M,N,O,P,Q,R,S,T,U,V,W,X], 3)
#    #WORD([Y,Z], 4)
#    WORD([G,L,O,B,A,L,G,A,M,E,J,A,M],2)
#    pygame.display.update()