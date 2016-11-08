#!/usr/bin/python2.7
import math
def quadratic_equation(a,b,c):
    if math.sqrt(b *b -4*a*c) >= 0:
        return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
    else:
        return "none"
print quadratic_equation(2,3,1)
print quadratic_equation(1,3,-4)
