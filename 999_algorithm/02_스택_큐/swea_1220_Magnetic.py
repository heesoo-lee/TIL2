for test in range(1, 11) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    ready = False
    for i in range (100) :
        ready = False
        for j in range(100) :
            if arr[j][i] == 1 :
                ready = True
            if arr[j][i] == 2 and ready :
                count += 1
                ready = False


    print( f'#{test} {count}')