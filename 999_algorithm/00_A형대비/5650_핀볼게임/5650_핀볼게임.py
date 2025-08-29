def game():
    global max_score

    worm = {k: [] for k in range(6, 11)}
    for i in range(n):
        for j in range(n):
            v = board[i][j]
            if 6 <= v <= 10:
                worm[v].append((j, i))

    def warp(x, y):
        w = board[y][x]
        a, b = worm[w]
        return (b if (x, y) == a else a)

    for sy in range(n):
        for sx in range(n):
            if board[sy][sx] != 0: continue
            for sd in range(4):
                x, y, d = sx, sy, sd
                score = 0
                while True:
                    nx, ny = x + dx[d], y + dy[d]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        score += 1
                        if d % 2 == 0:
                            d += 1
                        else : d -= 1
                        continue

                    cell = board[ny][nx]

                    if cell == -1:
                        break

                    if nx == sx and ny == sy:
                        break

                    # 블럭
                    if cell == 5:
                        nx, ny = x, y
                        score += 1
                        if d % 2 == 0:
                            d += 1
                        else : d -= 1
                        continue
                    elif cell == 1:
                        nx, ny = x, y
                        score += 1
                        if d == 0 : d = 1
                        elif d == 1: d = 3
                        elif d == 2: d = 0
                        else : d = 2
                        continue
                    elif cell == 2:
                        nx, ny = x, y
                        score += 1
                        if d == 0 : d = 1
                        elif d == 1: d = 2
                        elif d == 2: d = 3
                        else : d = 0
                        continue
                    elif cell == 3:
                        nx, ny = x, y
                        score += 1
                        if d == 0 : d = 2
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        else : d = 1
                        continue
                    elif cell == 4:
                        nx, ny = x, y
                        score += 1
                        if d == 0 : d = 3
                        elif d == 1: d = 0
                        elif d == 2: d = 1
                        else : d = 2
                        continue

                    #웜홀
                    if 6 <= cell <= 10:
                        nx, ny = warp(nx, ny)

                    x, y = nx, ny

                max_score = max(max_score, score)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1 ,0, 0] # 동서남북
    dy = [0, 0, 1, -1]
    max_score = 0
    game()
    print(max_score)