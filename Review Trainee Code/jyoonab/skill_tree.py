def solution(s: str, arr: list) -> int:
    temp = []
    result = 0

    for i in arr:
        for j in i:
            if j in s:
                temp.append(j)
                temp_str = ''.join(temp)

                if not ((temp_str in s) and (temp_str[0] == s[0])):
                    result -=1
                    break
        result += 1
        temp = []

    return result

if __name__ == '__main__':
    skill = "CBD"
    skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]

    print(solution(skill, skill_tree))
