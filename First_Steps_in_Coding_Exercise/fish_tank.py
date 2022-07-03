length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height / 1000

print(volume * (1 - percentage / 100))
