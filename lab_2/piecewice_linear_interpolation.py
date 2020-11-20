def piecewice_linear_interpolation(x, y, xnew):
    for i in range(len(x) - 1):
        if x[i] <= xnew <= x[i + 1]:
            return y[i] + (y[i + 1] - y[i]) * (xnew - x[i]) / (x[i + 1] - x[i])
