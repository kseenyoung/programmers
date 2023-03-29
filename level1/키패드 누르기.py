def solution(numbers, hand):
    left = 10
    right = 11
    result = ''
    direction = {0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1],
                 2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4],
                 5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3],
                 8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2]}

    for n in numbers:
        if n in [1, 4, 7]:
            result += 'L'
            left = n
        elif n in [3, 6, 9]:
            result += 'R'
            right = n
        elif n in [2, 5, 8, 0]:
            if direction[n][right] < direction[n][left]:
                result += 'R'
                right = n
            elif direction[n][right] == direction[n][left]:
                result += 'R' if hand == 'right' else 'L'
                if hand == 'right':
                    right = n
                else:
                    left = n
            else:
                result += 'L'
                left = n

    return result