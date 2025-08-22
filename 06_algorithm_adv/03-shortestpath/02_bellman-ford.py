def bellman_ford(graph, start):
    pass

# 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': 3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

# 음수 사이클 예시 그래프
# graph = {
#     'a': {'b': 4, 'c': 2},
#     'b': {'c': -3, 'd': 2, 'e': 3},
#     'c': {'b': 1, 'd': 4, 'e': 5},
#     'd': {'e': -3},
#     'e': {'f': 2},
#     'f': {}
# }

# 시작 정점 설정
start_vertex = 'a'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
