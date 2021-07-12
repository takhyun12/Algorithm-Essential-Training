def solution(s: str) -> str:
    result = ""
    previous = ""

    for i in range(len(s)):
        if previous == " " or i == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
        previous = s[i]

    return result

if __name__ == '__main__':
    cases = ['3people unFollowed me', 'for the last week', ' 111 222 333 hi ']
    print(solution(cases[0]))
    print(solution(cases[1]))
    print(solution(cases[2]))
