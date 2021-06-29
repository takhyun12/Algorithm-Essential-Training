def solution(a: str, b: str) -> int:
    a_split = split_list(''.join(filter(str.isalpha, a)).upper())
    b_split = split_list(''.join(filter(str.isalpha, b)).upper())

    union = set(a_split) | set(b_split)
    intersection = set(a_split) & set(b_split)

    print(intersection)
    print(union)

    print(len(intersection)/len(union))

    return int(65536*(len(intersection)/len(union)))

def split_list(a: str) -> list:
    result = []
    for i in range(len(a)-1):
        result.append(a[i:i+2])
    return result

if __name__ == '__main__':
    case1_list = ["FRANCE", "handshake", "aa1aa2", "E=M*C^2"]
    case2_list = ["french", "shake hands", "AAAA12", "e=m*c^2"]

    for i in range(len(case1_list)):
        print(solution(str(case1_list[i]), str(case2_list[i])))
