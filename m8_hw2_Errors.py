def personal_sum(numbers):
    res = 0
    incorrect_data = 0
    for i in numbers:
        try:
            res += i
        except TypeError as exc:
            incorrect_data += 1
            print(f'Несовпадающий тип данных - {i}')
    return (res, incorrect_data)


def calculate_average(numbers):
    try:
        summ, incorrect_data = personal_sum(numbers)
        res = summ / (len(numbers) - incorrect_data)
    except ZeroDivisionError as exc:
        res = 0
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')
        return None
    return res


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
