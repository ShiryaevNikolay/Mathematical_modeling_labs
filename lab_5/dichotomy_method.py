from lab_5.equations import *
import matplotlib.pyplot as plt


def dichotomy_method_with_param(eps, a, b, intervalA, intervalB):
    root = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        if abs(derivative_phi_with_param(a, b, root)) >= 1:
            return print("Итерационный процесс расходится")
        n += 1
        if fun_with_param(a, b, root) == 0:
            break
        if fun_with_param(a, b, intervalA) * fun_with_param(a, b, root) < 0:
            intervalB = root
        elif fun_with_param(a, b, intervalB) * fun_with_param(a, b, root) < 0:
            intervalA = root
        root = (intervalB + intervalA) / 2
    print("Число итераций: ", n)
    print("С параметрами: ", root)
    plt.scatter(root, 0)


def dichotomy_method_without_param(eps, intervalA, intervalB):
    root = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        if abs(derivative_phi(root)) >= 1:
            return print("Итерационный процесс расходится")
        n += 1
        if fun(root) == 0:
            break
        if fun(intervalA) * fun(root) < 0:
            intervalB = root
        elif fun(intervalB) * fun(root) < 0:
            intervalA = root
        root = (intervalB + intervalA) / 2
    print("Число итераций: ", n)
    print("Без параметров: ", root)
    plt.scatter(root, 0)