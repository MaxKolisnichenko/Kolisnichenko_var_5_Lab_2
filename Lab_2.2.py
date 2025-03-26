#Лаб.2 Рівень 2. Варіант 5.

numbers = list(map(int, input("Введіть цілі числа через пробіл: ").split()))

m = int(input("Введіть кількість рядків: "))
n = int(input("Введіть кількість стовпців: "))

if len(numbers) != m * n:
    print("Помилка! Неправильна кількість чисел.")
else:
    matrix = [numbers[i * n: (i + 1) * n] for i in range(m)]

    
    print("\nПочаткова матриця:")
    for row in matrix:
        print(row) # початкова матриця

  
    print("\nПеревернута матриця:")
    for row in reversed(matrix):
        print(row) # перевернута матриця
