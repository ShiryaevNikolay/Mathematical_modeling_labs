from lab_5.equations import *
import matplotlib.pyplot as plt


def newton_method_with_param(x0, n, a, b):
    x1 = x0
    for i in range(n):
        x1 = x0 - (fun_with_param(a, b, x0) / derivative_fun_with_param(a, b, x0))
        x0 = x1
    print("С параметрами: ", x1)
    plt.scatter(x1, 0)


def newton_method_without_param(x0, n):
    x1 = x0
    for i in range(n):
        x1 = x0 - (fun(x0) / derivative_fun(x0))
        x0 = x1
    print("Без параметров: ", x1)
    plt.scatter(x1, 0)
