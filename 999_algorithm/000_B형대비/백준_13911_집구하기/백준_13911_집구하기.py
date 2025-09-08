V, E = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(E)]
INF = float('inf')
graph = [[INF] * (V + 1) for _ in range(V + 1)]
for info in infos:
    s, e, d = info
    graph[s][e] = d
    graph[e][s] = d