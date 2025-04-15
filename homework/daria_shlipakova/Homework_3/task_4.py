import math
import random

leg_a = random.randint(1, 50)
leg_b = random.randint(1, 50)

hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
area = (leg_a * leg_b) / 2

print('Катет a =', leg_a)
print('Катет b =', leg_b)
print('Гипотенуза c =', hypotenuse)
print('Площадь треугольника =', area)
