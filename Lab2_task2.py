import math

salary = 5000
spend1 = 6000
months = 10
increase = 0.03

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money = 0
for i in range(months):
    money = money + spend1*(((increase+1)**i)) - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money))
