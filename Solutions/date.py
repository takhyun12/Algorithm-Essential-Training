import operator


def function(x):
    return -x[0], x[1]


def solution(minsik_name: str, girls_list: list) -> str:
    score_dict = []
    for index, girl_name in enumerate(girls_list):
        L = minsik_name.upper().count('L') + girl_name.upper().count('L')
        O = minsik_name.upper().count('O') + girl_name.upper().count('O')
        V = minsik_name.upper().count('V') + girl_name.upper().count('V')
        E = minsik_name.upper().count('E') + girl_name.upper().count('E')

        score = ((L + O) + (L + V) + (L + E) + (O + V) + (O + E) + (V + E)) % 100
        score_dict.append((score, girl_name))
    score_dict.sort(key=function)
    return score_dict[0][1]


if __name__ == '__main__':
    minsik_name = 'OHMINSIK'
    girls_list = ['TAEYEON', 'TIFFANY', 'YURI', 'HYOYEON', 'SOOYOUNG', 'SEOHYUN', 'YOONA', 'JESSICA', 'SUNNY']
    sweetheart = solution(minsik_name, girls_list)
    print(sweetheart)
