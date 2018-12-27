import size as s
import baketime as t
import flour as f
import fire as fr
import matplotlib.pyplot as plt
import numpy as np

def Graph(x, y, rule,f):
    plt.figure(f)
    plt.plot(x, y)
    plt.savefig(rule, bbox_inches='tight')

#time is short, size is small, flour is soft so fire is low
def rule1(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.small(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0,len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule1", 1)
    return y


def rule2(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.small(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule2", 2)
    return y


def rule3(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.small(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule3", 3)
    return y

def rule4(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.medium(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule4", 4)
    return y

def rule5(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.medium(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule5", 5)
    return y


def rule6(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.medium(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule6", 6)
    return y

def rule7(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.high(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule7", 7)
    return y

def rule8(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.high(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule8", 8)
    return y

def rule9(time, size, flour):
    mem_time = t.short(time)
    mem_size = s.high(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule9", 9)
    return y

def rule10(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.small(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule10", 10)
    return y

def rule11(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.small(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule11", 11)
    return y

def rule12(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.small(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule12", 12)
    return y

def rule13(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.medium(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule13", 13)
    return y

def rule14(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.medium(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule14", 14)
    return y

def rule15(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.medium(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule15", 15)
    return y

def rule16(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.high(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule16", 16)
    return y

def rule17(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.high(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule17", 17)
    return y

def rule18(time, size, flour):
    mem_time = t.medium(time)
    mem_size = s.high(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule18", 18)
    return y

def rule19(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.small(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule19", 19)
    return y

def rule20(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.small(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule20", 20)
    return y

def rule21(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.small(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule21", 21)
    return y

def rule22(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.medium(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.low(x[i], acut), 2))

    Graph(x, y, "rule22", 22)
    return y

def rule23(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.medium(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule23", 23)
    return y

def rule24(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.medium(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule24", 24)
    return y

def rule25(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.high(size)
    mem_flour = f.soft(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule25", 25)
    return y

def rule26(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.high(size)
    mem_flour = f.medium(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.medium(x[i], acut), 2))

    Graph(x, y, "rule26", 26)
    return y

def rule27(time, size, flour):
    mem_time = t.high(time)
    mem_size = s.high(size)
    mem_flour = f.hard(flour)

    x = np.arange(0, 210, 20)
    y = []

    acut = min(mem_time, mem_size, mem_flour)

    for i in range(0, len(x)):
        y.append(round(fr.high(x[i], acut), 2))

    Graph(x, y, "rule27", 27)
    return y