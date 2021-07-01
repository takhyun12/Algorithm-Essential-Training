# 재귀를 통한 방법
def solution(arr: list, target_number: int) -> int:
    if not arr:
        if target_number == 0:
            return 1
        else:
            return 0
    else:
        return solution(arr[1:], target_number+arr[0]) + solution(arr[1:], target_number-arr[0])


from itertools import product


# 경우의 수를 통한 방법
def solution2(arr: list, target_number: int) -> int:
    cases = [(x, -x) for x in arr]
    sum_cnt = list(map(sum, product(*cases)))
    return sum_cnt.count(target_number)


if __name__ == '__main__':
    numbers: list = [1, 1, 1, 1, 1]
    target: int = 3
    print(solution(numbers, target))
    print(solution2(numbers, target))
