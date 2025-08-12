import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col, acc) :
    global min_count

    if acc >= min_count:
        return

    if row == N-1 and col == M-1:
        min_count = min(min_count, acc)
        return

    for k in range(4):
        nx, ny = row + dx[k], col + dy[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if visited[nx][ny]: continue
        if not road[nx][ny]: continue

        visited[nx][ny] = 1
        dfs(nx, ny, acc + 1)
        visited[nx][ny] = 0


# 입력 처리
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 배열 및 최소 이동 횟수 초기화
visited = [[False] * M for _ in range(N)]
min_count = float('inf')

# 시작점 방문처리 후 탐색 시작
visited[0][0] = True
dfs(0, 0, 0)

print(min_count)  # 결과 출력
