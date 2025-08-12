t = int(input())
for test in range(1, t+1) :
    n, e, a, b = map(int, input().split())
    data = list(map(int, input().split()))

    relation = [[data[i], data[i+1]] for i in range(0, len(data), 2)]

    def find_parent(num) :
        parents = []
        for rel in relation :
            if rel[1] == num :