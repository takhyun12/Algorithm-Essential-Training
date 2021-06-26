# 마법거울의 심리상태가 1일 때는 지영 공주님의 모습을 있는 그대로 표현하고,
# 2일 때는 좌/우로 반전된 모습을, 3일 때는 상/하로 반전된 모습을 표현한다.

def solution(mirror_list: list, mood: int) -> list:
    if len(mirror_list) == 0 or (mood == 0 or mood >= 4):
        raise Exception("입력이 잘못되었습니다.")

    if mood == 1:
        return mirror_list
    elif mood == 2:
        for i in range(len(mirror_list)):
            mirror_list[i] = mirror_list[i][::-1]
        return mirror_list
    elif mood == 3:
        return mirror_list[::-1]


if __name__ == '__main__':
    input_data: list = ["OOOOOOOO", "OKKOOEEO", "OKKOOEEO", "OOOSSOOO", "OOOSSOOO", "OAOOOOAO", "OOAAAAOO", "OOOOOOOO"]
    print(f'original : {input_data}')
    mood: int = 3
    mirror_list = solution(input_data, mood)
    print(f'mirror_list : {mirror_list}')
