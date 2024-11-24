numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
m = 0
n = 0
for i in range(len(numbers)):
    if(numbers[i] is None):
        m = i
    else:
        n = n + numbers[i]
numbers[m] = (n/(len(numbers)))
print("Итог:", numbers)


