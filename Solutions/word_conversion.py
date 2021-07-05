from collections import deque


def get_adjacent_word(current:str, words:str) -> str:
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for cu, wo in zip(current, word):
            if cu != wo:
                count += 1

        if count == 1:
            yield word


def solution(begin: str, target: str, words: list) -> int:
    word_dict = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()
        adjacent_word_list = get_adjacent_word(current, words)
        for index, adjacent_word in enumerate(adjacent_word_list):
            if adjacent_word not in word_dict:
                word_dict[adjacent_word] = word_dict[current] + 1
                queue.append(adjacent_word)

    print(f'result : {word_dict.get(target)}')


if __name__ == '__main__':
    begin, target = "hit", "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution(begin, target, words)