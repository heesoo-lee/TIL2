t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    sums = [0] * (n - k + 1)

    for i in range(n - k + 1):
        sums[i] = sum(nums[i : i + k])

    answer = - 100000 * n

    for i in range(n - k):
        for j in range(i - k):
            answer = max(answer, sums[i] + sums[i + k + j])

    print(f"#{tc} {answer}")