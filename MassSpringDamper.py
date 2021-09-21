import math
import matplotlib.pyplot as plt

m = float(input("Massa objek (kg): "))
k = float(input("Konstanta pegas (kg/s): "))
c = float(input("Koefisien peredaman (kg/s): "))
y0 = float(input("Simpangan awal (m): "))
t = float(input("Waktu pengamatan (s): "))
n = int(input("Jumlah pengamatan: "))

alpha = c/(2*m)
omega = math.sqrt((k/m) - (c**2/(4*m**2)))
increment = t/n
tn = 0.0

listT = []
listY = []

for x in range(n+1):
    listT.append(tn)
    listY.append(((math.e**(-alpha*tn))) * (y0*math.cos(omega*tn) + y0*(alpha/omega)*math.sin(omega*tn)))
    tn = tn + increment

nformat = "{:2d}"
ynformat = "{: .8f}"
tnformat = "{0:.2f}"

for i in range(len(listY)):
    print(nformat.format(i) + ". t = " + tnformat.format(listT[i]) + ", y = " + ynformat.format(listY[i]))

plt.plot(listT, listY)
plt.show()