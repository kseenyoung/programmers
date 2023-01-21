#내 풀이
booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"], ["09:05", "bae"]]
#
# visitor = booked + unbooked
# visitor.sort(key=lambda x: x[0])
#
# late = []
# fin = []
# current = visitor[0][0]
#
# for t, v in visitor:
#     if t < current:
#         late.append([t, v])
#     current += 10
#     print(current)

def timeFu(t):
    h, m = map(int, t.split(':'))
    return h*60 + m


#풀이
def solution(booked, unbooked):
    booked = [(timeFu(t), name) for t, name in booked]
    unbooked = [(timeFu(t), name) for t, name in unbooked]
    booked.sort()
    unbooked.sort()
    b, u, t, answer = 0, 0, 0, []

    while b < len(booked) and u < len(unbooked):

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

    return answer


print(solution(booked, unbooked))