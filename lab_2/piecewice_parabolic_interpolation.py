def piecewice_parabolic_interpolation(x, y, xnew):
    for i in range(len(x)):
        y0 = y[i - 1]
        y1 = y[i]
        y2 = y[i + 1]
        x0 = x[i - 1]
        x1 = x[i]
        x2 = x[i + 1]
        return y0 + (y1 - y0)*(xnew - x0)/(x1 - x0) + (1/(x2 - x0))*(xnew - x0)*(xnew - x1)*(((y2 - y1)/(x2 - x1)) - ((y1 - y0)/(x1 - x0)))
