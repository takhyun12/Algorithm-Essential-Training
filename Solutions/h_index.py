def solution(citation_list: list) -> int:
    citation_list.sort(reverse=True)
    return max(map(min, enumerate(citation_list, start=1)))

if __name__ == '__main__':
    citations: list = [3, 0, 6, 1, 5]
    print(solution(citations))