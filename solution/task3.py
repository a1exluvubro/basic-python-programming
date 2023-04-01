import math

R = float(input("Введите радиус шара: "))
print("Объем равен:", 4/3*math.pi*R)

print("Проверка равенства e^(i*pi) = -1: ")
if math.e ** (math.pi*(0+1j)) == -1:
    print("Равенство верно")
else: 
    print("Равенство неверно")