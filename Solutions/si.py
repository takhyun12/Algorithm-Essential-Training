import math
from collections import Counter


def solution(arr1: list, arr2: list) -> list:
    stack = list()
    for progress, speed in zip(arr1, arr2):
        time_required = math.ceil((100 - progress)/ speed)
        if len(stack) == 0:
            stack.append(time_required)
        elif stack[-1] > time_required:
            stack.append(stack[-1])
        else:
            stack.append(time_required)

    answer_list = list(Counter(stack).values())
    return answer_list


def solution2(arr1: list, arr2: list) -> list:
    task_list = list()
    for progress, speed in zip(arr1, arr2):
        time_required = math.ceil((100 - progress)/ speed)
        task_list.append(time_required)

    for i in range(len(task_list) - 1):
        if task_list[i] > task_list[i+1]:
            task_list[i+1] = task_list[i]

    answer_list = list()
    c1 = Counter(task_list)
    for key, value in c1.items():
        answer_list.append(value)

    return answer_list


if __name__ == '__main__':
    case1: list = [93, 30, 55]
    case2: list = [1, 30, 5]
    solution(case1, case2)

    case3: list = [95, 90, 99, 99, 80, 99]
    case4: list = [1, 1, 1, 1, 1, 1]
    solution(case3, case4)
