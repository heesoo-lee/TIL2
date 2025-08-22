import heapq


t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split()) # 정점 수, 간선 수
    adj = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))

    dist = [float('inf')] * (n + 1)
    dist[0] = 0

    pq = [(0, 0)] # (거리, 정점)

    while pq:
        cur_d, u = heapq.heappop(pq)
        if cur_d > dist[u]:
            continue

        for v, w in adj[u]:
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    print(f'#{tc} {dist[n]}')

