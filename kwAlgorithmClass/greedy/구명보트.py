def solution(people, limit):
    answer = 0
    people.sort()
    #내 풀이
    # visited = [False] * len(people)
    #
    # for i in range(len(people)):
    #     if i == len(people) - 1:
    #         answer += 1
    #     else:
    #         if not visited[i]:
    #             if people[i] + people[i + 1] <= 100:
    #                 people[i:i + 2] = [True, True]
    #             else:
    #                 people[i] = True
    #             answer += 1
    # return answer

    #정답
    s = 0
    e = len(people) - 1

    while s <= e:
        if people[s] + people[e] > limit:
            e -= 1
            answer += 1
        else:
            s += 1
            e -= 1
            answer += 1
    return answer



print(solution([70, 50, 80, 50], 100))