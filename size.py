import math
import matplotlib.pyplot as plt

def small(value):
    if 0 <= value <= 30:
        membership = ((-1 / 30) * value) + 1
    else:
        membership = 0

    return membership


def medium(value):
    if 25 <= value <= 60:
        membership = 1 - math.fabs((value - 42.5) / 17.5)

    else:
        membership = 0

    return membership


def high(value):
    if 50 <= value <= 100:
        membership = 1 - math.fabs((value - 75) / 25)
    else:
        membership = 0

    return membership

y1 = []
y2 = []
y3 = []
x1 = []
plt.figure(92)
for x in range(0, 110):
    y1.append(small(x))
    y2.append(medium(x))
    y3.append(high(x))
    x1.append(x)

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.savefig("size.png", bbox_inches='tight')



