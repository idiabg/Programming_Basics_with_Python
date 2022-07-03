nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

mats = (nylon + 2) * 1.5 + (paint * 14.5 + paint * 14.5 * 10 / 100) + thinner * 5 + 0.4
work = mats * 30 / 100 * hours

print(mats + work)
