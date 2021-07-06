import collections


def solution(arr: list, target: int) -> int:
    location = 0
    deq = collections.deque([(value, index) for index, value in enumerate(arr)])

    while len(deq) != 0:
        pop_value = deq.popleft()
        if deq and pop_value[0] < max(deq)[0]:
            deq.append(pop_value)
        else:
            location += 1
            if pop_value[1] == target:
                break

    return location


if __name__ == '__main__':
    p = [2, 1, 3, 2]
    l = 2
    print(solution(p, l))