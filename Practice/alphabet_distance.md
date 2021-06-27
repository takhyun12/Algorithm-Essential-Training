## 알파벳 거리-백준

* References : https://www.acmicpc.net/problem/5218

* 길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리를 구하는 프로그램을 작성하시오.

* 두 글자 x와 y 사이의 알파벳 거리를 구하려면, 먼저 각 알파벳에 숫자를 할당해야 한다. 'A'=1, 'B' = 2, ..., 'Z' = 26. 

* 그 다음 y ≥ x인 경우에는 y-x, y < x인 경우에는 (y+26) - x가 알파벳 거리가 된다.

* 예를 들어, 'B'와 'D' 사이의 거리는 4 - 2 = 2이고, 'D'와 'B' 사이의 거리는 (2+26) - 4 = 24이다.

### Result Case:
```
AAAA ABCD  # 0 1 2 3
ABCD AAAA  # 0 25 24 23
DARK LOKI  # 8 14 19 24
STRONG THANOS  # 1 14 9 25 1 12
DEADLY ULTIMO  # 17 7 19 5 1 16
```

### Test Code:
```python
def solution(?: ???) -> ???:
    # input your code
    return ???

if __name__ == '__main__':
    test_case: list = ["AAAA ABCD", "ABCD AAAA", "DARK LOKI", "STRONG THANOS", "DEADLY ULTIMO"]
    # input your code
```

### Solution : [바로가기](https://github.com/takhyun12/Algorithm-Essential-Training/blob/main/Solutions/magic_mirror.py)
