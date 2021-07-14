def solution(number: int) -> int:
    limit = 2 ** 31
    reverse_number = str(number)[::-1]

    if reverse_number[-1] == "-":
        reverse_number = "-" + reverse_number[0:len(reverse_number)-1]

    if int(reverse_number) > limit or int(reverse_number) < -limit:
        return 0
    else:
        return int(reverse_number)


if __name__ == '__main__':
    numbers = [900000, 123, -321]
    for num in numbers:
        print(solution(num))