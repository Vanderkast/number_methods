import matplotlib.pyplot as mpl
import lib


def f_x(x):
    return lib.np.power(x, 2)


print('Введите степень многочлена Ньютона: ')
n = int(input())

a, b = -10, 10

x_f = lib.np.linspace(a, b, 1000)
y_f = [f_x(i) for i in x_f]


xs = lib.np.linspace(a, b, n)
print("params: {}".format(xs))
ys = [f_x(i) for i in xs]
print("values {}".format(ys))
print("keks: {}".format(lib.div_diff(xs, ys, 0)))

diffs = [lib.div_diff(xs, ys, i) for i in range(n)]
print("diffs {}".format(diffs))
y_formula = [lib.interpolated_f(xs, diffs, x) for x in xs]
print(y_formula)

inductive_diffs = lib.div_diff_matrix(xs, ys)[0]
print("inductive diffs {}".format(inductive_diffs))
y_inductive = [lib.interpolated_f(xs, inductive_diffs, x) for x in xs]
print("inductive y values: {}".format(y_inductive))

mpl.plot(x_f, y_f, linewidth=2)
mpl.plot(xs, y_formula, linewidth=1.7)
mpl.plot(xs, y_inductive, linewidth=1)

mpl.grid(True)
mpl.ylim(min(y_f)*1.2, max(y_f)*1.2)
mpl.legend(("f(x)", "interpolated f(x)", "inductive interp. f(x)"))
mpl.savefig('graph.png', format='png', dpi=300)
mpl.show()
