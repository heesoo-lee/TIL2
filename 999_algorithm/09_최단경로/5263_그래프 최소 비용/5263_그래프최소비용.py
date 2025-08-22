t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if arr[i][j] != 0:
                dist[i][j] = arr[i][j]

    for k in range(n):
        for i in range(n):
            if i == k: continue
            if dist[i][k] == float('inf'): continue

            for j in range(n):
                if j == k or j == i: continue
                if dist[k][j] == float('inf'): continue

                nd = dist[i][k] + dist[k][j]

                if nd < dist[i][j]:
                    dist[i][j] = nd

    answer = -float('inf')
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf') and i != j:
                answer = max(answer, dist[i][j])

    print(f'#{tc} {answer}')
