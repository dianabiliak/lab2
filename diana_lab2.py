import math
x = 0.1
while x <= 0.7:
    if x < 0.2:
      print("Значення виразу 1:", round(math.log(3*x+1, 5), 3))
    elif x < 0.4:
      print("Значення виразу 2:", round(x**math.cos(x), 3))
    else:
      print("Значення виразу 3:", round(1/math.sin(math.log(x)), 3))
    x += 0.05
    x = round(x, 3)

x = 1.1
d = 0.001 # похибка
while x <= 2.0:
    k = 1
    total_sum = 0
    while True:
      addend = (1/(2**k))*math.sin(x/(2**k))
      k += 1
      if abs(addend) <= d:
       break
      else:
        total_sum += addend

        
    print(f"Значення виразу з таблиці 2 зі значенням x {x}", round(total_sum, 3))
    x += 0.1
    x = round(x, 2)

