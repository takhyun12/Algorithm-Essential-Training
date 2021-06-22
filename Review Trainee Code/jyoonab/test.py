'''
문제: https://github.com/takhyun12/Algorithm-Essential-Training/blob/main/Practice/resistance.md
'''
def solution(resistance_dict: dict, color_list: list) -> int:
    # You can put your code in here
    return [int]

if __name__ == '__main__':
    resistance_dict = {"black": [0, 1],
                       "brown": [1, 10],
                       "red": [2, 100],
                       "orange": [3, 1000],
                       "yellow": [4, 10000],
                       "green": [5, 100000],
                       "blue": [6, 1000000],
                       "violet": [7, 10000000],
                       "grey": [8, 100000000],
                       "white": [9, 1000000000]}

    color_list = ["yellow", "violet", "red"]
    resistance_score = solution(resistance_dict, color_list)
    print(resistance_score)  # 4700

    color_list2 = ["white", "orange", "grey"]
    resistance_score = solution(resistance_dict, color_list2)
    print(resistance_score)  # 9300000000

    color_list3 = ["green", "white", "brown"]
    resistance_score = solution(resistance_dict, color_list3)
    print(resistance_score)  # 590
