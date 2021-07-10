def solution(s: list) -> list:
    solution = []

    for i in s:
        temp = i.split()
        if(temp[1] == 'enter'):
            solution.append(temp[0])
        elif(temp[1] == 'leave'):
            solution.remove(temp[0])

    return solution

if __name__ == '__main__':
    arr: list = ["Baha enter", "Askar enter", "Baha leave", "Artem enter"]
    print(solution(arr))
