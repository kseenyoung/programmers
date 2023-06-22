def solution(s):
    answer = [0, 0]

    def binary_trans(x):
        answer = ""
        while x > 0:
            answer += str(x % 2)
            x //= 2
        return answer

    while s != "1":
        temp = s.count("0")
        answer[1] += temp
        s = binary_trans(len(s) - temp)
        answer[0] += 1

    return answer