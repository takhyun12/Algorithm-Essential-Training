'''import itertools

def solution(s: list) -> str:
    all_possible_input = list(itertools.permutations(s))
    all_possible_result = []

    for i in all_possible_input:
        sub_result = ""
        for j in i:
            sub_result += str(j)
        all_possible_result.append(int(sub_result))

    print(all_possible_result)

    return str(max(all_possible_result))'''

'''
def solution(s: list) -> str:
    result = ""
    processed = []
    bigest_place = len(str(max(s)))

    s.sort()

    for i in s:
        processed.append([i, multi(str(i), bigest_place)])

    print(processed)
    processed = sorted(processed, key=lambda x: x[1], reverse=True)
    print(processed)

    for i in processed:
        result += str(i[0])

    return result

def multi(s: str, n: int) -> int:
    return int(s + ('0' * (n-len(s))))
'''

def solution(numbers):
    numbers = [ str(x) for x in numbers ]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = "".join(numbers) if numbers[0] != "0" else "0"
    return answer


if __name__ == '__main__':
    test_case1: list = [6, 10, 2]
    test_case2: list = [3, 30, 34, 5, 9]
    test_case3: list = [1, 100, 10100, 100]

    print(solution(test_case1))
    print(solution(test_case2))
    print(solution(test_case3))
