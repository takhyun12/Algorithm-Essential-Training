## 데이트-백준

* References : [https://www.acmicpc.net/problem/1296](https://www.acmicpc.net/problem/1296)

* 오민식은 자기가 좋아하는 여자 N명 중에 한 명과 함께 데이트하러 나가고 싶어한다.

* 하지만 N명 모두를 사랑하는 오민식에게는 한 명을 선택하고 나머지 여자를 버리는 것은 슬픈 결정이기 때문에 누구를 선택해야 할지 고민에 빠졌다.

* 마침 오민식은 사랑계산기를 얻었다. 사랑계산기는 두 사람의 이름을 이용해서 두 사람이 성공할 확률을 계산해 준다. 사랑계산기는 다음과 같이 작동한다.

* L = 두 사람 이름에서 등장하는 L의 개수
* O = 두 사람 이름에서 등장하는 O의 개수
* V = 두 사람 이름에서 등장하는 V의 개수
* E = 두 사람 이름에서 등장하는 E의 개수

* 위의 개수를 모두 계산 한 후에 확률 계산은 다음과 같이 한다.

* ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) mod 100

* 오민식의 영어 이름과 나머지 여자들의 이름이 주어졌을 때, 오민식과 성공할 확률이 가장 높은 여자의 이름을 출력하는 프로그램을 작성하시오. 
* 여러명일 때에는 알파벳으로 가장 앞서는 이름을 출력하면 된다.

### Solution 1: [Link](https://github.com/takhyun12/Algorithm-Essential-Training/blob/main/Solutions/date.py)

```python
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
```