def solution(n):
    if n % 6 == 0:  # 나누어 떨어졌을 때
        return n//6
    else:  # 나누어 떨어지지 않았을 때
        a = n//6 + 1  # 적어도 1판은 추가 될 것이다
        while a*6 % n != 0:  # 딱 떨어질 때까지 1판씩 추가
            a += 1
        return a