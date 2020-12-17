from lab_5.equations import *
import matplotlib.pyplot as plt


def newton_method_with_param(x, n, a, b):
    root = x
    for i in range(n):
        root = x - (fun_with_param(a, b, x) / derivative_fun_with_param(a, b, x))
        x = root
    print("Число итераций: ", n)
    print("С параметрами: ", root)
    plt.scatter(root, 0)


def newton_method_without_param(x, n):
    root = x
    for i in range(n):
        root = x - (fun(x) / derivative_fun(x))
        x = root
    print("Число итераций: ", n)
    print("Без параметров: ", root)
    plt.scatter(root, 0)
