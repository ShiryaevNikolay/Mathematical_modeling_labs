from lab_5.equations import *
import matplotlib.pyplot as plt


def iteration_method(x0, eps, a, b):
    x1 = phi_with_param(a, b, x0)
    while abs(x1 - x0) >= eps:
        x0 = x1
        x1 = phi_with_param(a, b, x0)
    print(x1)
    plt.scatter(x1, 0)
