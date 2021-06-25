def solution(phone_number: str) -> str:
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == '__main__':
    sample_list = ["01033334444", "027778888"]
    for sample in sample_list:
        print(solution(sample))

