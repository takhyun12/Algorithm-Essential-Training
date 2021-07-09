def solution(p):
    answer = ''

    if is_correct(p):
        return p

    while not is_correct(p):
        temp = separate_str(p)

        u = temp[0]
        v = "(" + temp[1] + ")"

        if not is_correct(u):
            u = reverse_str(temp[0][1:-1])
        p = u + v

    return p

def reverse_str(s:str) -> str:
    result = ""
    for i in s:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result

def separate_str(s: str) -> list:
    result = []
    temp = ""
    flag = 0

    for i in s:
        temp += i
        if is_balanced(temp) and flag == 0:
            result.append(temp)
            temp = ""
            flag = 1
    result.append(temp)

    return result

def is_balanced(s: str) -> bool:
    if s.count('(') == s.count(')'):
        return True
    return False

def is_correct(s: str) -> bool:
    while s.count('()') != 0:
        s = s.replace("()", "")
    if len(s) == 0:
        return True
    return False

if __name__ == '__main__':
    cases: list = ["(()())()", ")(", "()))((()"]

    print(solution(cases[0]))
    print(solution(cases[1]))
    print(solution(cases[2]))
