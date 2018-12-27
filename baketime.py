import math
import matplotlib.pyplot as plt

def short(value):
    if 0 <= value <= 20:
        membership = ((-1/20) * value) + 1
    else:
        membership = 0

    return membership


def medium(value):
    if 15 <= value <= 50:
        membership = 1 - math.fabs((value - 32.5) / 17.5)
    else:
        membership = 0

    return membership


def high(value):
    if 45 <= value <= 90:
        membership = 1 - math.fabs((value - 67.5) / 22.5)
    else:
        membership = 0

    return membership

y1 = []
y2 = []
y3 = []
x1 = []
plt.figure(91)
for x in range(0, 100):
    y1.append(short(x))
    y2.append(medium(x))
    y3.append(high(x))
    x1.append(x)

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.legend(('short', 'medium', 'high'), loc='upper right')
plt.savefig("baketime.png", bbox_inches='tight')