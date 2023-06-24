from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    wordlen = len(begin)

    def diff1(w1, w2):
        cnt = 0
        for i in range(wordlen):
            if w1[i] != w2[i]:
                cnt += 1
        return True if cnt == 1 else False

    que = deque()
    que.append((begin, 0))
    while que:
        word, cnt = que.popleft()
        if word == target:
            return cnt
        for word2 in words:
            if diff1(word, word2):
                que.append((word2, cnt + 1))
    return 0
