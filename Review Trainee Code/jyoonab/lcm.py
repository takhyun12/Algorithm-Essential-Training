def solution(s: list) -> int:
    sorted_list = sorted(s)

    result = lcm(sorted_list[0], sorted_list[1])
    sorted_list = sorted_list[2:]

    for i in sorted_list:
        if result/i != 0:
            result = lcm(result, i)

    return result

def gcd(a: int, b: int) -> int:
    if a < b:
        (a, b) = (b, a)

    while b != 0:
        (a, b) = (b, a % b)

    return a

def lcm(a: int, b: int) -> int:
    return int((a*b) / gcd(a,b))


if __name__ == '__main__':
    test_case1: list = [2,6,8,14]
    test_case2: list = [1,2,3]

    print(solution(test_case1))
    print(solution(test_case2))
