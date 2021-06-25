# Restrictions:
# Input : 입력될 문자열은 최대 1000글자이며, 반드시 대문자로 받아야 한다.
# Output : 입력된 문자열의 각 글자를 알파벳 다음 순서로 써서 출력한다. 알파벳 Z의 다음 순서는 A이다.

def solution(s: str) -> str:
    if 1 > len(s) or len(s) > 1000:
        raise Exception('정상적인 입력이 아닙니다.')

    result_list = list()
    for char in s.upper().replace(" ", ""):
        if char == "Z":
            result_list.append("A")
        else:
            result_list.append(chr(ord(char) + 1))

    return ''.join(result_list)


if __name__ == '__main__':
    test_cases = ['HAL', 'SWERC', 'Hal', 'H a L']
    for case in test_cases:
        print(f'Original : {case}, Result : {solution(case)}')

