n = 0
z = 0
while n != 20:
    print(f'results_n{n}_z{z}.bin')
    z += 10
    if z == 100+10:
        n += 5
        z = 0