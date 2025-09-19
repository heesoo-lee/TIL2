from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = list(input() for _ in range(h))
    fire_q = deque()
    person_q = deque()
    visited = [[0] * w for _ in range(h)]
    fire_time = [[-1] * w for _ in range(h)]
    escape = False

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                person_q.append((j, i, 0))
                visited[i][j] = True
            elif building[i][j] == '*':
                fire_q.append((j, i, 0))
                fire_time[i][j] = 0

    while fire_q:
        x, y, time = fire_q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < w and 0 <= ny < h): continue
            if fire_time[ny][nx] == -1 and building[ny][nx] != '#':
                fire_time[ny][nx] = time + 1
                fire_q.append((nx, ny, time + 1))

    while person_q and not escape:
        x, y, time = person_q.popleft()
        if x == 0 or x == w - 1 or y == 0 or y == h - 1:
            answer = time + 1
            escape = True

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < w and 0 <= ny < h): continue
            if visited[ny][nx]: continue
            if -1 < fire_time[ny][nx] <= time + 1: continue
            if building[ny][nx] == '.':
                visited[ny][nx] = True
                person_q.append((nx, ny, time + 1))

    if not escape:
        answer = 'IMPOSSIBLE'

    print(answer)
