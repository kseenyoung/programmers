# 내풀이(100%)
def solution(wallpaper):
    board = []
    maxNum = max(len(wallpaper), len(wallpaper[0]))
    minPoint, maxPoint = [maxNum, maxNum], [0, 0]
    for i, wall in enumerate(wallpaper):
        for j, w in enumerate(wall):
            if w == "#":
                if i < minPoint[0]:
                    minPoint[0] = i
                if i >= maxPoint[0]:
                    maxPoint[0] = i+1
                if j < minPoint[1]:
                    minPoint[1] = j
                if j >= maxPoint[1]:
                    maxPoint[1] = j+1

    return [minPoint[0], minPoint[1], maxPoint[0], maxPoint[1]]

# 풀이 참고
def solution(wallpaper):
    a, b = [], []
    wall = len(wallpaper[0])
    for i in range(len(wallpaper)):
        for j in range(wall):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a)+1, max(b)+1]

print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))


