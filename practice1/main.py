import random
import math

x0, y0, r0 = random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)
ExpNmb = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]
x_max, x_min = x0 + r0, x0 - r0
y_max, y_min = y0 + r0, y0 - r0
seria = []
pogreshnost=[]
obshayaSymma = 0
for z in range(5):
    seria.clear()
    pogreshnost.clear()
    summa = 0
    for j in range(len(ExpNmb)):
        m = 0
        for i in range(ExpNmb[j]):
            xp = (x_max - x_min) * random.random() + x_min
            yp = (y_max - y_min) * random.random() + y_min
            if (xp - x0) ** 2 + (yp - y0) ** 2 < r0 ** 2:
                m += 1
        pi = 4 * m / ExpNmb[j]
        seria.append(pi)
        pogreshnost.append(abs((pi - math.pi) / math.pi))
    for v in range(len(seria)):
        summa += seria[v]
    srednee = summa / len(seria)
    obshayaSymma += srednee
    srednyayaPogreshnost = abs((srednee - math.pi) / math.pi)
    print(f"SERIA_{z + 1} ={seria}")
    print(f"погрешность ={pogreshnost}")
    print(f"среднее значение={srednee} , средняя погрешность={srednyayaPogreshnost}")
    print()
obsheeSrednee = obshayaSymma / 5
obshayaPogreshnost = abs((obsheeSrednee - math.pi) / math.pi)
print(f"среднее значение пяти серий={obsheeSrednee} , ее погрешность ={obshayaPogreshnost}")

print("------------------task 4----------------------")
ExpNmb2 = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
x_max, x_min = 2, 0
y_max, y_min = 9, 0
seria = []
pogreshnost = []
obshayaSymma = 0
for z in range(3):
    seria.clear()
    pogreshnost.clear()
    summa = 0
    for j in range(len(ExpNmb2)):
        m = 0
        for i in range(ExpNmb2[j]):
            xp = (x_max - x_min) * random.random() + x_min
            yp = (y_max - y_min) * random.random() + y_min
            if xp ** 3 + 1 > yp:
                m += 1
        S = (x_max - x_min) * (y_max - y_min) * m / ExpNmb2[j]
        seria.append(S)
        pogreshnost.append(abs((S - 6) / 6))
    for v in range(len(seria)):
        summa += seria[v]
    srednee = summa / len(seria)
    obshayaSymma += srednee
    srednyayaPogreshnost = abs((srednee - 6) / 6)
    print(f"SERIA_{z + 1} ={seria}")
    print(f"погрешность ={pogreshnost}")
    print(f"среднее значение={srednee} , погрешность={srednyayaPogreshnost}")
    print()
obsheeSrednee = obshayaSymma / 3
obshayaPogreshnost = abs((obsheeSrednee - 6) / 6)
print(f"среднее значение трех серий={obsheeSrednee} , ее погрешность ={obshayaPogreshnost}")
