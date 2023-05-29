def solution(n, costs):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a, b = find(a), find(b)
        minP, maxP = min(a, b), max(a, b)
        parent[maxP] = minP

    parent = [i for i in range(n)]
    result = 0

    costs.sort(key=lambda x: x[2])

    for a, b, w in costs:
        if find(a) != find(b):
            union(a, b)
            result += w
    return result