deposit = float(input())
term = int(input())
interest_rate = float(input())

deposit_sum = deposit + term * deposit * interest_rate / 100 / 12

print(deposit_sum)
