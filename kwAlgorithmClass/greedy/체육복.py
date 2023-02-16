def solution(n, lost, reserve):
    # 그리디 : 여벌이 있는 학생이 자기 앞, 뒤 학생 확인
    answer = 0
    student = [1] * (n + 2)

    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -= 1

    for i, s in enumerate(student):
        if s == 2:
            if student[i - 1] == 0:
                student[i - 1:i + 1] = [1, 1]
            elif student[i + 1] == 0:
                student[i:i + 2] = [1, 1]
    return n - student.count(0)