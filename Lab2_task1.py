money = 20000
salary = 5000
spend1 = 6000
increase = 0.05

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
i = 0
while (money > 0):
    money = money + salary - (spend1*(((increase+1)**i)))
    i = i + 1
print("Количество месяцев, которое можно протянуть без долгов:", i-1)
