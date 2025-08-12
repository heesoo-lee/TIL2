def dfs(idx, prob, visited):
    global max_prob

    if prob <= max_prob:
        return
    if idx == n:
        max_prob = prob
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, prob * (task[idx][i] / 100), visited)
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    task = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    max_prob = -1
    dfs(0, 1, visited)
    answer = max_prob * 100
    print(f'#{tc} {answer:.6f}')
