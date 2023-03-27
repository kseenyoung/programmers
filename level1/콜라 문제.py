def solution(a, b, n):
    result = 0
    while n >= a:
        plus = n // a
        result += (plus)*b  # 얻는 병 개수 유의 (*b)
        n %= a
        n += b*plus
        print(plus, n)
    return result