# 부모의 정보만 주어질 때, 이진 트리 생성하기
# 자신의 값, 부모 인덱스 (부모가 0인 경우, 루트)
input_data = [
    ['A', 0],
    ['C', 1],
    ['B', 1],
    ['F', 3],
    ['G', 6],
    ['E', 2],
    ['D', 2]
]

n = 16
tree = [0] * (n+1)

for data in input_data:
    value = data[0]
    parent = data[1]

    # 내가 루트일 경우 (부모 인덱스 = 0일 경우)
    if not parent:
        tree[1] = value
        continue

    left_child = parent * 2
    right_child = parent * 2 + 1
    # 주어진 정보가 부모 노드의 index이기 때문에 내 index 찾아야 함

    if not tree[left_child]:
        tree[left_child] = value
    else:
        tree[right_child] = value
print(tree)

