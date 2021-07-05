"""
가장 큰수를 줄여나가는 방식으로 평균치를 낮춰서 제곱의 덧셈 연산의 평균을 줄여나가는것이 포인트
sort 를 하게되면 time_complexity 해결할 수 없도록 설계되어 있어서, min heap 을 사용하게 되었다.
"""

import heapq


def solution(tasks: list, n: int) -> int:
    # 전체 task 의 합 보다 잔여시간이 크면 야근을 할 필요가 없음
    if sum(tasks) < n:
        return 0

    # 모든 task 를 음수로 바꿈
    tasks = [-value for value in tasks]

    # list 를 heap 으로 변환
    heapq.heapify(tasks)

    # 가장 작은 값을 pop 해서 +1 한뒤 다시 넣음
    for i in range(n):
        heapq.heappush(tasks, heapq.heappop(tasks) + 1)
        i += 1
        
    # 계산된 결과의 제곱을 더해서 리턴
    return sum([value**2 for value in tasks])


if __name__ == '__main__':
    works = [4, 3, 3]
    n = 4
    print(solution(works, n))