from collections import Counter
people = [2, 3]
tshirts = [1, 2, 3]

def solution(people, tshirts):
    people.sort()
    tshirts.sort()
    p = 0
    for t in tshirts:
        if p >= len(people):
            break
        if t >= people[p]:
            p += 1

    return p


print(solution(people, tshirts))