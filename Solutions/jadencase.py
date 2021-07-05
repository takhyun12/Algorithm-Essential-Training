def solution(s: str) -> str:
    return ' '.join([word.capitalize() for word in s.split(" ")])


def solution2(s: str) -> str:
    s_split = s.split(" ")
    for index in range(len(s_split)):
        s_split[index] = s_split[index].capitalize()

    return ' '.join(s_split)


if __name__ == '__main__':
    cases = ['3people unFollowed me', 'for the last week', 'a   bcd  hello']
    print(solution2(cases[0]))
