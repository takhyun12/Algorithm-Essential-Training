def solution(citation_list: list) -> int:
    citation_list.sort(reverse=True) 
    return max(map(min, enumerate(citation_list, start=1)))  # start=0 시, 가장 큰수가 min 연산에 미포함 됨 

if __name__ == '__main__':
    citations: list = [3, 0, 6, 1, 5]
    print(solution(citations))
