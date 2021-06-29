def solution(input_list: list) -> str:
    numbers = list(map(str, input_list))

    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(numbers)))


import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0


def solution2(numbers):
    n = list(map(str, numbers))
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


if __name__ == '__main__':
    test_case1: list = [6, 10, 2]
    test_case2: list = [3, 30, 34, 5, 9]
    print(solution2(test_case2))
