import collections


def solution(skill: str, user_input: list) -> int:
    answer = 0
    for skill_tree in user_input:
        dq = collections.deque(list(skill))
        for s in skill_tree:
            if s in skill and s != dq.popleft():
                break
        else:
            answer += 1

    return answer


if __name__ == '__main__':
    skill = "CBD"
    skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
    solution(skill, skill_tree)
