t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    edges = []

    for i in range(n):
        for j in range(n):
            w = graph[i][j]
            if i != j and w != 0:
                edges.append((i, j, w))

    answer = -float('inf')

    for s in range(n):
        dist = [float('inf')] * n
        dist[s] = 0

        for _ in range(n-1):
            updated = False
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
