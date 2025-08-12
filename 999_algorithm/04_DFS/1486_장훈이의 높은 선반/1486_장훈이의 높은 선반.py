def dfs(idx, sum_heights):
    global min_sum
    if sum_heights >= b:
        min_sum = min(sum_heights, min_sum)
        return

    elif idx == n :
        return

    dfs(idx + 1, sum_heights + heights[idx])
    dfs(idx + 1, sum_heights)

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))

    selected = [0] * n
    min_sum = float('inf')
    dfs(0, 0)
    print(f'#{tc} {min_sum - b}')