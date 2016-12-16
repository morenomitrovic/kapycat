from comparandum import Comparandum
from alpha import Alpha

#===================================== C L A S S 2/2 ==================================================================
class Analogy(Comparandum):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        if len(x) == len(y) == len(z):
            if len(x) == len(y) == len(z) == 1:
                self.f1()
            elif len(x) == len(y) == len(z) == 2:
                self.f2()
            elif len(x) == len(y) == len(z) == 3:
                self.f3()
            else:
                print("Error, too weird for me.")
        else:
            print("Error, too weird for me.")

    def f1(self):
        if self.x.i1 <= self.y.i1 <= self.z.i1:
            i = self.y.i1 - self.x.i1 + self.z.i1
        elif self.y.i1 > self.z.i1 > self.x.i1:
            i = Alpha.len() - self.z.i1
        else:
            i = self.y.i1 + (self.x.i1 - self.z.i1)
        print("Meow: ", Alpha.get(i))
        print("This cat ♥ pretending to be smart.")

    def f2(self):
        r1 = abs(self.x.i2 - self.x.i1)
        r2 = abs(self.y.i2 - self.y.i1)
        r3 = abs(self.z.i2 - self.z.i1)
        d1 = abs(self.y.i2 - self.x.i1)
        d0 = abs(self.y.i1 - self.x.i2)
        d1_vert1 = abs(self.y.i1 - self.x.i1)
        d1_vert2 = abs(self.x.i2 - self.y.i2)
        iu1 = self.z.i2 + d0
        iu2 = iu1 + r2
        r4 = abs(iu2 - iu1)
        d2 = abs(iu1 - self.z.i2)
        if self.z.i2 >= self.z.i1 >= self.y.i2 >= self.y.i1 >= self.x.i2 >= self.x.i1:
            if (r1 + d1 + r2 + d0 + r3 + d2 + r4) <= Alpha.len():
                if d1_vert1 == d1_vert2:
                    print("Meow = ", Alpha.get(iu1) + Alpha.get(iu2))
                else:
                    iu2 += r1
                    print("Meow = ", Alpha.get(iu1) + Alpha.get(iu2))
            else:
                print("Meow = ", Alpha.get(iu1 - Alpha.len()) + Alpha.get((iu2 - Alpha.len())))
            print("This cat ♥ pretending to be smart.")

        elif self.x.i2 > self.y.i2 > self.z.i2 and self.x.i1 < self.y.i1 < self.z.i1:
            r1 = abs(self.y.i1 - self.x.i1)
            iu1 = self.z.i1 + r1
            iu2 = self.z.i2 - r1
            if d1_vert1 == d1_vert2:
                print("Meow = ", Alpha.get(iu1) + Alpha.get(iu2))
            else:
                iu2 -= d12_vert
                print("Meow = ", Alpha.get(iu1) + Alpha.get(iu2))
            print("This cat ♥ pretending to be smart.")
        else:
            # applying to symmetric relations where the answer lies in the interval determined by, say, the first comparandum
            print(
                "I think this requires stochastic reasoning. Are you sure you know what a correct answer would look like?")
    def f3(self):
        r1i = abs(self.x.i2 - self.x.i1)
        r1ii = abs(self.x.i3 - self.x.i2)
        r2i = abs(self.y.i2 - self.y.i1)
        r2ii = abs(self.y.i3 - self.y.i2)
        # defining distances between pair-comparanda
        d1 = abs(self.y.i1 - self.x.i3)
        d0 = abs(self.z.i1 - self.y.i3)
        # defining the index-location ingredients for i comparandum and corresponding char u, s.t. alpha[u]=i
        iu1 = self.z.i3 + d1
        iu2 = iu1 + r1i
        iu3 = iu2 + r1ii
        if r1i == r2i and r1ii == r2ii:
            print("Meow = ", Alpha.get(iu1) + Alpha.get(iu2) + Alpha.get(iu3))
        else:
            print("I'm confused but I know I'm in the primary else clause. So there.")
#======================================================================================================================
