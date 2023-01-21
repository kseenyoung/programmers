def transTime(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def solution(booked, unbooked):
    booked = [(transTime(t), name) for t, name in booked] + [(1000000, None)] #더미 값을 넣지 않으면 제대로 동작x 왜??
    unbooked = [(transTime(t), name) for t, name in unbooked] + [(1000000, None)]
    booked.sort(key=lambda x: x[0])
    unbooked.sort(key=lambda x: x[0])

    t, b, u, answer = 0, 0, 0, []

    while b < len(booked) and u < len(unbooked): #False and True이면 while문이 끝나지 않나??

        t1, t2 = booked[b][0], unbooked[u][0]
        if t1 <= t:
            answer.append(booked[b][1])
            b += 1
            t += 10
        elif t2 <= t:
            answer.append(unbooked[u][1])
            u += 1
            t += 10
        else:
            t = min(t1, t2)
        answer.pop() #더미 제거 주의
    return answer


print(solution([["09:10", "lee"]], [["09:00", "kim"], ["09:05", "bae"]]))