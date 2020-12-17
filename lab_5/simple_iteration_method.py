from lab_5.equations import *
import matplotlib.pyplot as plt


def iteration_method_with_param(x, eps, a, b):
    root = phi_with_param(a, b, x)
    while abs(root - x) >= eps:
        x = root
        root = phi_with_param(a, b, x)
    print("С параметрами: ", root)
    plt.scatter(root, 0)


def iteration_method_without_param(x, eps):
    root = phi(x)
    while abs(root - x) >= eps:
        x = root
        root = phi(x)
    print("Без параметров: ", root)
    plt.scatter(root, 0)
