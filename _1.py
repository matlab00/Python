import math
class Punkt():
    

    def __init__(self, p1 = 0, p2 = 0):

        self.p1 = p1
        self.p2 = p2

    def odleglosc(self):
        
        print(math.sqrt(pow(0-self.p1,2)+pow(0-self.p2,2)))

    @staticmethod
    def dystans(x, y):
             
        print(math.sqrt(pow(x.p1-y.p1,2)+pow(x.p2-y.p2,2)))

    def __str__(self):

        return f"p1: {self.p1} p2: {self.p2}"

    def __repr__(self):

        return f"p1: {self.p1} p2: {self.p2}"


class Kolo(Punkt):

    def __init__(self,r = 1,p1 = 0,p2 = 0):

        super().__init__(p1,p2)
        self.r = r

    def obwod(self):
        print(float(2*3.14*self.r))

    def pole(self):
        print(float(3.14*pow(self.r,2)))


pkt = Punkt(1,2)
pkt2 = Punkt(3,4)

kolo1 = Kolo(3,3,4)
kolo1.obwod()
kolo1.pole()
