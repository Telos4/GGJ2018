################
# encoding UTF-8
################

import renderer
import time

delay = 1

class TEXT():
    """
    Buchstaben und Zahlen zeichnen
    """

    global delay

    def __init__(self,renderer,param):
        self.renderer = renderer
        self.LE = param[0] #200
        self.OI = param[1] #50
        self.OX = self.OI
        self.OY = self.OI


    def A(self):
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+2*self.LE])

    def B(self):
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE],[self.OX+self.LE,self.OY+2*self.LE])

    def C(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])

    def D(self):
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE//2,self.OY])
        self.renderer.line([self.OX+self.LE//2,self.OY],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY+self.LE],[self.OX+self.LE//2,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE],[self.OX+self.LE//2,self.OY+2*self.LE])

    def E(self):
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])

    def F(self):
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])

    def G(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE//2,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY+2*self.LE],[self.OX+self.LE, self.OY+self.LE])

    def H(self):
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+2*self.LE])

    def I(self):
        self.renderer.line([self.OX+self.LE/2,self.OY], [self.OX+self.LE/2,self.OY+2*self.LE])

    def J(self):
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE//2,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])

    def K(self):
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+2*self.LE])

    def L(self):
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])

    def M(self):
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE//2,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE//2,self.OY+2*self.LE], [self.OX+self.LE,self.OY])

    def N(self):
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY+2*self.LE])

    def O(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])

    def P(self):
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])

    def Q(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX+3//4*self.LE, self.OY+3//4*self.LE], [self.OX+5//4*self.LE, self.OY+5//4*self.LE])

    def R(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE//2,self.OY+self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE, self.OY+self.LE])

    def S(self):
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY+self.LE],[self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE],[self.OX+self.LE,self.OY+2*self.LE])

    def T(self):
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE//2,self.OY],[self.OX+self.LE//2,self.OY+2*self.LE])

    def U(self):
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])

    def V(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE//2, self.OY + 2*self.LE])
        self.renderer.line([self.OX+self.LE//2,self.OY+2*self.LE], [self.OX+self.LE, self.OY])

    def W(self):
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE//2,self.OY])
        self.renderer.line([self.OX+self.LE//2,self.OY], [self.OX+self.LE,self.OY+2*self.LE])

    def X(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE, self.OY+2*self.LE])
        self.renderer.line([self.OX, self.OY+2*self.LE],[self.OX+self.LE,self.OY])

    def Y(self):
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE//2, self.OY+self.LE])
        self.renderer.line([self.OX+self.LE//2, self.OY+self.LE], [self.OX + self.LE, self.OY])
        self.renderer.line([self.OX+self.LE//2, self.OY+self.LE], [self.OX + self.LE//2, self.OY+ 2*self.LE])

    def Z(self):
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX, self.OY+2*self.LE],[self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX,self.OY+2*self.LE])


    def zero(self):
        self.O()

    def one(self):
        self.renderer.line([self.OX+self.LE, self.OY], [self.OX+self.LE,self.OY+2*self.LE])

    def two(self):
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE],[self.OX+self.LE,self.OY+2*self.LE])

    def three(self):
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE,self.OY+2*self.LE])

    def four(self):
        self.renderer.line([self.OX,self.OY],[self.OX,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY],[self.OX+self.LE,self.OY+2*self.LE])

    def five(self):
        self.S()

    def six(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY+2*self.LE],[self.OX+self.LE, self.OY+self.LE])

    def seven(self):
        self.one()
        self.renderer.line([self.OX,self.OY],[self.OX+self.LE,self.OY])

    def eight(self):
        self.zero()
        self.renderer.line([self.OX,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE])

    def nine(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+self.LE])
        self.renderer.line([self.OX,self.OY+2*self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY+2*self.LE],[self.OX+self.LE, self.OY])

    def doubledot(self):
        self.renderer.rectangle([self.OX+self.LE//2,self.OY+self.LE*2/3],[self.OX+self.LE//2+self.OI,self.OY+self.LE*2/3+self.OI])
        self.renderer.rectangle([self.OX+self.LE//2,self.OY+self.LE*4//3],[self.OX+self.LE//2+self.OI,self.OY+self.LE*4//3+self.OI])

    def space(self):
        self.OX = self.OX + self.LE/2

    def arrowup(self):
        self.renderer.line([self.OX+self.LE/2,self.OY],[self.OX+self.LE/2, self.OY+self.LE*2])
        self.renderer.line([self.OX,self.OY+self.LE/3],[self.OX+self.LE/3, self.OY])
        self.renderer.line([self.OX+self.LE/2, self.OY],[self.OX+self.LE,self.OY+self.LE/3])

    def arrowdown(self):
        self.renderer.line([self.OX+self.LE/2,self.OY],[self.OX+self.LE/2, self.OY+self.LE*2])
        self.renderer.line([self.OX,self.OY+self.LE*2/3],[self.OX+self.LE/3, self.OY+self.LE*2])
        self.renderer.line([self.OX+self.LE/2, self.OY+self.LE*2],[self.OX+self.LE,self.OY+self.LE*2/3])
    
    def imaginaerraumi(self):
        self.renderer.line([self.OX+self.LE,self.OY+self.LE],[self.OX+self.LE,self.OY+self.LE*2])
        self.renderer.line([self.OX+self.LE*4/5,self.OY+self.LE*2],[self.OX+self.LE,self.OY+self.LE*2])
        self.renderer.rectangle([self.OX+self.LE-self.OI/2,self.OY+self.LE*2/3],[self.OI/2+self.OX+self.LE,self.OY+self.LE*2/3+self.OI])
    
    def imaginaerraumr(self):
        self.renderer.line([self.OX,self.OY], [self.OX+self.LE,self.OY])
        self.renderer.line([self.OX,self.OY], [self.OX,self.OY+2*self.LE])
        self.renderer.line([self.OX+self.LE//2,self.OY+self.LE], [self.OX+self.LE,self.OY+2*self.LE])
        self.renderer.line([self.OX,self.OY+self.LE], [self.OX+self.LE,self.OY+self.LE])
        self.renderer.line([self.OX+self.LE,self.OY], [self.OX+self.LE, self.OY+self.LE])
        self.renderer.line([self.OX+self.LE/6,self.OY], [self.OX+self.LE/6,self.OY+self.LE*2])
        

    def WORD(self,letters, zeile):
        LE = self.LE
        self.OX = self.renderer.windowwidth/2 - self.LE*(len(letters)+1)/2 - self.OI*(len(letters)-1)/2
        OI = self.OI
        self.OY = 3*int(int(LE)*int(int(zeile) - 1) + 2*OI)
        for l in letters:
            if l == 'A':
                self.A()
            elif l == 'B':
                self.B()
            elif l == 'C':
                self.C()
            elif l == 'D':
                self.D()
            elif l == 'E':
                self.E()
            elif l == 'F':
                self.F()
            elif l == 'G':
                self.G()
            elif l == 'H':
                self.H()
            elif l == 'I':
                self.I()
            elif l == 'J':
                self.J()
            elif l == 'K':
                self.K()
            elif l == 'L':
                self.L()
            elif l == 'M':
                self.M()
            elif l == 'N':
                self.N()
            elif l == 'O':
                self.O()
            elif l == 'P':
                self.P()
            elif l == 'Q':
                self.Q()
            elif l == 'R':
                self.R()
            elif l == 'S':
                self.S()
            elif l == 'T':
                self.T()
            elif l == 'U':
                self.U()
            elif l == 'V':
                self.V()
            elif l == 'W':
                self.W()
            elif l == 'X':
                self.X()
            elif l == 'Y':
                self.Y()
            elif l == 'Z':
                self.Z()
            elif l == '1':
                self.one()
            elif l == '2':
                self.two()
            elif l == '3':
                self.three()
            elif l == '4':
                self.four()
            elif l == '5':
                self.five()
            elif l == '6':
                self.six()
            elif l == '7':
                self.seven()
            elif l == '8':
                self.eight()
            elif l == '9':
                self.nine()
            elif l == '0':
                self.zero()
            elif l == ':':
                self.doubledot()
            elif l == ' ':
                self.space()
            elif l =='+':
                self.arrowup()
            elif l == '-':
                self.arrowdown()
            elif l == 'i':
                self.imaginaerraumi()
            elif l == 'r':
                self.imaginaerraumr()
            self.OX = self.OX + self.LE + self.OI
        self.OX = self.OI