import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

'''
def getSquare(a, b):
    h = 0.01
    arr = np.arange(a, b, h)
    s = 0
    for i in range(len(arr)):
        s += abs((math.sin(2 * arr[i])) * h)
    return s
'''

def J(x, x1, y, y1):
    return (x1 * x1 + y1 * y1 - 2 * x * y)


def W0(t):
    return t / (math.pi / 2)


def Wi(t, p):
    return math.pow(t, p) * math.pow(t - (math.pi / 2), p)


def W1(t, p):
    return Wi(t, p) * (t * t + t)


def W2(t, p):
    return Wi(t, p) * (t * t * t - 3 * t + 2)


def W3(t, p):
    return Wi(t, p) * (math.cos(t / 2))


def W4(t, p):
    return Wi(t, p) * (math.sin(t / 2))


def W(t, a, n):
    p = 3
    if n == 2:
        return a[1] * W2(t, p) + a[0] * W1(t, p) + W0(t)
    elif n == 3:
        return a[2] * W3(t, p) + a[1] * W2(t, p) + a[0] * W1(t, p) + W0(t)
    elif n == 4:
        return a[3] * W4(t, p) + a[2] * W3(t, p) + a[1] * W2(t, p) + a[0] * W1(t, p) + W0(t)


def Wp1(t, a, n):
    h = 0.00001
    p = 3

    if n == 2:
        return a[1] * ((W2(t + h, p) - W2(t - h, p)) / (h * 2)) + a[0] * ((W1(t + h, p) - W1(t - h, p)) / (h * 2)) + (
                W0(t + h) - W0(t - h)) / (h * 2)
    elif n == 3:
        return a[2] * ((W3(t + h, p) - W3(t - h, p)) / (h * 2)) + a[1] * ((W2(t + h, p) - W2(t - h, p)) / (h * 2)) + a[
            0] * ((W1(t + h, p) - W1(t - h, p)) / (h * 2)) + (W0(t + h) - W0(t - h)) / (h * 2)
    elif n == 4:
        return a[3] * ((W4(t + h, p) - W4(t - h, p)) / (h * 2)) + a[2] * ((W3(t + h, p) - W3(t - h, p)) / (h * 2)) + a[
            1] * ((W2(t + h, p) - W2(t - h, p)) / (h * 2)) + a[0] * ((W1(t + h, p) - W1(t - h, p)) / (h * 2)) + (
                W0(t + h) - W0(t - h)) / (h * 2)


def ritz(ta, tb, a, n, e):
    def findDiff():
        t = dt
        _diff = 0
        for j in range(n):
            x = W(t, a, n)
            x1 = Wp1(t, a, n)
            y = W(t, a, n)
            y1 = Wp1(t, a, n)
            _diff += J(x, x1, y, y1)
            t += dt
        return abs(_diff)

    dlt = e * 10
    dt = (tb - ta) / (n + 1)
    for i in range(n):
        diff = findDiff()
        a[i] += dlt
        new_diff = findDiff()
        if new_diff < diff:
            while new_diff < diff:
                diff = new_diff
                a[i] += dlt
                new_diff = findDiff()
            a[i] -= dlt

        else:
            a[i] -= dlt * 2
            new_diff = findDiff()
            while new_diff < diff:
                diff = new_diff
                a[i] -= dlt
                new_diff = findDiff()
            a[i] += dlt

    return a


def true_x(t):
    return math.sin(t)


def true_x1(t):
    return math.cos(t)


matplotlib.pyplot.style.use('dark_background')
e = 1e-4
_a = [0.5, 0.5, 0.5, 0.5]
ta = 0
tb = math.pi / 2
fa = 0
fb = 1

a2, a3, a4 = _a.copy(), _a.copy(), _a.copy()
a2 = ritz(ta, tb, a2, 2, e)
a3 = ritz(ta, tb, a3, 3, e)
a4 = ritz(ta, tb, a4, 4, e)


figure, axis = plt.subplots(1, 3)

t_points = []
x_points2 = []
x_points3 = []
x_points4 = []
x_true_points = []
m = 100
for i in range(m):
    t_points.append((tb * i) / (m - 1))
    x_true_points.append(true_x(t_points[-1]))
    x_points2.append(W(t_points[-1], a2, 2))
    x_points3.append(W(t_points[-1], a3, 3))
    x_points4.append(W(t_points[-1], a4, 4))

int_a2 = 0
int_a3 = 0
int_a4 = 0
int_true = 0
m = 100
for i in range(m):
    int_a2 += J(W(i / m, a2, 2), Wp1(i / m, a2, 2), W(i / m, a2, 2), Wp1(i / m, a2, 2))
    int_a3 += J(W(i / m, a3, 3), Wp1(i / m, a3, 3), W(i / m, a3, 3), Wp1(i / m, a3, 3))
    int_a4 += J(W(i / m, a4, 4), Wp1(i / m, a4, 4), W(i / m, a4, 4), Wp1(i / m, a4, 4))
    int_true += J(true_x(i / m), true_x1(i / m), true_x(i / m), true_x1(i / m))

print("",int_true, "\nn = 2", int_a2, "\nn = 3", int_a3, "\nn = 4", int_a4)

# print(d1,d2,d3)
# print(getSquare(_ta,_tb))

axis[0].plot(t_points, x_true_points)
axis[0].plot(t_points, x_points2)
axis[0].set_title("n = 2")
axis[1].plot(t_points, x_true_points)
axis[1].plot(t_points, x_points3)
axis[1].set_title("n = 3")
axis[2].plot(t_points, x_true_points)
axis[2].plot(t_points, x_points4)
axis[2].set_title("n = 4")

plt.show()
