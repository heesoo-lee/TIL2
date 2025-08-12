for t in range(1, 11) :
    n = int(input())
    info = [list(input().split()) for _ in range(n)]

    tree = [0] * (n+1)
    answer = []

    for row in info :
        index = int(row[0])
        value = row[1]
        tree[index] = value

    def traversal(idx) :
        if idx <= n :
            traversal(idx*2)
            answer.append(tree[idx])
            traversal(idx*2+1)
    traversal(1)
    print(f"#{t} {''.join(answer)}")