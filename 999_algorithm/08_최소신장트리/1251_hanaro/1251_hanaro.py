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
    n = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    tax = float(input())
    info = []

    for i in range(n):
        for j in range(n):
            d = (island_x[i] - island_x[j])**2 + (island_y[i] - island_y[j])**2
            info.append((d, i, j))

    info.sort()
    parent = [i for i in range(n)]
    rank = [0] * n

    total = 0
    picked = 0

    for w, u, v in info:
        if union(u, v):
            total += w
            picked += 1
            if picked == n-1:
                break

    answer = round(tax * total, 0)

    print(f'#{tc} {int(answer)}')
