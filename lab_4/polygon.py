import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
import scipy.special as special
import numpy as np
from scipy import integrate
from scipy import integrate


def step_fun(point, a, b, deltaX, N, x, K, index, m, sigma):
    # массив для хранения количества xi, попавших в интервал
    sum = []
    # массив выборочных вероятностей
    F = [0]
    # массив для хранения координат по оси Х
    fx = [a]
    for q in range(K):
        sum.append(0)
        # правая граница интервала
        b = a + (q + 1) * deltaX
        fx.append(b)
        for i in range(len(x)):
            # если xi попадает в интервал, то добавляем в массив сумм
            if a <= x[i] < b:
                sum[q] += 1
        F.append(sum[q] / N)
    # индекс для постоения двух графиков на одном окне
    index += 1
    # строим ступенчатую диаграмму и показываем графики
    plt.step(fx, F)
    if point == 0:
        plt.title("Равномерное распределение")
        fx_even(a, b, fx)
    elif point == 1:
        plt.title("Нормальное распределение")
        fx_gauss(fx, m, sigma)
    # elif point == 2:
    #     plt.title("Распределение Рэлея")
    #     fx_rayleigh(fx, sigma)
    plt.show()


# функция непрерывного распределения
def fx_even(a, b, fx):
    fy = []
    for i in range(len(fx)):
        fy.append(((fx[i] - a) / (b - a)))
    plt.plot(fx, fy, linewidth=3, color='r')


# функция гаусовского распределения
def fx_gauss(fx, m, sigma):
    fy = []
    for i in range(len(fx)):
        fy.append((1 / 2) * (1 + special.erf((fx[i] - m) / (np.sqrt(2 * sigma**2)))))
    print(fy)
    plt.plot(fx, fy, linewidth=3, color='r')


# функция рэлеевского распределения
def fx_rayleigh(fx, sigma):
    fy = []
    for i in range(len(fx)):
        fy.append(1 - np.exp(-(fx[i] ** 2) / (2 * sigma ** 2)))
    plt.plot(fx, fy, linewidth=3, color='r')


def find_func(t, sigma):
    return np.exp(-t**2 / (2 * sigma**2))
