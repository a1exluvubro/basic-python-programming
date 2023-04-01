import math

katet = float(input("Введите длину катета: "))
corner = float(input("Введите величину противолежащего угла в градусах: "))
print("Площадь треугольника равна:", 1/2*katet**2*math.tan(corner))