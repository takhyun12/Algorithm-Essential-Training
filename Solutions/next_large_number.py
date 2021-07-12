def solution(n: int) -> int:
    n_binary = bin(n)[:1:-1] + '0'
    zero_count = n_binary.find('1')
    one_count = n_binary[zero_count:].find('0')
    return int(n_binary[:zero_count + one_count:-1] + '10' + '0' * zero_count + '1' * (one_count-1), 2)


def solution2(n: int) -> int:
    """ 반복이 많아서 효율성 테스트를 넘지 못함 """
    result = 0
    n_one_count = bin(n).count("1")
    for m in range(n+1, 2*n+1):
        m_one_count = bin(m).count("1")
        if n_one_count == m_one_count:
            result = m
            break

    return result


if __name__ == '__main__':
    n_list = [78, 15]
    print(solution2(n_list[0]))
