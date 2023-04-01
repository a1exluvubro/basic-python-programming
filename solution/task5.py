import math

e = float(input("Введите ваше число эксцентриситет: "))
print("Тип орбиты:")
if e == 0:
    print("Круговая орбита")
elif 0 < e < 1:
    print("Эллиптическая орбита")
elif e == 1:
    print("Параболическая орбита")
elif 1 < e < math.inf:
    print("Гиперболическая орбита")
elif e == math.inf:
    print("Прямая")
else:
    print("Эксцентриситет < 0")