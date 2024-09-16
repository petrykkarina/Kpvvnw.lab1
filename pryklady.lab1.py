import math

x = 1.549
y = 7.317

term1 = 3.14 * x**2
term2 = -7 * y**(-2)
term3 = x * y**3
term4 = 7 * math.sqrt(y)
term5 = math.log(x + 7 * math.sqrt(y))

result = term1 - term2 + term3 + term4 + term5

print(result)