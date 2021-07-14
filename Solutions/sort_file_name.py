# Using Algorithm
def solution(file_list: list) -> list:
    new_file_list = list()
    for file in file_list:
        # head
        head = ''
        for char in file:
            if char.isdigit():
                break
            head += char

        # number
        number = ''
        for char in file[len(head):]:
            if not char.isdigit():
                break
            number += char

        # tail
        tail = file[len(head) + len(number):]

        # save (head / number / tail / origin)
        new_file_list.append([str(head).lower(), int(number), str(tail).lower(), file])

    new_file_list.sort(key=lambda x: (x[0], x[1]))
    return [file[3] for file in new_file_list]


# ---------------------------------------------------------------------------------------------------

import re


# Using Regex
def solution2(file_list: list) -> list:
    a = sorted(file_list, key=lambda file: int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file: re.split('\d+', file.lower())[0])
    return b

# ---------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    case1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(case1))
    print(solution2(case1))
