import lib as lib


xs = lib.np.linspace(-1, 1, 5)
ys = [lib.np.power(x, 2) for x in xs]
#xs = [-1, 0, 1]
#ys = [1, 0, 1]
n = len(xs)
diffs = [lib.div_diff(xs, ys, i) for i in range(n)]
interp_f = [lib.interpolated_f(xs, diffs, x) for x in xs]

print(diffs)
print(interp_f)

matrix = lib.div_diff_matrix(xs, ys)
print(matrix)
print(matrix[0])
interp_matrix_f = [lib.interpolated_f(xs, matrix[0], x) for x in xs]
print(interp_matrix_f)
