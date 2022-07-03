pens = int(input())
markers = int(input())
detergent = int(input())
percent_discount = int(input())

price = pens * 5.8 + markers * 7.2 + detergent * 1.2
discount = price * percent_discount / 100

print(price - discount)
