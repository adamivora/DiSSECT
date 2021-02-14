from sage.all import *

pr = PolynomialRing(ZZ, ('a', 'd', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, d, X1, X2, Y1, Y2 = pr.gens()
Z1, Z2 = 1, 1
formula = {}
C = X1 * X2
formula['C'] = C
D = Y1 * Y2
formula['D'] = D
E = C * D
formula['E'] = E
t0 = a * D
formula['t0'] = t0
H = C - t0
formula['H'] = H
t1 = X1 + Y1
formula['t1'] = t1
t2 = X2 + Y2
formula['t2'] = t2
t3 = t1 * t2
formula['t3'] = t3
t4 = t3 - C
formula['t4'] = t4
I = t4 - D
formula['I'] = I
t5 = E + d
formula['t5'] = t5
X3 = t5 * H
formula['X3'] = X3
t6 = E - d
formula['t6'] = t6
Y3 = t6 * I
formula['Y3'] = Y3
Z3 = H * I
formula['Z3'] = Z3
for key, value in formula.items():
    print(f'{key} = {value}')
