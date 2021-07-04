import math

def solution(p: list, s: list) -> list:
    pre_process = []
    stack = []
    result = []

    #전처리
    for i in range(len(p)):
        pre_process.append(math.ceil((100-p[i])/s[i]))

    #후처리
    for i in pre_process:
        if len(stack) != 0:
            if stack[0] < i:
                result.append(len(stack))
                stack = []

        stack.append(i)

    result.append(len(stack))

    return result


if __name__ == '__main__':
    Progresses: list = [[93, 30, 55], [95, 90, 99, 99, 80, 99], [50, 60, 50]]
    Speeds: list = [[1, 30, 5], [1, 1, 1, 1, 1, 1], [10, 8, 10]]

    print(solution(Progresses[0], Speeds[0]))
    print(solution(Progresses[1], Speeds[1]))
    print(solution(Progresses[2], Speeds[2]))
