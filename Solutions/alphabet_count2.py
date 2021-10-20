import re


def solution(input_list: list) -> list:
    result_list = list()
    for sentence in input_list:
        filtered_sentence = re.sub(r"[^a-z]", '', sentence.lower())
        alphabet_list = list(set(filtered_sentence))
        result_list.append(len(alphabet_list))
        
    return result_list


if __name__ == '__main__':
    input_list = ["The quick brown fox jumped over the lazy dogs.", "New Zealand Programming Contest.", "get_word_nums"]
    result_list = solution(input_list)
    print(result_list)