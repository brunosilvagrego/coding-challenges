class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary

        temp = Complex(0,0)
        temp.real = a + c
        temp.imaginary = b + d
        return temp
        
    def __sub__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary

        temp = Complex(0,0)
        temp.real = a - c
        temp.imaginary = b - d
        return temp

    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary

        temp = Complex(0,0)
        temp.real = (a * c) - (b * d)
        temp.imaginary = (a * d) + (b * c)
        return temp

    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary

        temp = Complex(0,0)
        temp.real = ((a * c) + (b * d)) / ((c**2) + (d**2))
        temp.imaginary = ((b * c) - (a * d)) / ((c**2) + (d**2))
        return temp

    def mod(self):
        temp = Complex(0,0)
        temp.real = math.sqrt((self.real**2) + (self.imaginary**2))
        return temp

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

