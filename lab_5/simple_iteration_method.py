from lab_5.equations import *
import matplotlib.pyplot as plt


def iteration_method_with_param(x0, eps, a, b):
    x1 = phi_with_param(a, b, x0)
    while abs(x1 - x0) >= eps:
        x0 = x1
        x1 = phi_with_param(a, b, x0)
    print("С параметрами: ", x1)
    plt.scatter(x1, 0)


def iteration_method_without_param(x0, eps):
    x1 = phi(x0)
    while abs(x1 - x0) >= eps:
        x0 = x1
        x1 = phi(x0)
    print("Без параметров: ", x1)
    plt.scatter(x1, 0)
