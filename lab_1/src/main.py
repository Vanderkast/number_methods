import lib as lib
import matplotlib.pyplot as mpl


def f_x(x):
    return lib.np.power(x, 2)


print("Введите степень интерполяционного многочлена Лагранжа")
n = int(input())

print("Введите отрезок [a,b]")
a = float(input())
b = float(input())

nf = 1000
x_f = lib.get_node_list(a, b, nf)
y_f = lib.get_value_list(x_f, f_x, nf)

x_lag = lib.get_node_list(a, b, n)
y_lag = lib.get_value_list(x_lag, f_x, n)

xnew = lib.np.linspace(a, b, n)
ynew = [lib.lagrange(x_lag, y_lag, i) for i in xnew]
mpl.plot(x_f, y_f, linewidth=2)
mpl.plot(xnew, ynew, linewidth=1)

mpl.grid(True)
mpl.ylim(min(y_f)*1.2, max(y_f)*1.2)
mpl.legend(("f(x)", "interpolated f(x), n={}".format(n)))
mpl.savefig('graph.png', format='png', dpi=300)
mpl.show()
