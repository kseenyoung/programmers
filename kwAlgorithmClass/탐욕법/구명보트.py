def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    answer = 0
    while start <= end:  # 가장 적게 나가는 사람 + 가장 많이 나가는 사람 <= limit 일 때 가장 많이 2명을 태울 수 있다.
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1

    return answer





print(solution([70, 50, 80, 50],	100))