def solution(array, commands):
    # 내 풀이(맞음)
    answer = [0]*len(commands)
    idx = 0
    for i, j, k in commands:
        temp = array[i-1: j]
        temp.sort()
        answer[idx] = temp[k-1]
        idx += 1

    return answer

    # 쌤 풀이
    answer = []
    for c in commands:
        temp = array[c[0]-1:c[1]]
        temp.sort()
        answer.append(temp[c[2]-1])
    return answer




print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))