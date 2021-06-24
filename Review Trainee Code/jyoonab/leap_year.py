def solution(year):
    if type(year) != int:
        return 0
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    return 0

if __name__ == '__main__':
    year = int(input())
    print(solution(year))
