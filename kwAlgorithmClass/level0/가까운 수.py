def solution(array, n):
    array.sort()  # ***정렬
    answer = 0
    minN = 101

    for a in array:
        if abs(a - n) < minN:
            minN = abs(a-n)  # answer 아닌 최소값 비교
            answer = a

    return answer


solution([3, 10, 28], 20)