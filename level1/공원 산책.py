def solution(park, routes):
    board = []
    w, h = len(park[0]), len(park)
    idrl = {'E': 1, 'S': 0, 'W': -1, 'N': 0}
    idud = {'E': 0, 'S': 1, 'W': 0, 'N': -1}
    x, y = 0, 0  # 위치
    # 공원
    for i, line in enumerate(park):
        temp = []
        for j, p in enumerate(line):
            if p == 'S':
                x, y = j, i
                temp.append(1)
            else:
                temp.append(0 if p == 'X' else 1)
        board.append(temp)

    for route in routes:
        direction, count = route.split()
        for i in range(1, int(count)+1):  # 움직이는 동안 문제 없는지 확인
            x += idrl[direction]
            y += idud[direction]
            if x > w-1 or x < 0 or y > h-1 or y < 0:  # 문제 발생
                x -= idrl[direction]*i
                y -= idud[direction]*i
                break
            elif board[y][x] == 0:
                x -= idrl[direction]*i
                y -= idud[direction]*i
                break

    return [y, x]

print(solution(["SOO","OOO","OOO"],	["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],	["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],	["E 2","S 3","W 1"]))

