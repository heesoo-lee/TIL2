for _ in range(10) :
    t = int(input())
    numbers = list(map(int, input().split()))
    minus = 1

    while True :
        num = numbers.pop(0)
        num -= minus
        if num <= 0 :
            num = 0
            numbers.append(num)
            break
        numbers.append(num)
        minus += 1
        if minus >= 6 :
            minus = 1
    out = ' '.join(map(str, numbers))
    print(f'#{t} {out}')
    # print(f'#{t}', end=' ')