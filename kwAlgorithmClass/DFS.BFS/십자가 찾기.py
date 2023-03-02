import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
board = []

for _ in range(N):  # 입력을 board에 저장
    line = list(input())
    board.append(line)

tempBoard = copy.deepcopy(board)  # '*' -> '.' 처리할 공간, 단순 copy시 주소값으로 저장함
for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == '*':  # 십자의 중심이 될 수도 있는 위치
            up = down = i
            left = right = j
            size = 0
            while True:  # 십자 모양일 때까지 반복
                up -= 1
                down += 1
                left -= 1
                right += 1
                if up >= 0 and down < N and left >= 0 and right < M and board[up][j] == '*' and board[down][j] == '*' and \
                        board[i][left] == '*' and board[i][right] == '*':
                    size += 1
                    tempBoard[up][j] = tempBoard[down][j] = tempBoard[i][left] = tempBoard[i][right] = '.'
                    result.append((i + 1, j + 1, size))
                else:  # 더이상 십자 모양이 아닐 때
                    if size > 0:  # 십자 모양이 하나 있었을 때 중심을 '.'로 변경
                        tempBoard[i][j] = '.'
                    break

temp = True  # 십자모양으로 지워지지 않은 '*'가 있는지 확인할 변수
for t in tempBoard:
    if '*' in t:
        temp = False
        print(-1)
        break
if temp:  # 십자모양으로 모든 '*'을 지운 경우
    print(len(result))
    result.sort(key=lambda x: (x[0], x[1], -x[2]))
    for r in result:
        print(r[0], r[1], r[2])