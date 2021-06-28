def solution(s: str) -> int:
    result_word_list = list()
    result_word = ""

    # 예외처리
    if len(s) == 1 or len(s) > 1000:
        return len(s)

    for tokken_len in range(1, len(s) // 2 + 1):
        tokken_count = 1
        tokken = s[:tokken_len]

        for i in range(tokken_len, len(s), tokken_len):
            if s[i:i+tokken_len] == tokken:
                tokken_count += 1
            else:
                if tokken_count == 1:
                    tokken_count = ""

                result_word += str(tokken_count) + tokken
                tokken = s[i:i+tokken_len]
                tokken_count = 1

        if tokken_count == 1:
            tokken_count = ""

        result_word += str(tokken_count) + tokken
        result_word_list.append(result_word)
        result_word = ""

    print(result_word_list)
    return min(map(len, result_word_list))

def solution2(s: str) -> int:
    result_word_list = list()
    result_word_list.append(s)
    result_word = ""

    for tokken_len in range(1, int(len(s) // 2) + 1):
        tokken_list = [s[i:i + tokken_len] for i in range(0, len(s), tokken_len)]
        tokken_dict = dict()

        # 토큰의 갯수를 세아림
        for index in range(len(tokken_list) - 1):
            if tokken_list[index] == tokken_list[index + 1]:
                if tokken_list[index] not in tokken_dict:
                    tokken_dict[tokken_list[index]] = 2
                else:
                    tokken_dict[tokken_list[index]] += 1

        # 딕셔너리가 비어있지 않으면
        skip_step = 0

        if tokken_dict:
            for j in range(len(tokken_list)):
                if skip_step > 0:
                    skip_step -= 1
                    continue

                if tokken_list[j] in tokken_dict:
                    result_word += str(tokken_dict[tokken_list[j]]) + tokken_list[j]
                    skip_step = (tokken_dict[tokken_list[j]] - 1)
                    del tokken_dict[tokken_list[j]]
                else:
                    result_word += tokken_list[j]

            result_word_list.append(result_word)

    # return result
    print(result_word_list)
    return min(map(len, result_word_list))

if __name__ == '__main__':
    input_list: list = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd",
                        "acacacbacacac", "acacacacacacbacacacacacac", "a" * 100, "xxxxxxxxxxyyy"]
    # 10x3y
    # test = "abcabcdede"
    # print(f'result = {solution(test)}')
    for input_value in input_list:
        print(len(input_value))
        print(f'result = {solution(input_value)}')
        print('')
