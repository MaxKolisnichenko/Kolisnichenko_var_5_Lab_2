#Лаб.2 Рівень 3. Варіант 5.

cars = {
    "AA1234BB": ["Toyota", "Іваненко"],
    "BC5678CC": ["BMW", "Петренко"],
    "AA9876BB": ["Toyota", "Сидоренко"],
    "BC3456CC": ["Mercedes", "Коваленко"],
    "AA1122BB": ["Honda", "Мельник"],
    "BC3344CC": ["BMW", "Шевченко"]
}

def find_owner(plate):
    return cars.get(plate, ["Номер не знайдено"])[1]  # пошук прізвища власника за номером авто

def unique_brands_stats():
    brands = {info[0] for info in cars.values()}  # підрахунок унікальних марок авто
    return len(brands), brands

plate_number = input("Введіть номер авто: ").strip().upper() # введення номера для пошуку
owner = find_owner(plate_number)
print(f"Власник авто {plate_number}: {owner}")

count, brands = unique_brands_stats() # виведення статистики унікальних марок
print(f"Кількість унікальних марок: {count}")
print(f"Список унікальних марок: {', '.join(brands)}")
