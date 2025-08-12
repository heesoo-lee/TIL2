def dfs(count):
    if count == n:
        global answer
        answer = max(answer, int("".join(map(str, numbers))))
        return

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            num = int("".join(map(str, numbers)))
            if (num, count + 1) not in visited:
                visited.add((num, count + 1))
                dfs(count + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


t = int(input())
for tc in range(1, t + 1):
    numbers, n = map(str, input().split())
    n = int(n)
    numbers = list(map(int, numbers))

    visited = set()
    answer = 0

    dfs(0)

    print(f'#{tc} {answer}')
