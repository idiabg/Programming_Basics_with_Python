from math import pi

figure = input()

if figure == 'square':
    a = float(input())
    area = a * a
    print(round(area, 3))
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(round(area, 3))
elif figure == 'circle':
    r = float(input())
    area = pi * r * r
    print(round(area, 3))

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(round(area, 3))
