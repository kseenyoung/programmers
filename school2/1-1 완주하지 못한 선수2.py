#방법 1
from collections import Counter
def solution(participants, complicator):
    pCounter = Counter(participants)
    cCounter = Counter(complicator)

    return list(pCounter - cCounter)[0]


#방법 2
def solution(participants, complicator):
    hash = {}
    for i in participants:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1

    for i in complicator:
        if i in hash:
            hash[i] -= 1

    for i in hash:
        if hash[i] != 0:
            return hash[i]