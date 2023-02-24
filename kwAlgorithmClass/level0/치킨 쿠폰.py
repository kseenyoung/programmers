def solution(chicken):
    cupon = chicken
    answer = 0
    while cupon > 9:
        temp = cupon // 10  # 서비스 치킨
        print(temp)
        answer += temp
        cupon %= 10  # 쿠폰으로 치킨 시킴 나머지 주의!!
        cupon += temp

    return answer