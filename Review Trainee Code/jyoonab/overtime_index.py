import heapq

def solution(n:int, works:list) -> int:
    result = 0
    total = 0
    heap = []

    for i in works:
        heapq.heappush(heap, -i)
        total += i

    if (total - n) <= 0:
        return 0

    for i in range(n):
        temp = heap[0] + 1
        heapq.heappop(heap)
        heapq.heappush(heap, temp)

    return sum([i**2 for i in heap])

if __name__ == '__main__':
    works = [4, 3, 3]
    n = 4
    print(solution(n, works))
