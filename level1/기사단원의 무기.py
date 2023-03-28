# 풀이1 (66.7%) : 시간 초과
def solution(number, limit, power):
    hero = [0] * (number + 1)
    for i in range(1, number + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        hero[i] = count if count <= limit else power

    return sum(hero)

# 풀이2(100%)
def solution(number, limit, power):
    hero = [0] * (number + 2)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            hero[j] += 1
        hero[i] = hero[i] if hero[i] <= limit else power
    # print(hero)
    return sum(hero)
