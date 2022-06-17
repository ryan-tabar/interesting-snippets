# complex number class
import math 

class Complex:
    # inputs either in cartesian or polar form
    def __init__(self, in1, in2, polar=False):
        if not polar:
            self.re = in1
            self.im = in2
            self.__polar() 
        else:
            self.mag = in1
            self.arg = in2
            self.__cartesian() 

    def __add__(self, other): return Complex(self.re + other.re, self.im + other.im)
    def __sub__(self, other): return Complex(self.re - other.re, self.im - other.im)
    def __mul__(self, other): return Complex(self.mag * other.mag, self.arg + other.arg, polar=True)
    def __truediv__(self, other): return Complex(self.mag / other.mag, self.arg - other.arg, polar=True)
    def __repr__(self): return f"Complex({self.re}, {self.im})"
    def __str__(self): return f"{self.re:.2f} + {self.im:.2f}i"

    # private methods
    def __cartesian(self):
        self.re = self.mag * math.cos(self.arg)
        self.im = self.mag * math.sin(self.arg)

    def __polar(self):
        self.mag = math.sqrt(self.re ** 2 + self.im ** 2)
        self.arg = math.pi if self.re == 0 else math.atan(self.im / self.re)

c1 = Complex(2, 3)
c2 = Complex(-1, 5)
i = Complex(0, 1)
c3 = c1 + i
print(c3)