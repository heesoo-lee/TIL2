t = int(input())
for tc in range(1, t+1):
    n = int(input())

    def count_tile(idx):
        if idx == 1:
            return 1
        if idx == 2:
            return 3
        if idx == 3:
            return 6
        else:
            return count_tile(idx - 3) + 2 * count_tile(idx - 2) + count_tile(idx - 1)

    answer = count_tile(n)
    print(f'#{tc} {answer}')



