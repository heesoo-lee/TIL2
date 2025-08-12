t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    # n: 한 변의 셀의 개수, m: 격리 시간, k: 미생물 군집 개수
    groups = [list(map(int, input().split())) for _ in range(k)]
    # 상: 1, 하: 2, 좌: 3, 우: 4
    answer = 0
    dx = [0, 0, 0, -1, 1]
    dy = [0, -1, 1, 0, 0]

    for _ in range(m): # 격리 시간 동안 돌음
        moved = dict() # 군집들 이동한 정보 저장할 딕셔너리
        for i in range(len(groups)):

            y, x, num, d = groups[i]
            if num == 0 : continue # 미생물 수 0(=사멸)인 군집은 무시 (최종 답에 영향 X)

            ny = y + dy[d]
            nx = x + dx[d] # 이동할 좌표 우선 변수에 저장

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                # 이동할 좌표가 빨간 벽에 부딪힐 경우
                num //= 2 # 미생물 수 반으로 줄음
                if num == 0: # 미생물가 0이 된 경우
                    groups[i][2] = 0 # 실제 군집에 미생물 수 적용
                    continue
                if d % 2 == 1: # 방향 숫자가 1, 3(상, 좌)일 경우
                    d += 1
                else: # 나머지(하, 우)일 경우
                    d -= 1

            groups[i] = [ny, nx, num, d] # 실제 군집에 적용

            if(ny, nx) not in moved: # 이동한 좌표에 아무도 없으면
                moved[(ny, nx)] = [[i, num, d]] # 딕셔너리에 추가
            else: # 누가 있으면
                moved[(ny, nx)].append([i, num, d]) # 그 좌표(키)에 이번 군집 정보 추가

        for position, infos in moved.items():
            if len(infos) > 1:
                infos.sort(key=lambda x: -x[1])
                # 미생물 수 합침
                total = sum(info[1] for info in infos)
                max_idx = infos[0][0]
                new_direction = infos[0][2]

                groups[max_idx] = [position[0], position[1], total, new_direction]

                for i in range(1, len(infos)):
                        groups[infos[i][0]][2] = 0

    for group in groups:
        answer += group[2]

    print(f'#{tc} {answer}')

