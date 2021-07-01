def solution(s: str) -> int:
    dp: list = [] # saves all possible length of compressed strings

    if len(set(s)) == 1: # if only contains one char
        if len(s) == 1:
            return 1
        else:
            return 2

    for i in range(len(s)):
        if i != 0:
            temp = split_list(s, i)
            dp.append(start_compression(temp))

    return min(dp)

def split_list(s: str, n: int) -> str: # split list into n elements
    return [s[i:i+n] for i in range(0, len(s), n)]

def start_compression(s: list) -> int: # return lengths of compressed string
    '''
    데이터 1차 가공(분류)
    '''
    result_str: str = ""
    result: list = []
    previous_index: int = 0

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            result.append(s[previous_index:i+1])
            previous_index = i+1

    result.append(s[previous_index:])

    '''
    데이터 2차 가공(압축)
    '''
    for i in result:
        if len(i) == 1:
            result_str += i[0]
        else:
            result_str += str(len(i)) + i[0]

    return len(result_str)

if __name__ == '__main__':
    input_list: list = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd",
                        "acacacbacacac", "acacacacacacbacacacacacac", "a" * 100, "xxxxxxxxxxyyy"]
    for i in input_list:
        print(solution(i))
