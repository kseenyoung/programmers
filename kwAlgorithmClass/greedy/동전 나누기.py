c = int(input())

money = [10000, 5000, 500, 100, 50, 10]
result = 0
for m in money:
    result += c//m
    c %= m

print(result)