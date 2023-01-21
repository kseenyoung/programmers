def solution(number, k):
    collection = []
    for i, n in enumerate(number):
        while len(collection) > 0 and k > 0 and collection[-1] < n:
            collection.pop()
            k -= 1
        if k == 0:
            collection += number[i:]
            break
        collection.append(n)

    collection = collection[:-k] if k > 0 else collection
    return ''.join(collection)