import numpy as np


def get_node_list(a, b, n):
    nodes = []
    space = (b - a) / n
    for i in range(n + 1):
        nodes.append(a + (i * space))
    return nodes


def get_value_list(nodes, f_x, n):
    values = []
    for i in range(n + 1):
        values.append(f_x(nodes[i]))
    return values


def lagrange(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i != j:
                p1 *= (t - x[i])
                p2 *= (x[j] - x[i])
        z += + y[j] * p1 / p2
    return z
