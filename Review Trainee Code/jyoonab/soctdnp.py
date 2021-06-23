def solution(s: str) -> int:
    alphabet_str: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result: int = 0

    for i in alphabet_str:
        if not i in s:
            result += ord(i)

    return result


if __name__ == '__main__':
    cases = ["ABCDEFGHIJKLMNOPQRSTUVW", "A", "BDCW", "K", "", 554342389243782437823478243872348234,
    "CCBBAA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefg"]
    for case in cases:
        result: int = solution(str(case))
        print(result)
