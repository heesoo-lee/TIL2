from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs() :
    queue = deque([(1, 1)])
    visited = [[0] * 100 for _ in range(100)]
    visited[1][1] = -1

    while queue :
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[ny][nx] == 3 :
                    return 1
                if arr[ny][nx] != 1 and visited[ny][nx] != -1:
                    visited[ny][nx] = -1
                    queue.append((nx, ny))

    return 0

for _ in range(10) :
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    answer = bfs()
    print(f'#{tc} {answer}')

