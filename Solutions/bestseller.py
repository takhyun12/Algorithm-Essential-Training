from collections import Counter


def solution(book_list: list) -> str:
    book_counter = Counter(book_list)

    max_number = max(book_counter.values())
    best_seller_list = [book[0] for book in book_counter.items() if book[1] == max_number]
    best_seller = sorted(best_seller_list)[0]

    return best_seller


if __name__ == '__main__':
    input_list = ["top", "top", "abc", "abc", "kimtop"]
    result = solution(input_list)
    print(result)
