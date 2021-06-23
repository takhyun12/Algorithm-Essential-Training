def solution(s: str) -> int:
    # You can put your code in here

    MAX_NUM = 2015
    add_num = 0

    #if len(s) < 1 or len(s) > 1000:
        #return -1

    simplified_list = list(dict.fromkeys(sorted(s)))

    for i in simplified_list:
        #if (ord(i) > 90 or ord(i) < 65):
        #    return -1
        add_num += ord(i)

    return MAX_NUM - add_num


if __name__ == '__main__':
    cases = ["ABCDEFGHIJKLMNOPQRSTUVW", "A", "BDCW", "K", "", 554342389243782437823478243872348234,
    "CCBBAA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for case in cases:
        result: int = solution(str(case))
        print(result)
