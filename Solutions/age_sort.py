def solution(arr: list) -> list:
    if len(arr) <= 0 or len(arr) > 15:
        raise Exception('입력이 잘못되었습니다.')

    user_data_dict = dict()
    for value in arr:
        age, name = value.split()
        print(f"[Source] age: {age}, name: {name}")

        if name not in user_data_dict:
            user_data_dict[name] = int(age)

    print("")

    sorted_dict = dict(sorted(user_data_dict.items(), key=lambda item: item[1]))
    for key, value in sorted_dict.items():
        print(f"[Result] age: {value}, name: {key}")


if __name__ == '__main__':
    test_case1: list = ["21 Junkyu", "21 Dohyun", "20 Sunyoung"]
    solution(test_case1)