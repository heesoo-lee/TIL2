t = int(input())
for tc in range(1, t+1):
    n = int(input())
    command = [list(map(int, input().split())) for _ in range(n)]
    print(command)
