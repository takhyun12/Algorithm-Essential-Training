def solution(s: str) -> str:
    result: str = ""
    length: int = len(s) - 4

    return ('*'*length) + s[-4:]

if __name__ == '__main__':
    sample_list = ["01033334444", "027778888"]

    for i in range(len(sample_list)):
        print(solution(sample_list[i]))
    # input your code
