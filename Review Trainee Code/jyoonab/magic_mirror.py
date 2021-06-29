def solution(l: list, n: int) -> str:
    result = []

    if n == 1:
        result = l
    elif n == 2:
        for i in l:
            result.append(i[::-1])
    elif n == 3:
        result = l[::-1]
    return result

if __name__ == '__main__':
    mirror_data: list = ["OOOOOOOO", "OKKOOEEO", "OKKOOEEO", "OOOSSOOO", "OOOSSOOO", "OAOOOOAO", "OOAAAAOO", "OOOOOOOO"]
    level: int = 3

    print(solution(mirror_data, level))
