import math
import random

a = random.randint(1, 50)
b = random.randint(1, 50)

arithmetic_mean = (a + b) / 2
geometric_mean = math.sqrt(a * b)

print('Первое число:', a)
print('Второе число:', b)
print('Среднее арифметическое:', arithmetic_mean)
print('Среднее геометрическое:', geometric_mean)
