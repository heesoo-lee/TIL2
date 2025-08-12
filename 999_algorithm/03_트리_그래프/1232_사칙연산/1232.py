for t in range(1, 11) :
    n = int(input())
    input_data = [list(input().split()) for _ in range(n)]

    tree = [0] * (n+1)

    for data in input_data :
        index = int(data[0])
        value = data[1]
        tree[index] = value

    for i in range(n, 0, -1) :
        if len(input_data[i-1]) == 4 :
            left_idx = int(input_data[i-1][2])
            right_idx = int(input_data[i-1][3])
            if tree[i] == '+':
                tree[i] = int(tree[left_idx]) + int(tree[right_idx])
            elif tree[i] == '-':
                tree[i] = int(tree[left_idx]) - int(tree[right_idx])
            elif tree[i] == '*':
                tree[i] = int(tree[left_idx]) * int(tree[right_idx])
            elif tree[i] == '/':
                tree[i] = int(tree[left_idx]) // int(tree[right_idx])

    print(f"#{t} {tree[1]}")
