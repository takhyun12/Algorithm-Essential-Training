from collections import Counter
import math


def solution(a: str, b: str) -> math.floor:
    a_list = list()
    b_list = list()

    for i in range(len(a) - 1):
        if a[i].isalpha() and a[i + 1].isalpha():
            a_list.append((a[i] + a[i + 1]).lower())

    for j in range(len(b) - 1):
        if b[j].isalpha() and b[j + 1].isalpha():
            b_list.append((b[j] + b[j + 1]).lower())

    union = set(a_list) | set(b_list)  # 합집합
    intersection = set(a_list) & set(b_list)  # 교집합

    union_sum = sum([max(a_list.count(u), b_list.count(u)) for u in union])
    intersection_sum = sum([min(a_list.count(i), b_list.count(i)) for i in intersection])

    if len(union) == 0 and len(intersection) == 0:
        return 65536
    else:
        return math.floor((intersection_sum / union_sum) * 65536)


def solution2(a: str, b: str) -> int:
    a_list = list()
    b_list = list()

    for i in range(len(a) - 1):
        if a[i].isalpha() and a[i + 1].isalpha():
            a_list.append((a[i] + a[i + 1]).lower())

    for j in range(len(b) - 1):
        if b[j].isalpha() and b[j + 1].isalpha():
            b_list.append((b[j] + b[j + 1]).lower())

    c1 = Counter(a_list)
    c2 = Counter(b_list)

    union = sum((c1 | c2).values())  # 합집합
    intersection = sum((c1 & c2).values())  # 교집합

    if union == 0 and intersection == 0:
        return 65536
    else:
        return int(intersection / union * 65536)


if __name__ == '__main__':
    case1_list = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
    case2_list = ["french", "shake hands", "AAAA12", "e=m*c^2"]

    for i in range(len(case1_list)):
        print(solution(case1_list[i], case2_list[i]))
        print(solution2(case1_list[i], case2_list[i]))
