from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(n, arr) :
    queue = deque([(0, 0, 0)])
    visited = [[float('inf')] * n for _ in range(n)]
    visited[0][0] = 0

    while queue :
        x, y, time = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n :
                # new_time = time + arr[ny][nx]
                if time + arr[ny][nx] < visited[ny][nx]:
                    visited[ny][nx] = time + arr[ny][nx]
                    queue.append((nx, ny, time + arr[ny][nx]))

    return visited[n-1][n-1]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    answer = bfs(n, arr)
    print(f'#{tc} {answer}')

