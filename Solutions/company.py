def solution(arr: list):
    log_dict = dict()
    for access_log in arr:
        name, action = access_log.split()
        if action == "enter":
            log_dict[name] = action
        elif action == "leave":
            del(log_dict[name])

    print(list(log_dict.keys()))

if __name__ == '__main__':
    samples: list = ["Baha enter", "Askar enter", "Baha leave", "Artem enter"]
    solution(samples)