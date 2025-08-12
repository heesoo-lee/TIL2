def depth_first_search(vertex):
    # vertex : 현재 방문 정점의 index

    # global에 있는 visited를 방문할 때마다 해당 idx번째를 True로 바꾸고 싶음
    # 그럴려면? 함수는 기본적으로 LEGB 룰을 따르기 때문에...
    global visited # 없어도 되긴 함
    visited[vertex] = True


    # 정점 방문
    print(graph[vertex])

    # 현재 정점이 진출할 수 있을, 후보군들을 찾는다
    # 인접 행렬의 vertex번째 리스트를 순회한다
    for idx in range(N):
    # for candidate in adj_matrix[vertex]:
        # 그 진출 후보군 A~G 중에, 가능한 경우에 대해서만
        # 그 idx번째가 이전에 방문한 적이 없을 때만
        if adj_matrix[vertex][idx] and visited[idx] == False :
            depth_first_search(idx)


        # 0    1    2    3    4    5    6
graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# 정점 수: N
N = 7
# 해당 정점 방문 여부 표시 : False로 초기화
visited = [False] * N


# 인접 행렬
adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
]

depth_first_search(0)

