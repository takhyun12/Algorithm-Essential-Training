def solution(sample_list: list) -> dict:
    result: dict = {}
    max_num: int = max(sample_list)
    position_num: int = sample_list.index(max_num)
    result["maximum value"] = max_num
    result["index"] = position_num+1

    return result

if __name__ == '__main__':
    sample_list = [3, 29, 38, 12, 57, 74, 40, 85, 61]
    print(solution(sample_list))
