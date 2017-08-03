from sympy import *

print E ** (I * pi) + 1

x = Symbol('x')
print x
print type(x)
print expand(E ** (I * x))
print expand(E ** (I * x), complex=True)

x = Symbol("x", real=True)
print expand(exp(I * x), complex=True)

tmp = series(exp(I * x), x, 0, 10)
pprint(tmp)
