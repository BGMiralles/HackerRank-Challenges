# Input Format:
#     One line of input: The real and imaginary part of a number separated by a space.
#
# Output Format:
#     For two complex numbers `C` and `D`, the output should be in the following sequence on separate lines:
#     C + D
#     C - D
#     C * D
#     C / D
#     mod(C)
#     mod(D)

class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, no):
        x = complex(self.real, self.imag)+complex(no.real, no.imag)
        return Complex(x.real, x.imag).__str__()
    def __sub__(self, no):
        x = complex(self.real, self.imag)-complex(no.real, no.imag)
        return Complex(x.real, x.imag).__str__()
    def __mul__(self, no):
        x = complex(self.real, self.imag)*complex(no.real, no.imag)
        return Complex(x.real, x.imag).__str__()
    def __div__(self, no):
        x = complex(self.real, self.imag)/complex(no.real, no.imag)
        return Complex(x.real, x.imag).__str__()
    def mod(self):
        return Complex(abs(complex(self.real, self.imag)), 0)
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result
