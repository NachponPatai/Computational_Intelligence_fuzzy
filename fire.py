import math
import matplotlib.pyplot as plt

def low(value, acut):
    if 0 <= value <= 120:
        membership = ((-1/120) * value) + 1
        if membership > acut:
            membership = acut
    else:
        membership = 0

    return membership


def medium(value, acut):
    if 100 <= value <= 160:
        membership = 1 - math.fabs((value - 130) / 30)
        if membership > acut:
            membership = acut
    else:
        membership = 0

    return membership


def high(value, acut):
    if 150 <= value <= 200:
        membership = 1 - math.fabs((value - 175) / 25)
        if membership > acut:
            membership = acut
    else:
        membership = 0

    return membership

def union(x, y):
    out = []
    for i in range(0, len(x)):
        ax = max(x[i], y[i])
        out.append(ax)
    return out

y1 = []
y2 = []
y3 = []
x1 = []
plt.figure(90)
for x in range(0, 210):
    y1.append(low(x,x))
    y2.append(medium(x,x))
    y3.append(high(x,x))
    x1.append(x)

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.legend(('low', 'medium', 'high'), loc='upper right')
plt.savefig("fire.png", bbox_inches='tight')