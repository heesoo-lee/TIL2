from collections import deque

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')

dp = [[INF, INF, INF] for _ in range(n)]

queue = deque([(-1, -1, 0)]) #(인덱스, 색, 비용)

while queue:
    idx, color, cost = queue.popleft()

    if idx == n - 1: break

    for i in range(3):
        if color != i and dp[idx + 1][i]  > cost + info[idx + 1][i]:
            queue.append((idx + 1, i, cost + info[idx + 1][i]))
            dp[idx + 1][i] = cost + info[idx + 1][i]

answer = min(dp[n - 1])
print(answer)