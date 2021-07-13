def solution(n: int, times: list) -> int:
    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        total = 0

        for time in times:
            total += mid // time

        if total >= n:
            right = mid
        else:
            left = mid + 1
            
    return left


if __name__ == '__main__':
    n = 6
    times = [7, 10]
    solution(n, times)