def dfs(index, result) :
    global min_answer
    global max_answer

    if sum(operators) == 0 :
        min_answer = min(min_answer, result)
        max_answer = max(max_answer, result)
        return

    for i in range(4) :
        if operators[i] > 0:
            operators[i] -= 1
            num = numbers[index]
            if i == 0 :
                dfs(index+1, result + num)
            elif i == 1 :
                dfs(index+1, result - num)
            elif i == 2 :
                dfs(index+1, result * num)
            elif i == 3 :
                dfs(index+1, int(result / num))
            operators[i] += 1


t = int(input())
for tc in range(1, t+1) :
        # 연산자 순서 : + - * /
    n = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_answer = 100000000
    max_answer = -100000000

    dfs(1, numbers[0])
    answer = max_answer - min_answer

    print(f'#{tc} {answer}')