from itertools import product

def solution(numbers: list, target: int) -> int:
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))

    return s.count(target)

if __name__ == '__main__':
    numbers: list = [1, 1, 1, 1, 1]
    target: int = 3
    print(solution(numbers, target))
