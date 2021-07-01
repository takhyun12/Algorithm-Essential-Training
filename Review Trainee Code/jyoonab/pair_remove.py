def solution(s: str) -> int:
    result = []

    if len(s) % 2 != 0:
        return 0

    for i in s:
        result.append(i)
        # if same char were inserted
        if len(result) >= 2 and result[-1:] == result[-2:-1]:
            result.pop()
            result.pop()

    if len(result) == 0:
        return 1

    return 0

if __name__ == '__main__':
    test_case1: list = ["baabaa", "cdcd"]
    for i in test_case1:
        print(solution(i))
