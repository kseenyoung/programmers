def solution(board, moves):
    basket = [[] for _ in range(len(board))]
    result = []
    for b in reversed(board):
        for i, a in enumerate(b):
            if a != 0:
                basket[i].append(a)
    count = 0
    for m in moves:
        if basket[m - 1]:
            toy = basket[m - 1].pop()
            if result and result[-1] == toy:
                count += 2
                result.pop()
            else:
                result.append(toy)

    return count