def solution(number_list: str, k: int) -> str:
    stack = []
    for number in number_list:
        while len(stack) > 0 and stack[-1] < number and k > 0:
            stack.pop()
            k -= 1
        stack.append(number)

    if k > 0:
        return ''.join(stack[:-k])
    else:
        return ''.join(stack)


if __name__ == '__main__':
    n_array = ["1924", "1231234", "4177252841", "77777"]
    k_array = [2, 3, 4, 1]
    print(solution(n_array[0], k_array[0]))
