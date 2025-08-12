import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(row, col):
    # 너비 우선 탐색 -> queue
    #queue = deque([(0, 0)])
    queue = deque()
    queue.append((0, 0))

    while queue:
        row, col = queue.popleft()
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 리스트 범위 벗어나면 안됨
            # 이전에 방문한 적 없어야 함
            # 위치가 길 이어야 함 (1 = 길, 0 = 벽)
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and data[nx][ny] :
                queue.append((nx, ny))
                distance[nx][ny] = distance[row][col] + 1
                if nx == n-1 and ny == m-1 : # 도착지면
                    return
    return -1 # 모든 후보군 탐색했지만 함수 종료된 적 없다면, 도착할 수 없다는 의미

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

# 방문 표시 기록 -> 우리의 최종 목적 = 해당 위치까지 도달하는데 걸린 비용
distance = [[-1] * m for _ in range(n)]

get_road_move_time(0, 0)