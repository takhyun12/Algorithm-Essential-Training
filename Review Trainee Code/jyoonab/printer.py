def solution(priorities: list, location: int) -> int:
    indexed_list = []
    result = 0

    # 전처리
    for i in range(len(priorities)):
        indexed_list.append([i, priorities[i]])

    while len(indexed_list) != 0:
        max_value = max(priorities)

        if indexed_list[0][1] == max_value:
            if location == indexed_list[0][0]:
                return result + 1

            indexed_list = indexed_list[1:]
            priorities.remove(max_value)
            result += 1

            if len(priorities) != 0:
                max_value = max(priorities)
        else:
            indexed_list = indexed_list[1:] + [indexed_list[0]]

    return 0

if __name__ == '__main__':
    priorities = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
    location = [2, 0]
    print(solution(priorities[0], location[0]))
    print(solution(priorities[1], location[1]))
