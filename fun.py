L = []
L = list(map(lambda x: x * x  ,range(1,101)))
print sum(L)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-1)
print my_abs(2)
print my_abs(0)

def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])


import math
def move(x,y,step,angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x , y = move(100,100,60,math.pi/6)
print x , y
r = move(100,100,60,math.pi/6)
print r

import math
def quadratic_equation(a,b,c):
    if math.sqrt(b *b -4*a*c) >= 0:
        return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
    else:
        return "none"
print quadratic_equation(2,3,1)
print quadratic_equation(1,3,-4)


