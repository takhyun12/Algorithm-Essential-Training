"""
Restrictions:
          1. len(s) / 2 의 Time complexity 구현하시오.
          2. 추가적인 변수를 할당하지 마시오.
"""


def solution(s: str) -> str:
    reversed_list = list(s)
    start, fin = 0, len(s) - 1
    while start < fin:
        reversed_list[start], reversed_list[fin] = reversed_list[fin], reversed_list[start]
        start += 1
        fin -= 1
    return ''.join(reversed_list)


def solution2(s: str) -> str:
    s_list = list(s)
    s_list.reverse()
    return ''.join(s_list)


def solution3(s: str) -> str:
    return s[::-1]


def solution4(s: str) -> str:
    return ''.join(reversed(s))


if __name__ == '__main__':
    test_case = "Feel so Good!" * 1000000
    print(solution(test_case))
    print(solution2(test_case))
    print(solution3(test_case))
    print(solution4(test_case))
