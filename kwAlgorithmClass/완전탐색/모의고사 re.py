def solution(answers):
    # 내 풀이(맞음)
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = [0]*3

    for j, student in enumerate(students):  # 한 명씩 채점
        for i, a in enumerate(answers):
            if a == student[i % len(student)]:  # 패턴을 반복해 돌면서 채점
                result[j] += 1  # 한 문제 맞음
    maxN = max(result)
    return [i for i, r in enumerate(result, start=1) if r == maxN]

    # 쌤 풀이
    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0, 0, 0]

    for a, b in enumerate(answers):
        for i, v in enumerate(p):  # 학생 순서대로 채점
            if b == v[a % len(v)]:
                s[i] += 1

    box = []
    for i, v in enumerate(s):
        if v == max(s):
            box.append(i + 1)


print(solution([1, 2, 3, 4, 5]))
