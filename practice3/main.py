import numpy as np
import matplotlib.pyplot as plt


class Approximation:
    def __init__(self, sample, regions, nbins, m, sigma, max_i=10):
        self.sample = sample
        self.regions = regions
        self.nbins = nbins
        self.max_i = max_i
        self.m = m
        self.sigma = sigma

    def approximation(self):
        a, b = 0, 20
        rectangle_size = 1 / (self.regions)
        X = np.array([])
        dX = 0.01
        current_x = a
        current_area, rectangle_length = 0, 0
        Z = np.ones(self.sample)
        while current_x < b:
            rectangle_length = rectangle_length + dX
            current_area = ((1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (current_x ** 2)) - (
                    1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (rectangle_length ** 2))) * rectangle_length
            if current_area > rectangle_size:
                X = np.append(X, rectangle_length)
                current_x = rectangle_length
        Y = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (X ** 2))
        for j in range(self.sample):
            num = 0
            while (Z[j] == 1) and num < self.max_i:
                i = np.random.randint(0, len(X))
                u0 = np.random.uniform(-1, 1)
                u1 = np.random.uniform(0, 1)
                x = u0 * X[i]
                if abs(x) < X[i - 1]:
                    Z[j] = x
                else:
                    y = Y[i] + u1 * (Y[i - 1] - Y[i])
                    point = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (x ** 2))
                    if y < point:
                        Z[j] = x
                num = num + 1

        gap = np.linspace(a, b, 100 + 1)
        freqs = np.zeros(100)
        for x in Z:
            for i in range(100):
                if gap[i] <= a + (b - a) * x < gap[i + 1]:
                    freqs[i] += 1
                    break
        freqs = freqs / len(Z)
        intervals = np.linspace(a, b, 100 + 1)
        plt.bar(intervals[:-1], freqs, width=1)
        plt.title(f"Гистограммы относительных частот для {len(Z)} элементов")
        plt.show()
        return Z

    def plot_matplotlib(self):
        data = self.approximation()
        data = data * self.sigma + self.m
        plt.hist(data, bins=self.nbins, density=True)
        plt.grid(True)
        plt.title("Функция плотности вероятности")


def px(x, m, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - m) ** 2) / (2 * sigma ** 2))


def task(m, sigma, N):
    x = np.linspace(0, 20, 100)
    plt.plot(x, px(x, m, sigma), linewidth=1, label=f"{m = }; {sigma = }", )
    plt.legend()
    plt.title(f"Нормальное распределение для {N}")


def root_mean_square_deviation(data, m):
    squareData = []
    MX = np.sum(data) / len(data)
    for i in range(len(data)):
        swuare = data[i]
        squareData.append(swuare ** 2)
    DX = (np.sum(squareData) / len(data) - MX ** 2) * len(data) / (len(data) - 1)
    return DX


def main():
    X = range(0, 21, 2)
    y1, y2, y3, y4 = [], [], [], []
    Y = [y1, y2, y3, y4]
    sigma = 0
    count = 0
    for y in Y:
        count += 1
        if count == 4:
            M = 12
            sigma = 1
        else:
            M = 10
            if count == 1:
                sigma = 2
            if count == 2:
                sigma = 1
            if count == 3:
                sigma = 0.5
        for i in range(len(X)):
            y.append(px(X[i], M, sigma))
        plt.plot(X, y, linewidth=2, label=f'Мат ожидание={M}, Сигма = {sigma}')
    plt.title("Распределение плотности вероятности")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()
    a, b = 0, 20
    theoryMX = (b - a) / 2
    theoryDX = ((b - a) ** 2) / 12
    print(f"Теоретическое мат. ожидание:{theoryMX}, Теоретическое среднеквадратичное отклонение:{np.sqrt(theoryDX)}")
    rmsd = []
    N = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
    for i in range(len(N)):
        m, sigma = 10, 2
        z = Approximation(N[i], regions=100, nbins=100, m=m, sigma=sigma)
        z.plot_matplotlib()
        task(m, sigma, N[i])
        plt.show()
        data = z.approximation()
        data = data * sigma + m
        rmsd.append(np.sqrt(theoryDX) - root_mean_square_deviation(data, m))
        print(f'N = {N[i]}, среднеквадратичное отклонение = {rmsd[-1]}')
    plt.plot( rmsd, N, linewidth=1)
    plt.title(f"Среднеквадратичное отклонение в зависимости от N")
    plt.show()


if __name__ == '__main__':
    main()