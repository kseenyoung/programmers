def transHourToMin(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def solution(booked, unbooked):
    booked = [(transHourToMin(b[0]), b[1]) for b in booked] + [(10000, None)]
    unbooked = [(transHourToMin(u[0]), u[1]) for u in unbooked] + [(10000, None)]

    b, u, t, answer = 0, 0, 0, []
    booked.sort()
    unbooked.sort()

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

    answer.pop()
    return answer


print(solution([["09:10", "lee"]], [["09:00", "kim"], ["09:05", "bae"]]))
