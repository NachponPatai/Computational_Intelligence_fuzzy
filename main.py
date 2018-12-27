import matplotlib.pyplot as plt
import numpy as np
import rule as r
import fire as fr
plt.rcParams.update({'figure.max_open_warning': 0})
x = np.arange(0, 210, 20)
y = 0
yx = 0

time = float(input("time: "))
size = float(input("size: "))
flour = float(input("flour: "))

output1 = r.rule1(time, size, flour)
output2 = r.rule2(time, size, flour)
output3 = r.rule3(time, size, flour)
output4 = r.rule4(time, size, flour)
output5 = r.rule5(time, size, flour)
output6 = r.rule6(time, size, flour)
output7 = r.rule7(time, size, flour)
output8 = r.rule8(time, size, flour)
output9 = r.rule9(time, size, flour)
output10 = r.rule10(time, size, flour)
output11 = r.rule11(time, size, flour)
output12 = r.rule12(time, size, flour)
output13 = r.rule13(time, size, flour)
output14 = r.rule14(time, size, flour)
output15 = r.rule15(time, size, flour)
output16 = r.rule16(time, size, flour)
output17 = r.rule17(time, size, flour)
output18 = r.rule18(time, size, flour)
output19 = r.rule19(time, size, flour)
output20 = r.rule20(time, size, flour)
output21 = r.rule21(time, size, flour)
output22 = r.rule22(time, size, flour)
output23 = r.rule23(time, size, flour)
output24 = r.rule24(time, size, flour)
output25 = r.rule25(time, size, flour)
output26 = r.rule26(time, size, flour)
output27 = r.rule27(time, size, flour)


output = fr.union(output1, output2)
output = fr.union(output, output3)
output = fr.union(output, output4)
output = fr.union(output, output5)
output = fr.union(output, output6)
output = fr.union(output, output7)
output = fr.union(output, output8)
output = fr.union(output, output9)
output = fr.union(output, output10)
output = fr.union(output, output11)
output = fr.union(output, output12)
output = fr.union(output, output13)
output = fr.union(output, output14)
output = fr.union(output, output15)
output = fr.union(output, output16)
output = fr.union(output, output17)
output = fr.union(output, output18)
output = fr.union(output, output19)
output = fr.union(output, output20)
output = fr.union(output, output21)
output = fr.union(output, output22)
output = fr.union(output, output23)
output = fr.union(output, output24)
output = fr.union(output, output25)
output = fr.union(output, output26)
output = fr.union(output, output27)

print("output: ", output)
print("x: ", x)

for i in range(0, len(output)):
    y += x[i] * output[i]
    yx += output[i]
centroid = y / yx

print("Centroid: ", centroid)
plt.figure(0)
plt.plot(x, output)
plt.savefig("output.png", bbox_inches='tight')