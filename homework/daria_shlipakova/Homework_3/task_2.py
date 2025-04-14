import random

x = random.randint(1, 50)
y = random.randint(1, 50)

result1 = x - y / 1 + x * y
result2 = (x - y) / (1 + x * y)

print('x =', x)
print('y =', y)
print('x − y / 1 + xy =', result1)
print('(x − y) / (1 + xy) =', result2)
