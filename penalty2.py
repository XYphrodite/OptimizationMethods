import math
from math import *
import numpy as np
import matplotlib.pyplot as plt
import random


def ln(b, a):
    if b < 0:
        return 0
    elif b < a:
        return a**2
    return log(b, a) ** 2


def foo(x1, x2):
    a = -3
    b = -1
    c = 1
    d = 3
    alf = 130
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
        (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def f1(x):
    x1 = x[0]
    x2 = x[1]
    return (pow(x1, 2) + 2 * x2)


def f2(x):
    return (x[1] - x[0])


def isIn(x):
    if (f1(x) < 0.1):
        return True
    else:
        return False


def interior_penalty(e):
    def powell(xi):
        dlt = e / 10
        x1 = xi[0]
        x2 = xi[1]

        y1 = R(x1, x2)

        while (True):
            hF = False
            vF = False
            dF = False

            rt = 0
            lt = 0
            tp = 0
            bt = 0

            # horizontal
            x1 += dlt
            y2 = R(x1, x2)
            x1 -= dlt
            if (y2 <= y1):
                hF = True
                x1 += dlt
                while (y2 <= y1):
                    # print("1 x1: ", x1, "x2: ", x2)
                    y1 = y2
                    rt += 1
                    x1 += dlt
                    y2 = R(x1, x2)
                x1 -= dlt
            else:
                x1 -= dlt
                y2 = R(x1, x2)
                while (y2 <= y1):
                    # print("2 x1: ", x1, "x2: ", x2)
                    hF = True
                    y1 = y2
                    lt += 1
                    x1 -= dlt
                    y2 = R(x1, x2)
                x1 += dlt

            # vertical
            x2 += dlt
            y2 = R(x1, x2)
            x2 -= dlt
            if (y2 <= y1):
                vF = True
                x2 += dlt
                while (y2 <= y1):
                    # print("3 x1: ", x1, "x2: ", x2)
                    y1 = y2
                    tp += 1
                    x2 += dlt
                    y2 = R(x1, x2)
                x2 -= dlt
            else:
                x2 -= dlt
                y2 = R(x1, x2)
                while (y2 <= y1):
                    # print("4 x1: ", x1, "x2: ", x2)
                    vF = True
                    y1 = y2
                    bt += 1
                    x2 -= dlt
                    y2 = R(x1, x2)
                x2 += dlt

            # diagnal
            if (rt > 0):
                if (tp > 0):
                    x1 += dlt * rt
                    x2 += dlt * tp
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("5 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 += dlt * rt
                        x2 += dlt * tp
                        y2 = R(x1, x2)
                    x1 -= dlt * rt
                    x2 -= dlt * tp
                else:
                    x1 += dlt * rt
                    x2 -= dlt * bt
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("6 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 += dlt * rt
                        x2 -= dlt * bt
                        y2 = R(x1, x2)
                    x1 -= dlt * rt
                    x2 += dlt * bt
            elif (lt > 0):
                if (tp > 0):
                    x1 -= dlt * lt
                    x2 += dlt * tp
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("7 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 -= dlt * lt
                        x2 += dlt * tp
                        y2 = R(x1, x2)
                    x1 += dlt * lt
                    x2 -= dlt * tp
                else:
                    x1 -= dlt * lt
                    x2 -= dlt * bt
                    y2 = R(x1, x2)
                    while (y2 <= y1):
                        # print("8 x1: ", x1, "x2: ", x2)
                        dF = True
                        y1 = y2
                        x1 -= dlt * lt
                        x2 -= dlt * bt
                        y2 = R(x1, x2)
                    x1 += dlt * lt
                    x2 += dlt * bt

            if ((hF == False) and (vF == False) and (dF == False)): break

        xx = [x1, x2, 0]
        xx[2] = foo(xx[0], xx[1])

        return xx

    # штраф
    def R(x1, x2):
        return foo(x1, x2) + k * ln(f1([x1, x2]), math.e) +k*f2([x1, x2])**2

    def gradR(x1, x2):
        h = 0.001
        return [(R(x1 + h, x2) - R(x1 - h, x2)) / (h * 2), (R(x1, x2 + h) - R(x1, x2 - h)) / (h * 2)]

    def gradient(x):
        xx = [x[0], x[1], x[2]]
        h = 1
        gradvectR = gradR(xx[0], xx[1])
        while pow(gradvectR[0] + gradvectR[1], 2) > e:
            xx[0] = xx[0] - h * gradvectR[0]
            xx[1] = xx[1] - h * gradvectR[1]
            gradvectR = gradR(xx[0], xx[1])
        xx[2] = foo(xx[0], xx[1])
        return xx

    x_list = []
    k = 1
    c = 10
    randy = 10
    rand = random.randint(-randy, randy)
    x = [rand, rand, 0]

    while not isIn(x):
        rand = random.randint(-randy, randy)
        x = [rand, rand + e / 2, 0]
    x[2] = foo(x[0], x[1])
    print("Начальные значения x: [", x[0], ",", x[1], "]")
    xn = powell(x)

    while abs(x[2] - xn[2]) > e:
        x = [xn[0], xn[1], xn[2], k]
        k *= c
        x_list.append(x)
        xn = powell(x)

    return x, x_list


e = 0.001
dlt = e * 10
_x, _x_list = interior_penalty(e)

# while (isIn(_x) != True):
#   _x, _x_list = interior_penalty(e)
if (isIn(_x)):
    print("В границах")
for i in range(len(_x_list)):
    print(i + 1, ". x1 = ", _x_list[i][0], " x2 = ", _x_list[i][1], " f(x1,x2) = ", _x_list[i][2], " r = ",
          _x_list[i][3])

print("X* = [", _x[0], ", ", _x[1], " ]")
levels = [0.0, 0.05, 0.10, 0.3,
          0.5, 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50]
xg1 = np.arange(-7, 5.5, 0.0250)
xg2 = np.arange(-6, 6, 0.0250)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(foo)
yg = f2(xg1, xg2)

x1i = np.linspace(-5, 5, 100)
x2i = np.linspace(-5, 5, 100)

xe1 = np.linspace(-3.3, 3.3, 100)
xe2 = []
for i in xe1:
    xe2.append(-pow(i, 2) / 2)

cont = plt.contour(xg1, xg2, yg, levels=levels)
plt.plot(x1i, x2i, color="blue")
plt.plot(xe1, xe2, color="red")
plt.plot(_x[0], _x[1], color="black", marker=".")
# for i in _x_list:
# plt.plot(i[0], i[1], color="yellow", marker=".")
plt.show()
