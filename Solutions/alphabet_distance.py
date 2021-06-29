def solution(a: str, b: str) -> str:
    distance_list = list()
    for i in range(len(a)):
        a_ord, b_ord = ord(a[i]), ord(b[i])
        if a_ord <= b_ord:
            distance_list.append(str(b_ord - a_ord))
        else:
            distance_list.append(str((b_ord + 26) - a_ord))

    return ' '.join(distance_list)

if __name__ == '__main__':
    test_case: list = ["AAAA ABCD", "ABCD AAAA", "DARK LOKI", "STRONG THANOS", "DEADLY ULTIMO"]
    for case in test_case:
        a, b = case.split()
        result = solution(a, b)
        print(result)

