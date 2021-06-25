def solution(s: str) -> str:
    result: str = ""
    print(s)
    for i in s:
        if ord(i) == 90:
            result += 'A'
        elif ord(i) == 122:
            result += 'a'
        else:
            result += chr(ord(i)+1)
    return result

if __name__ == '__main__':
    test_cases = ['HAL',
                  'SWERC',
                  'Hal',
                  'DNVNIQRWEHJKFBQWHADOQWDCMVJ' * 10000000]

    for case in test_cases:
        print(solution(case))
