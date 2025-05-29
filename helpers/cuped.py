
import numpy as np


def cuped(x, y):
    # calculate theta
    cov = np.cov(x, y, ddof=1)[0, 1]
    var = np.var(x, ddof=1)
    theta = cov / var
    import plotly.graph_objects as go

    # adjust Y
    x_bar = np.mean(x)
    y_adj = y - theta * (x - x_bar)

    return y_adj


def cuped_simplified(x, y):
    # calculate theta
    cov = np.cov(x, y)[0, 1]
    var = np.var(x)
    theta = cov / var

    # adjust Y
    y_adj = y - theta * x

    return y_adj
