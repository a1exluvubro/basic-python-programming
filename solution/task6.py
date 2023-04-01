import math

a = 0

for k in range(100):
    a+=1/math.factorial(k)
if round(a, 7) == round(math.e, 7):
    print("Равенство верно, частичная сумма ряда равна e")
else:
    print("Равнество неверн, частичная сумма ряда равна: ", a)
