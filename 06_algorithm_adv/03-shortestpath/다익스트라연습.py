import heapq, math # 우선순위 큐, 무한대 사용

def dijkstra(graph, start):
    distance = {v: math.inf for v in graph} # 각 정점까지의 최단거리 초기화
    distance[start] = 0 # 시작 정점의 거리 = 0
    heap = [] # (거리, 정점) 형태의 최소 힙
    heapq.heappush(heap, [0, start]) # 시작 정점을 힙에 넣기
    visited = set() # 최단거리가 확정된 정점 집합

    while heap:  # 힙이 빌 때까지 반복
        dist, current = heapq.heappop(heap) # 가장 가까운 정점 꺼내기
        if current in visited or distance[current] < dist: # 이미 확정이거나 더 긴 경로면 스킵
            continue
        visited.add(current) # 현재 정점의 최단거리 확정

        for nxt, weight in graph[current].items(): # 인접 정점들 순회
            next_distance = dist + weight # 현재까지 거리 + 간선 가중치
            if next_distance < distance[nxt]: # 더 짧은 경로 찾으면
                distance[nxt] = next_distance # 최단거리 갱신
                heapq.heappush(heap, [next_distance, nxt]) # 힙에 후보로 삽입

    return distance # 모든 정점에 대한 최단거리 반환'

graph = {
    'a': {'b': 3, 'c': 5},
    'b': {'c': 2},
    'c': {'b': 1, 'd': 4, 'e': 6},
    'd': {'e': 2, 'f': 3},
    'e': {'f': 6},
    'f': {}
}
start_v = 'a' # 시작 정점
res = dijkstra(graph, start_v) # 다익스트라 실행
print(res) # {'a': 0, 'b': 3, 'c': 5, 'd': 9, 'e': 11, 'f': 12}