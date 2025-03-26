#Лаб.2 Рівень 1. Варіант 5.

import random

arr = [random.randint(1, 100) for _ in range(20)]

multiples11= [num for num in arr if num % 11 == 0]

multiples11.sort(reverse=True)

print("Згенерований масив:", arr)
print("Числа, кратні 11 у порядку спадання:", multiples11)
