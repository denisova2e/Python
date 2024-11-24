# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    a = 0
    for element in l:
        if element == item:
            a = a + 1
    return a

my_list = [645, 2432546, 645, 63643316, 81, 684, 88]

# Подсчитываем количество вхождений числа 1
result = my_count(my_list, 645)
print(f"Число 645 встречается в списке {result} раз.")


result = my_count(my_list, 81)
print(f"Число 81 встречается в списке {result} раз.")