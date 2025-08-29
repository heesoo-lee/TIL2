def floyd_warshall(graph): # 플로이드워셜: 모든 쌍 최단거리(APSP) 계산
    n = len(graph) # 정점(노드) 수
    for k_node in range(n): # 중간(경유) 정점 k를 하나씩 고려
        for start in range(n): # 출발 정점 i
            for end in range(n): # 도착 정점 j
                Dik = graph[start][k_node] # i->k 최단 거리
                Dkj = graph[k_node][end] # k->j 최단 거리
                Dij = graph[start][end] # i->j 최단 거리
                if Dik + Dkj < Dij: # k 경유가 더 짧아진다면
                    graph[start][end] = Dik + Dkj # 최단거리 갱신
    for i in range(n):
        if graph[i][i] < 0:
            print('음수 사이클 존재')
