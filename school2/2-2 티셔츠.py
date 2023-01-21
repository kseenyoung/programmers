def solution(people, tshirts):
    people.sort()
    tshirts.sort()
    result = 0
    p = 0
    for t in tshirts:
        if p == len(people):
            break
        if t >= people[p]:
            p += 1
    return p