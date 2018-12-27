import math
import matplotlib.pyplot as plt

def soft(value):
    if 0 <= value <= 3:
        membership = ((-1 / 3) * value) + 1
    else:
        membership = 0

    return membership


def medium(value):
    if 2 <= value <= 6:
        membership = 1 - math.fabs((value - 4) / 2)
    else:
        membership = 0

    return membership


def hard(value):
    if 5 <= value <= 10:
        membership = 1 - math.fabs((value - 7.5) / 2.5)
    else:
        membership = 0

    return membership


y1 = []
y2 = []
y3 = []
x1 = []
plt.figure(93)
for x in range(0, 11):
    y1.append(soft(x))
    y2.append(medium(x))
    y3.append(hard(x))
    x1.append(x)

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.legend(('soft', 'medium', 'hard'), loc='upper right')
plt.savefig("flour.png", bbox_inches='tight')