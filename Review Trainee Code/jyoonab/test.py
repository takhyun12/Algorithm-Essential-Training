def solution(index: int, text: str) -> str:
    # You can put your code in here
    return [str]


if __name__ == '__main__':
    cases = ["4, MISSPELL",
             "1, PROGRAMMING",
             "7, CONTEST",
             "3, BALLOON"]

    for case in cases:
        idx, txt = case.split(',')
        result: str = solution(int(inx), txt.lstrip())
        print(result)