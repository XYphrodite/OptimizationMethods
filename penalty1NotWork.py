import math
from math import *
import numpy as np
import matplotlib.pyplot as plt
import random


def f(x1, x2):
    a = 1
    b = 1
    c = 1
    d = 3
    alf = 120
    return (pow(((x1 - a) * cos(alf) + (x2 - b) * sin(alf)), 2)) / (c * c) + \
           (pow(((x2 - b) * cos(alf) - (x1 - a) * sin(alf)), 2)) / (d * d)


def con1(x1, x2):
    return - x1 * x2 + (1 / math.pow(math.e, x2))


def con2(x1,x2):
    return -x1 - x2


def in_constraints(X):
    if (con1(X[0], X[1]) >= 0) and (con2(X[0],X[1]) >= 0):
        return True
    else:
        return False


def grad(x1, x2):
    # gradient vector
    h = 0.0001
    return [(f(x1 + h, x2) - f(x1 - h, x2)) / (h * 2), (f(x1, x2 + h) - f(x1, x2 - h)) / (h * 2)]


def interior_penalty(e):

    def fi(x1, x2):
        return min(0, con1(x1, x2))+min(0, con2(x1))

    def R(x1, x2):
        return f(x1, x2) + 1 / k * (1 / con1(x1, x2) + 1 / con2(x1,x2))

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
        xx[2] = f(xx[0], xx[1])

        return xx

    x_list = []
    k = 1
    c = 10
    x = [random.randint(-5, 5), random.randint(-5, 5), 0]

    while in_constraints(x):
        #h = 0.0001
        #gv = [(fi(x[0] + h, x[1]) - fi(x[0] - h, x[1])) / (h * 2), (fi(x[0], x[1] + h) - fi(x[0], x[1] - h)) / (h * 2)]
        #x[0], x[1] = [x[0] - gv[0], x[1] - gv[1]]
        #print("help 1 ", gv, " ", x)
        x = [random.randint(-5, 5), random.randint(-5, 5), 0]
        #print("yay ", x)

    x[2] = f(x[0], x[1])
    print("Initial x: ", x)
    xn = powell(x)

    while abs(x[2] - xn[2]) > e:
        #print("help 2")
        k *= c
        x = [xn[0], xn[1], xn[2]]
        x_list.append(x)
        xn = powell(x)
    if(len(x_list) > 0):
        x_list.pop()
        x = x_list[len(x_list)-1]


    return x, x_list


e = 0.0001
_x, _x_list = interior_penalty(e)
for i in range(len(_x_list)):
    print(i+1, ". x1: ", _x_list[i][0], " x2: ", _x_list[i][1], " y: ", _x_list[i][2], " k: ", pow(10, i))
print("Solution: ", _x[0], " ", _x[1])

levels = [0.0, 0.05, 0.10, 0.3,
          0.5, 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50]
xg1 = np.arange(-5, 10.250, 0.250)
xg2 = np.arange(-5, 10.250, 0.250)
xg1, xg2 = np.meshgrid(xg1, xg2)
f2 = np.vectorize(f)
yg = f2(xg1, xg2)

x1i = np.linspace(5, -5, 100)
x2i = np.linspace(-5, 5, 100)

xe2 = np.linspace(0.1, 10, 100)
xe1 = []
for i in xe2:
    xe1.append(1 / (pow(math.e, i) * i))

cont = plt.contour(xg1, xg2, yg, levels=levels)
plt.plot(x1i, x2i, color="blue")
plt.plot(xe1, xe2, color="red")
plt.plot(_x[0], _x[1], color="black", marker=".")
plt.show()