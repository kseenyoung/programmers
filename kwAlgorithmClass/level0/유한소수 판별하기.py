import math


def solution(a, b):
    temp = b // math.gcd(a, b)

    # for i in range(2, temp):
    #     if temp % i == 0:
    #         if i == 2 or i == 5:
    #             temp %= i
    #         else:
    #             return 2
    #     if temp == 0:
    #         break
    # return 1
    while temp % 2 == 0:
        temp //= 2
    while temp % 5 == 0:
        temp // 5

    return 1 if temp == 1 else 2


print(solution(12, 21))