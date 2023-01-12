import math
import numpy as np
import matplotlib.pyplot as plt

a = 22695477
b = 1
m = 2 ** 32
N = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5]
A = 0
B = 10
theoryMX = (B - A) / 2
theoryDX = ((B - A) ** 2) / 12
print(f"Теоретическое мат. ожидание:{theoryMX}, Теоретическая дисперсия:{theoryDX}")
print()


def method(a, b, m):
    X = 1
    while True:
        X = (a * X + b) % m
        yield X


def relative_freq(array, a, b, cuts):
    gap = np.linspace(a, b, cuts + 1)
    freqs = np.zeros(cuts)
    for x in array:
        for i in range(cuts):
            if gap[i] <= x < gap[i + 1]:
                freqs[i] += 1
                break
    return freqs / len(array)


def plot_hist(array, a, b, cuts):
    freqs = relative_freq(array, a, b, cuts)
    intervals = np.linspace(a, b, cuts + 1)
    plt.bar(intervals[:-1], freqs, width=1)
    plt.title(f"Пирсон: {np.sum((((1 / cuts) - freqs) ** 2) / freqs):.7f} для {len(array)} элементов")
    plt.show()


allX = []
for j in range(len(N)):
    X = []
    squareX = []
    chain = method(a, b, m)
    for i in range(N[j]):
        X.append(A + (B - A) * next(chain) / m)
        squareX.append(X[i] ** 2)
    for k1 in range(len(X)):
        for k2 in range(len(X)):
            if X[k1] == X[k2] and k1 != k2:
                print(f"{X[k1]}, {X[k2]},к1={k1}, к2= {k2}, период {k2 - k1}")
    allX.append(X)
    MX = math.fsum(X) / len(X)
    DX = (math.fsum(squareX) / len(X) - MX ** 2) * len(X) / (len(X) - 1)
    print(f"для последовательсности {j + 1}: Фактическое мат. ожидание: {MX}, Фактическая дисперсия: {DX}")
    print()
for x in allX:
    plot_hist(x, A, B, cuts=10)
