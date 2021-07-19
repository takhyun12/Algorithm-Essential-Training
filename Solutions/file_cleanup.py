from collections import Counter


def solution(file_list: list) -> list:
    extension_list = list()
    for file in file_list:
        file_name, file_extension = file.split('.')
        extension_list.append(file_extension)

    c1 = Counter(extension_list)  # List -> Counter
    c1 = sorted(c1.items())  # Counter -> List

    for key, value in c1:
        print(key, value)


if __name__ == '__main__':
    files = ["sbrus.txt", "spc.spc", "acm.icpc", "korea.icpc", "sample.txt", "hello.world", "sogang.spc", "example.txt"]
    solution(files)