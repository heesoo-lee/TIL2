def bellman_ford(graph, start):  # 벨만-포드: 단일 시작점 최단거리 + 음수 사이클 감지
    n = len(graph) # 정점 개수
    distance = {v: float('inf') for v in graph} # 모든 정점 최단거리 초기화
    distance[start] = 0
    # distance = {'a': inf, 'b': inf, 'c': inf, 'd': inf, 'e': inf, 'f': inf}
    for _ in range(n - 1):
        updated = False
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] != float('inf') and distance[u] + weight < distance[v]: # 더 짧은 경로 발견하면
                    distance[v] = distance[u] + weight # 거리 갱신
                    updated = True  # 갱신 발생 표시
        if not updated:  # 더 이상 갱신이 없으면 조기 종료
            break
    for u in graph:  # 추가 1회 완화 시도 (음수 사이클 검사)
        for v, weight in graph[u].items():
            if distance[u] != float('inf') and distance[u] + weight < distance[v]: # 여전히 줄어든다?
                print('음수 사이클이 있습니다.')   # 음수 사이클 존재
                return False   # 실패 신호 반환
    return distance

graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': -3, 'd': 2, 'e': 3},  # b→c가 -3, c→b가 1 → b↔c 합 -2(음수 사이클)
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

start_vertex = 'a'
result = bellman_ford(graph, start_vertex)
print(f"'{start_vertex}': {result}")
