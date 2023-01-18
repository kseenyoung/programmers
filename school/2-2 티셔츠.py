from collections import Counter
people = [2, 3]
tshirts = [1, 2, 3]

def solution(people, tshirts):
    answer = len(people)
    for i in tshirts:
        if i in people:
            tshirts.remove(i)
            people.remove(i)

    for i in tshirts:
        for j in people:
            if j < i:
                people.pop()
                break

    return answer - len(people)


print(solution(people, tshirts))