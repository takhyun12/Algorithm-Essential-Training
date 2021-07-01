def reverseStr(p: str) -> str:
    ans = ""
    for s in p:
        if s == "(":
            ans += ")"
        else:
            ans += "("
    return ans


def seperate(p: str) -> [str, str]:
    u, v = p, ""
    for i in range(2, len(p), 2):
        if p[:i].count('(') == p[:i].count(')'):
            u = p[:i]
            v = p[i:]
            break
    return u, v


def isCorrect(p: str) -> bool:
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0


def solution(p: str):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if p == '':
        return p

    # 2. 문자열 w를 두 "균형잡인 괄호 문자열" u, v로 분리합니다.
    u, v = seperate(p)

    # 3. 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계 부터 다시 수행합니다.
    if isCorrect(u):
        u += solution(v)
        return u

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        new_word = "("  # 4.1 빈 문자열에 첫 번째 문자로 '("를 붙힙니다
        new_word += solution(v)  # 4.2 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과의 문자열을 이어 붙힙니다.
        new_word += ")"  # 4.3 ')'를 이어붙힙니다.

        if len(u) > 0:
            new_word += reverseStr(u[1:-1])
        return new_word


if __name__ == '__main__':
    cases: list = ["(()())()", ")(", "()))((()"]
    result = solution(cases[1])
    print(f"result: '{result}'")
