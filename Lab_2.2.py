#Лаб.2 Рівень 2. Варіант 5.

input_str = input("Введіть цілі числа через пробіл: ")
if not all(s.strip('-').isdigit() for s in input_str.split()):
    print("Помилка! У введених даних повинні бути тільки цілі числа.")
else:
    numbers = list(map(int, input_str.split()))

    try:
        m = int(input("Введіть кількість рядків: "))
        n = int(input("Введіть кількість стовпців: "))
        
        if m <= 0 or n <= 0:
            print("Помилка! Кількість рядків і стовпців повинна бути більшою за 0.")
        elif len(numbers) != m * n:
            print("Помилка! Неправильна кількість чисел для матриці розміром", m, "x", n)
        else:
            matrix = [numbers[i * n: (i + 1) * n] for i in range(m)]

            print("\nПочаткова матриця:")
            for row in matrix:
                print(row)

            print("\nПеревернута матриця (по горизонталі):")
            for row in reversed(matrix):
                print(row)
    except ValueError:
        print("Помилка! Введено неціле число для розміру матриці.")
