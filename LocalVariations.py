import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot


def Wb(t):
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
        return a[1] * W2(t, p) + a[0] * W1(t, p) + Wb(t)
    elif n == 3:
        return a[2] * W3(t, p) + a[1] * W2(t, p) + a[0] * W1(t, p) + Wb(t)
    elif n == 4:
        return a[3] * W4(t, p) + a[2] * W3(t, p) + a[1] * W2(t, p) + a[0] * W1(t, p) + Wb(t)


def Wp1(t, a, n):
    h = 0.00001
    p = 3

    if n == 2:
        return a[1] * ((W2(t + h, p) - W2(t - h, p)) / (h * 2)) + a[0] * ((W1(t + h, p) - W1(t - h, p)) / (h * 2)) + (
                Wb(t + h) - Wb(t - h)) / (h * 2)
    elif n == 3:
        return a[2] * ((W3(t + h, p) - W3(t - h, p)) / (h * 2)) + a[1] * ((W2(t + h, p) - W2(t - h, p)) / (h * 2)) + a[
            0] * ((W1(t + h, p) - W1(t - h, p)) / (h * 2)) + (Wb(t + h) - Wb(t - h)) / (h * 2)
    elif n == 4:
        return a[3] * ((W4(t + h, p) - W4(t - h, p)) / (h * 2)) + a[2] * ((W3(t + h, p) - W3(t - h, p)) / (h * 2)) + a[
            1] * ((W2(t + h, p) - W2(t - h, p)) / (h * 2)) + a[0] * ((W1(t + h, p) - W1(t - h, p)) / (h * 2)) + (
                Wb(t + h) - Wb(t - h)) / (h * 2)


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
    return x1 * x1 - 2 * x * y + y1 * y1


def LocalVariations(t_ab, x_ab, n, e):
    def findDiff():
        _diff = 0
        t = (t_ab[1] - t_ab[0]) / (n + 1)
        dt = t
        for j in range(n + 1):
            x = xf_arr[j]
            x1 = (xf_arr[j + 1] - x) / dt
            y = x
            y1 = x1
            _diff += J(x, x1, y, y1)
            t += dt
        return _diff

    dlt = e * 10
    xf_arr = []
    t_arr = []
    init = (x_ab[1] - x_ab[0]) / t_ab[1] * 1.25
    dt = (t_ab[1] - t_ab[0]) / (n + 1)
    for i in range(n):
        xf_arr.append(init)
        t_arr.append(dt * (i + 1))
    xf_arr = [x_ab[0]] + xf_arr + [x_ab[1]]
    t_arr = [t_ab[0]] + t_arr + [t_ab[1]]

    for i in range(1, n + 1):
        diff = findDiff()
        xf_arr[i] += dlt
        newDiff = findDiff()
        if newDiff < diff:
            while newDiff < diff:
                diff = newDiff
                xf_arr[i] += dlt
                newDiff = findDiff()
            xf_arr[i] -= dlt
        else:
            xf_arr[i] -= (dlt * 2)
            newDiff = findDiff()
            while newDiff < diff:
                diff = newDiff
                xf_arr[i] -= dlt
                newDiff = findDiff()
            xf_arr[i] += dlt

    return xf_arr, t_arr


def true_x(t):
    return math.sin(t)


def true_x1(t):
    return math.cos(t)


e = 1e-5
a = 0
b = math.pi / 2
xa = 0
xb = 1

x1, t1 = LocalVariations([a, b], [xa, xb], 3, e)
x2, t2 = LocalVariations([a, b], [xa, xb], 4, e)
x3, t3 = LocalVariations([a, b], [xa, xb], 5, e)

pyplot.style.use('dark_background')
figure, axis = plt.subplots(1, 3)

t_points = []
x_true_points = []
m = 10
for i in range(m):
    t_points.append((b * i) / (m - 1))
    x_true_points.append(true_x(t_points[-1]))

int_a2 = 0
int_a3 = 0
int_a4 = 0
int_true = 0
m = 10
for i in range(m):
    int_a2 += J(W(i / m, x1, 2), Wp1(i / m, x1, 2), W(i / m, x1, 2), Wp1(i / m, x1, 2))
    int_a3 += J(W(i / m, x2, 3), Wp1(i / m, x2, 3), W(i / m, x2, 3), Wp1(i / m, x2, 3))
    int_a4 += J(W(i / m, x3, 4), Wp1(i / m, x3, 4), W(i / m, x3, 4), Wp1(i / m, x3, 4))
    int_true += J(true_x(i / m), true_x1(i / m), true_x(i / m), true_x1(i / m))

print(int_true, "\n", int_a2, "\n", int_a3, "\n", int_a4)

axis[0].plot(t_points, x_true_points)
axis[0].plot(t1, x1)
axis[0].set_title("n = 3")
axis[1].plot(t_points, x_true_points)
axis[1].plot(t2, x2)
axis[1].set_title("n = 4")
axis[2].plot(t_points, x_true_points)
axis[2].plot(t3, x3)
axis[2].set_title("n = 5")

plt.show()
