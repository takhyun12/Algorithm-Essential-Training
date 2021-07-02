def solution(s: list) -> list:
    result = []

    for i in s:
        temp = i.split(" ")
        result.append([int(temp[0]), temp[1]])

    result = sorted(result, key=lambda x: x[0])

    return result

if __name__ == '__main__':
    test_case1: list = ["21 Junkyu", "21 Dohyun", "20 Sunyoung"]
    print(solution(test_case1))
