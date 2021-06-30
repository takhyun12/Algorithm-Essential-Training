def solution(l: list) -> list:
    result = []
    final_result = []
    dict = {}

    # 전처리
    for i in l:
        split_str = i.split()

        if(split_str[0] == "Enter"):
            dict[split_str[1]] = split_str[2]
            result.append(["Enter", split_str[1]])
        elif(split_str[0] == "Leave"):
            result.append(["Leave", split_str[1]])
        elif(split_str[0] == "Change"):
            dict[split_str[1]] = split_str[2]

    # 가공
    for i in result:
        if i[0] == "Enter":
            final_result.append(dict[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            final_result.append(dict[i[1]] + "님이 나갔습니다.")
            
    return final_result

if __name__ == '__main__':
    log: list = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    print(solution(log))
