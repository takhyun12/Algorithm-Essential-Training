## 저항(Resistance)-백준

* References : https://www.acmicpc.net/problem/1076

* 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다.

* 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.

* 저항의 값은 다음 표를 이용해서 구한다.

![table](https://user-images.githubusercontent.com/41291493/122884356-04cd5080-d379-11eb-9820-d48cf8180d9c.png)

예를 들어, 저항에 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.

### Test
```python
def solution(resistance_dict: dict, color_list: list) -> int:
    # You can put your code in here
    print(resistance_dict)
    print(color_list)
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
    print(resistance_score)
```
