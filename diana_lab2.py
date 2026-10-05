import math
x = 0.1
while x <= 0.7:
    if x < 0.2:
      print("Значення виразу 1:", round(math.log(3*x+1, 5), 3))
    elif 0.2 <= x < 0.4:
      print("Значення виразу 2:", round(x**math.cos(x), 3))
    elif x >= 0.4:
      print("Значення виразу 3:", round(1/math.sin(math.log(x)), 3))
    x += 0.05
    x = round(x, 3)

x = 1.1
while x <= 2.0:
    k = 1
    addend = (1/(2**k))*math.sin(x/(2**k))
    total_sum = 0
    d = 0.001 # похибка
    while abs(addend) >= d:
        total_sum += addend
        k += 1
        addend = (1/(2**k))*math.sin(x/(2**k))
    print(f"Значення виразу з таблиці 2 зі значенням x {x}: {total_sum}")
    x += 0.1
    x = round(x, 2)

