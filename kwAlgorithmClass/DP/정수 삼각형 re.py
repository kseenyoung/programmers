def solution(triangle):
    result = []

    for i in range(1, len(triangle)):  # level
        for j, n in enumerate(triangle[i]):  # number
            if j == 0:  # 첫번째 원소
                triangle[i][0] += triangle[i-1][0]
            elif j == len(triangle[i])-1: # 마지막 원소
                triangle[i][j] += triangle[i-1][j-1]
            else:  # 중간 원소
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    print(triangle)
    return max(triangle[len(triangle)-1])



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
