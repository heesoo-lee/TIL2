import copy


r, c, t = map(int, input().split()) # 행, 열, 시간
room = [list(map(int, input().split())) for _ in range(r)]
cleaner = []

# 공기청정기 위치 찾기
for i in range(r):
    if room[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i+1)
        break
time = 0
while time < t:
    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                if i - 1 >= 0:
                    room[i-1][j] += room[i][j] // 5
                    room[i][j] -= room[i][j] // 5
                if i + 1 < r:
                    room[i + 1][j] += room[i][j] // 5
                    room[i][j] -= room[i][j] // 5
                if j - 1 >= 0:
                    room[i][j - 1] += room[i][j] // 5
                    room[i][j] -= room[i][j] // 5
                if j + 1 < c:
                    room[i][j + 1] += room[i][j] // 5
                    room[i][j] -= room[i][j] // 5

    # 바람 순환 (위, 반시계)
    sub_room = copy.deepcopy(room)
    sub_room[cleaner[0]][1] = 0
    sub_room[cleaner[0]][2 : c] = room[cleaner[0]][1 : c-1]
    sub_room[0][0 : c-1] = room[0][1 : c]
    for i in range(cleaner[0] - 1):
        sub_room[i + 1][0] = room[i][0]
    for i in range(cleaner[0]):
        sub_room[i][c-1] = room[i+1][c-1]

    # 바람 순환 (아래 , 시계)
    sub_room[cleaner[1]][1] = 0
    sub_room[cleaner[1]][2: c] = room[cleaner[0]][1: c - 1]
    sub_room[r-1][0: c - 1] = room[r-1][1: c]
    for i in range(cleaner[0] + 1, r):
        sub_room[i - 1][0] = room[i][0]
    for i in range(cleaner[0], r):
        sub_room[i][c-1] = room[i - 1][c-1]
    time += 1
    room = copy.deepcopy(sub_room)

answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
           answer += room[i][j]

print(answer)

