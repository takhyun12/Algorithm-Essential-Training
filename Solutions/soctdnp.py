def solution(s: str) -> int:
    zero_ascii_list = list()
    for ascii_code in range(ord('A'), ord('Z') + 1):
        if s.count(chr(ascii_code)) == 0:
            zero_ascii_list.append(ascii_code)

    return sum(zero_ascii_list)


if __name__ == '__main__':
    cases = ["ABCDEFGHIJKLMNOPQRSTUVW", "A", "DUDHCBQWUUWQWGBDBQHBDHDBBDDBD", "BDCW", "K", "", 554342389243782437823478243872348234]
    for case in cases:
        result: int = solution(str(case))
        print(result)