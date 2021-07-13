def solution(n: int) -> bool:
    result = 0
    str_n = str(n)

    for i in range(len(str_n)):
        if i % 2 == 0: # if even
            temp = int(str_n[i]) * 2
            if temp > 9:
                temp = int(str(temp)[0]) + int(str(temp)[1])
            result += temp
        else: # if odd
            result += int(str_n[i])

    if result % 10 == 0:
        return True

    return False

if __name__ == '__main__':
    arr = [2720992711828767, 3444063910462763, 6011733895106094]
    print(solution(arr[0]))
    print(solution(arr[1]))
    print(solution(arr[2]))
