from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def fire(arr):
    global w, h
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                for d in range(4):
                    nx, ny = j + dx[d], i + dy[d]
                    if 0 <= nx < w and 0 <= ny < h and arr[ny][nx] != '#' and arr[ny][nx] != '*':
                        arr[ny][nx] = '*'
    return arr

def move(arr, time, x, y):
    global answer
    global escape
    if arr[y][x] == '@':
        answer = 'IMPOSSIBLE'
        return

    if y == 0 or y == h - 1 or x == 0 or x == w - 1:
        escape = True
        answer = time
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if visited[ny][nx]:
            continue
        if 0 <= nx < w and 0 <= ny < h and arr[ny][nx] == '.':
            arr[y][x] = '.'
            arr[ny][nx] = '@'
            visited[ny][nx] = True
            queue.append((nx, ny, time + 1))

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = list(input() for _ in range(h))
    queue = deque()
    visited = [[0] * w for _ in range(h)]
    x, y, time = 0, 0, 0
    found = False
    escape = False
    answer = 0

    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                x, y = j, i
                found = True
                break
        if found:
            break

    queue.append((x, y, time))

    while not escape:
        x, y, time = queue.popleft()
        new_building = fire(building)
        move(new_building, time, x, y)

    print(answer)