import numpy as np


# Фунция с параметрами
def fun_with_param(a, b, x):
    return a * np.exp(-1 * (b * x)) - x


def phi_with_param(a, b, x):
    return a * np.exp(-1 * (b * x))


def derivative_fun_with_param(a, b, x):
    return -1 * a * b * np.exp(-1 * (b * x)) - 1


def derivative_phi_with_param(a, b, x):
    return -1 * (a * b) / (np.exp(b * x))


# Функция без параметров
def fun(x):
    return x * (2 ** x) - 1


def phi(x):
    return 2 ** (-x)


def derivative_fun(x):
    return (2 ** x) * (1 + np.log(2) * x)


def derivative_phi(x):
    return -1 * np.log(2) / (2 ** x)
