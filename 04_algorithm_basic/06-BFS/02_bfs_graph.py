from collections import deque

def bfs(start_vertex):
    '''

    인접 행렬로 순회 시 정점의 index
    인접 리스트로 순회 시 정점의 값
    '''

    visited = set()

    queue = deque([start_vertex])
    visited.add(start_vertex)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 모든 노드들에 대해서 인덱스 조사
        for next_index in range(len(nodes)):
            if next_index not in range(len(nodes)) and adj_matrix[node][next_index]:
                visited.add(next_index)
                queue.append(next_index)

        # 내 인접 리스트에서 인접 정점 찾아서 순회
        # for neighbor in adj_list.get(node, []):
        #     if neighbor not in visited:
        #         visited.add(neighbor)
        #         queue.append(neighbor)

    return result



# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 4',
    '3 5',
    '4 5',
    '5 6'
]

# 인접 리스트 형태
'''
adj_list = {
    'A': ['B', 'C'],
    ...
    'G': ['F']
}
'''
adj_list = {node: [] for node in nodes}

# 간선 정보와 정점의 index 정보로 adj_list 채워주기
for edge in edges:
    u, v = edge.split()
    adj_list[nodes[int(u)]].append(nodes[int(v)])
    adj_list[nodes[int(v)]].append(nodes[int(u)])

# 인접 행렬
adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
for edge in edges:
    u, v = edge.split()
    u_index, v_index = int(u), int(v)
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1