import math

def solution(citations):
    sorted_list = sorted(citations, reverse=True)

    for i in range(len(sorted_list)):
        if sorted_list[i] == i+1:
            return i+1
        elif sorted_list[i] <= i+1:
            return i

    return len(sorted_list)

if __name__ == '__main__':
    citations: list = [3, 0, 6, 1, 5]
    print(solution(citations))
