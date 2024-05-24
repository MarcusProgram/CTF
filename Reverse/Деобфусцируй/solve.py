import sympy as sp

a, b, c, d, e, f, g, h, i = sp.symbols('a b c d e f g h i')

eq1 = b - c
eq2 = c - g
eq3 = g - h
eq4 = g + b + c
eq5 = 3*a + 12*d + e + 4*f + 6*i - 2194
eq6 = -6*a + 2*d - 4*e - f + 9*i + 243
eq7 = a + 6*d + 2*e + 7*f + 11*i - 2307
eq8 = 5*a - 2*d - 7*e + 76*f + 8*i - 8238
eq9 = 2*a - 2*d - 2*e - 2*f + 2*i + 72

solution = sp.solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (a, b, c, d, e, f, g, h, i))

print("Solution :")
for var, value in solution.items():
    print(value,end=' ')