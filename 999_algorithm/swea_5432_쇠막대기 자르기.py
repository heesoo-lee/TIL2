t = int(input())

for test in range(1, t+1) :
    pipe = str(input())
    count = 0
    answer = 0
    remember = []
    for i in range(len(pipe)-1) :
        if pipe[i] == '(' and pipe[i+1] == '(' :
            count += 1
        elif pipe[i] == '(' and pipe[i+1] == ')':
            answer += count
            if count not in remember :
                answer += count
            remember.append(count)
        elif pipe[i] == ')' and pipe[i+1] == ')' :
            count -=1

    print(f'#{test} {answer}')
