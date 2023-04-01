import math

k = 1
a = math.pi ** 2 / 12
row = pow(-1, k+1) / k**2

while round(a, 10) != round(row, 10):
    k+=1
    row+=pow(-1, k+1) / k**2
    print(k)
print("Ответ: ", k)