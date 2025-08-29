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
    v, e = map(int, input().split()) # 마지막 노드 번호, 간선 개수
    edges = []

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()
    parent = [i for i in range(v + 1)]
    rank = [0] * (v + 1)
    total = 0
    picked = 0

    for w, n1, n2 in edges:
        if union(n1, n2):
            total += w
            picked += 1
            if picked == v:
                break

    print(f'#{tc} {total}')
