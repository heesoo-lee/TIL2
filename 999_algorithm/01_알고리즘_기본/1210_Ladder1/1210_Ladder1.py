def go(y, x, direction, visited):
    if y == 0:
        return x

    visited[y][x] = 1 # 방문 처리

    if direction == 'up': # 위로 가는 중인데
        if x < 99 and arr[y][x + 1] == 1 and not visited[y][x + 1]:
            # x < 99이고, 현재 위치의 오른쪽이 1이고 방문한 적 없으면
            return go(y, x + 1, 'right', visited) # 오른쪽으로 go
        elif x > 0 and arr[y][x - 1] == 1 and not visited[y][x - 1]:
            # 왼쪽 1이고 방문한 적 없으면
            return go(y, x - 1, 'left', visited) # 왼쪽으로 go
        else:
            return go(y - 1, x, 'up', visited) # 아니면 걍 위로

    elif direction == 'right':  # 오른쪽으로 가는 중
        if x < 99 and arr[y][x + 1] == 1 and not visited[y][x + 1]:
            return go(y, x + 1, 'right', visited)
        else:
            return go(y - 1, x, 'up', visited)

    elif direction == 'left':  # 왼쪽으로 가는 중
        if x > 0 and arr[y][x - 1] == 1 and not visited[y][x - 1]:
            return go(y, x - 1, 'left', visited)
        else:
            return go(y - 1, x, 'up', visited)


for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2: # 맨 아래 줄 탐색해서 2인 칸 찾음
            visited = [[0] * 100 for _ in range(100)] #visited 배열 생성
            answer = go(99, i, 'up', visited) #2인곳에서 시작

    print(f'#{t} {answer}')
