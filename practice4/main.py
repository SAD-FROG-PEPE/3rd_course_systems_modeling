import numpy as np
import matplotlib.pyplot as plt


def p(x, lyambda):
    return lyambda * np.exp(-lyambda * x)


X = np.arange(0, 20, 0.1)
y1, y2, y3 = [], [], []
Y = [y1, y2, y3]
sigma = 0
count = 0
for y in Y:
    count += 1
    if count == 1:
        lyambda = 1.5
    if count == 2:
        lyambda = 1
    if count == 3:
        lyambda = 0.5
    for i in range(len(X)):
        y.append(p(X[i], lyambda))
    plt.plot(X, y, linewidth=1.5)
plt.title("Плотность вероятности экспоненциального закона")
plt.show()


def P(x, lyambda):
    return 1 - np.exp(-lyambda * x)


plt.plot(X, P(X, 1.5))
plt.title("Обратное преобразования для экспоненциального закона")
plt.show()


def exponential_value(lyambda, n):
    u = np.random.uniform(0, 1, n)
    x = -np.log(1 - u) / lyambda
    return x


def mean_square_deviation(x, mu):
    return np.sqrt(np.sum((x - mu) ** 2) / len(x))


N = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
array = []
for i in range(len(N)):
    x = exponential_value(1.5, N[i])
    plt.hist(x, bins=100, density=False)
    plt.title(f"Гистограммы относительных частот для {N[i]} элементов")
    p(x, 1.5)
    array.append(mean_square_deviation(x, 1 / 1.5))
    print(f'N = {N[i]}, Среднеквадратичное отклонение = {array[-1]}')
    plt.show()