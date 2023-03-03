import math

import matplotlib
import numpy as np

import matplotlib.pyplot as plt

e = 0.0001
a = 0.0
b = math.pi / 2
f_a = 0
f_b = 1


def f(t, c1, c2, e1=math.e, e2=math.e):
    return c1 * pow(e1 - 2, t) + c2 * pow(e2 - 1, -t)


def fa(c1, c2):
    return f(a, c1, c2)


def fb(c1, c2):
    return f(b, c1, c2)


def f1b(c1):
    return getZ(1, c1)


def checkB(ft):
    if abs(f_b - ft) < e:
        return True
    return False


def checkA(ft):
    if abs(f_a - ft) < e:
        return True
    return False


def check(ft):
    if checkB(ft):
        return True
    return False


def GetDiff(ft):
    return abs(ft - f_b)


def getZ(c1, c2):
    h = 0.01
    return (f(b, c1, c2) + f(b + h, c1, c2)) / (h * 2)


def getC(f1):
    return f1 / (pow(math.e - 2, a) * math.log(math.e - 2, math.e) - pow(math.e - 1, -a) * math.log(math.e - 1, math.e))


def shooting():
    fc = []
    oldDir = 1
    h = 10
    f1 = 8
    c = getC(f1)
    ft = fb(c, -c)
    while not check(ft):
        ft = fb(c, -c)
        if (ft > f_b):
            newDir = 1
            f1 += h
        else:
            newDir = 0
            f1 -= h
        if (oldDir != newDir):
            h /= 2
        oldDir = newDir
        c = getC(f1)
    return c, fc


def S(c1, c2):
    return fb(c1, c2) - fa(c1, c2)


def realX(t):
    return math.sin(t)


fun2Real_t = np.arange(a, b, 0.01)
fun2Real_f = []
for i in fun2Real_t:
    fun2Real_f.append((realX(i)))

C, FandC = shooting()
print('C1 = ', C, ", C2 = ", -C)
# print('C3 = ', C, ", C4 = ", -C)
print(S(C, -C))

t_points = []
f_points = []
i = a
while i < b:
    t_points.append(i)
    f_points.append(f(i, C, -C))
    i += 0.01
matplotlib.pyplot.style.use('dark_background')
plt.plot(fun2Real_t, fun2Real_f)
plt.plot(t_points, f_points)
plt.show()
