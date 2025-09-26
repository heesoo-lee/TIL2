from collections import deque

n, k = map(int, input().split())
answer = 0
q = deque()
visited = [0] * 100001
q.append((n, 0))
visited[n] = True

while q:
    x, time = q.popleft()

    if x == k:
        answer = time
        break

    for nx in (x - 1, x + 1, 2 * x):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            q.append((nx, time + 1))

print(answer)