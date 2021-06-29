from math import gcd


def solution(arr: list) -> int:
    lcm: int = 0
    for i in range(len(arr) - 1):
        if i == 0:
            head = arr[i]
        else:
            head = lcm
        tail = arr[i + 1]
        lcm = head * tail // gcd(head, tail)

    return lcm


if __name__ == '__main__':
    test_case1: list = [2, 6, 8, 14]
    test_case2: list = [1, 2, 3]
    print(solution(test_case1))
