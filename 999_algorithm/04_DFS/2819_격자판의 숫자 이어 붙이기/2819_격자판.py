def dfs(x, y, count) :
    num.append(str(arr[y][x]))
    if count == 6:
        numbers.add(''.join(num))
        num.pop()
        return
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, count + 1)

    num.pop()

t = int(input())
for tc in range(1, t+1) :
    arr = [list(map(int, input().split())) for _ in range(4)]
    numbers = set()
    num = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0)
    print(f'#{tc} {len(numbers)}')