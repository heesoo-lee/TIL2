t = int(input())

for test in range(1, t+1) :
    n, m = map(int, input().split())
    num = bin(m)[-n:]
    onoff = 'OFF'
    if num == '1' * n :
        onoff = 'ON'
    else : pass

    print(f"#{test} {onoff}")