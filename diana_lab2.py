import math
x = 0.1
interval = [0.1, 0.7]
for x in interval:
    x += 0.05
if x < 0.2:
    print("Значення виразу 1:", math.log(3*x+1, 5))
elif x >= 0.2 or x < 0.4:
    print("Значення виразу 2:", x**math.cos(x))
elif x >= 0.4:
    print("Значення виразу 3:", 1/math.sin(ln(x)))

x = 1.1
k = 1
while x <= 2.0:
    addent = (1/(2**k))*math.sin(x/2*k)
    print(f"Значення виразу з таблиці 2: {addent}")
    if addent < 0.001 or x <= 2.0:
        k += 1
        x += 0.1
    else:
        break
    
