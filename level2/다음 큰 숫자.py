def solution(n):
    cnt1 = str(bin(n)[2:]).count("1")

    for answer in range(n + 1, 1000001):
        if cnt1 == str(bin(answer)[2:]).count("1"):
            return answer