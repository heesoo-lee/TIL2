t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    # n: 한 변의 셀의 개수, m: 격리 시간, k: 미생물 군집 개수
    groups = [list(map(int, input().split())) for _ in range(k)]
    # 상: 1, 하: 2, 좌: 3, 우: 4
    answer = 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    moved = dict()

    for _ in range(m):
        for i in range(k):
            if groups[i] == [-1, -1, -1, -1]: continue

            y, x, num, direction = groups[i][0], groups[i][1], groups[i][2], groups[i][3]
            nx = x + dx[direction - 1]
            ny = y + dy[direction - 1]

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                if num == 1:
                    groups[i] = [-1, -1, -1, -1]
                else:
                    num = num // 2
                    if direction % 2 == 1:
                        direction += 1
                    else:
                        direction -= 1

            if (ny , nx) not in moved:
                moved[(ny, nx)] = [[num, d]]
            else :
                moved[(ny, nx)].append([num, d])

            for j in range(k):
                if j != i and groups[j][0] == ny and groups[j][1] == nx:
                    conflict.append([i, groups[j][2], groups[j][3]])

            groups[i] = [ny, nx, num, direction]

        max_num = 0
        new_num = 0
        if len(conflict) > 1:
            for l in range(k):
                for c in conflict:
                    if c[0] == l:
                        new_num += c[1]
                        if c[1] > max_num:
                            c[1] = max_num
                            new_direction = c[2]
                        groups[l][1] = new_num
                        groups[l][2] = new_direction
                for p in range(k):
                    if l != p and groups[l][0] == groups[p][0] and groups[l][1] == groups[p][1]:
                        groups[p] = [-1, -1, -1, -1]

    for group in groups:
        if group != [-1, -1, -1, -1]:
            answer += group[2]

    print(f'#{tc} {answer}')
