from lab_5.equations import *
import matplotlib.pyplot as plt


def iteration_method_with_param(x, eps, a, b):
    root = phi_with_param(a, b, x)
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi_with_param(a, b, x)
    print("Число итераций: ", n)
    print("С параметрами: ", root)
    plt.scatter(root, 0)


def iteration_method_without_param(x, eps):
    root = phi(x)
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi(x)
    print("Число итераций: ", n)
    print("Без параметров: ", root)
    plt.scatter(root, 0)
