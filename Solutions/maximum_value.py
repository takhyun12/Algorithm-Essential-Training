def solution(sample_list: list) -> (int, int):
    return max(sample_list), sample_list.index(max(sample_list)) + 1


if __name__ == '__main__':
    samples = [3, 29, 38, 12, 57, 74, 40, 85, 61, 1, 111]
    maximum_value, index = solution(samples)
    print(f'maximum_value : {maximum_value}, index : {index}')
