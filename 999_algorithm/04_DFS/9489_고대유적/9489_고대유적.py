t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [] # 구조물의 길이들 담는 리스트

    # 가로 구조물 탐색
    for y in range(n):
        count = 0 # 카운트 초기화
        for x in range(m):
            if arr[y][x] == 1: # 값이 1일 경우 카운트 1 추가
                count += 1
            else:
                if count > 0: # 값이 0인데 카운트 0보다 클 경우 (=구조물이 끝난 경우)
                    result.append(count) # 구조물 길이 담기
                count = 0 # 카운트 초기화
        if count > 0: # 구조물이 한 행의 끝까지 있을 경우 대비
            result.append(count)

    # 세로 구조물 탐색
    for x in range(m):
        count = 0
        for y in range(n):
            if arr[y][x] == 1:
                count += 1
            else:
                if count > 0:
                    result.append(count)
                count = 0
        if count > 0:
            result.append(count)

    answer = max(result)
    print(f'#{tc} {answer}')
