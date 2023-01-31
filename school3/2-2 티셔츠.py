#풀이1(20%)
def solution1(people, tshirts):
    answer = 0
    people.sort()
    tshirts.sort()
    t = 0

    for p in people:
        while t < len(tshirts) and tshirts[t] < p:
            t += 1
        if t == len(tshirts):
            break
        answer += 1

    return answer

#풀이2(100%)
def solution2(people, tshirts):
    answer = 0
    people.sort()
    tshirts.sort()
    t = 0

    for p in people:
        while t < len(tshirts) and tshirts[t] < p:
            t += 1
        if t == len(tshirts):
            break
        if tshirts[t] >= p:
            t += 1
            answer += 1

    return answer