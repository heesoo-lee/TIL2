t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    info = list(map(int, input().split()))

    group = [i for i in range(n+1)]

    def find_set(x):
        if x != group[x]:
            group[x] = find_set(group[x])
        return group[x]

    def union(a, b):
        ra, rb = find_set(a), find_set(b)
        if ra != rb:
            group[rb] = ra

    for a, b in zip(info[0::2], info[1::2]):
        union(a, b)

    roots = {find_set(i) for i in range(1, n+1)}
    answer = len(roots)
    print(f'#{tc} {answer}')

