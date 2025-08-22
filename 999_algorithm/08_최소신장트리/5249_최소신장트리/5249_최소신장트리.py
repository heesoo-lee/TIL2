def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False

    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)

    total = 0
    picked = 0

    for w, u, v in edges:
        if union(u, v):
            total += w
            picked += 1
            if picked == V:
                break

    print(f'#{tc} {total}')
