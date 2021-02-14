from sage.all import *

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
Z1, Z2 = 1, 1
formula = {}
u = Y2 - Y1
formula['u'] = u
uu = u ** 2
formula['uu'] = uu
v = X2 - X1
formula['v'] = v
vv = v ** 2
formula['vv'] = vv
vvv = v * vv
formula['vvv'] = vvv
R = vv * X1
formula['R'] = R
t0 = 2 * R
formula['t0'] = t0
t1 = uu - vvv
formula['t1'] = t1
A = t1 - t0
formula['A'] = A
X3 = v * A
formula['X3'] = X3
t2 = R - A
formula['t2'] = t2
t3 = vvv * Y1
formula['t3'] = t3
t4 = u * t2
formula['t4'] = t4
Y3 = t4 - t3
formula['Y3'] = Y3
Z3 = vvv
formula['Z3'] = Z3
for key, value in formula.items():
    print(f'{key} = {value}')
