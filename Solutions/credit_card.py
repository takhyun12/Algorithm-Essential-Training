def solution(card_number: int) -> bool:
    card_number = list(str(card_number))
    for index, value in enumerate(card_number):
        if (index + 1) % 2 != 0:
            value = int(value) * 2
            if value >= 10:
                card_number[index] = int(str(value)[0]) + int(str(value)[1])
            else:
                card_number[index] = value

    card_number = [int(value) for value in card_number]
    if sum(card_number) % 10 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    arr = [2720992711828767, 3444063910462763, 6011733895106094]
    for a in arr:
        print(solution(a))

