def solution(s: str) -> int:
    # Exception Handle
    if len(s) >= 1000000 or len(s) <= 1:
        return -1

    # Main
    stack = list()
    for index, value in enumerate(s):
        if len(stack) == 0:
            stack.append(value)
        elif value == stack[-1]:
            stack.pop()
        else:
            stack.append(value)

    if len(stack) == 0:
        return 1
    else:
        return 0


def solution2(s: str) -> int:
    stack = list()
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    test_case1: list = ["baabaa", "cdcd", 'bbaabbddccbabb', 'ba']
    for case in test_case1:
        print(solution(case))
        print(solution2(case))