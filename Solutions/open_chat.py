def solution(log_list: list) -> list:
    user_dict = dict()
    for log in log_list:
        log_split = log.split(' ')
        if log_split[0] in ["Enter", "Change"]:
            user_dict[log_split[1]] = log_split[2]

    result_list = list()
    for log in log_list:
        log_split = log.split()
        if "Enter" == log_split[0]:
            result_list.append(f"{user_dict[log_split[1]]}님이 들어왔습니다.")
        elif "Leave" == log_split[0]:
            result_list.append(f"{user_dict[log_split[1]]}님이 나갔습니다.")
    return result_list


def solution2(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]


if __name__ == '__main__':
    input_list: list = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    output_list = solution(input_list)
    print(output_list)