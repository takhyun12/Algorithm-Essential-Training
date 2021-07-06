## 신용카드 판별-백준

* References : https://www.acmicpc.net/problem/14726

### Description

* 신용카드는 총 16자리의 숫자로 구성되어 있다. 

* 언뜻 보기에는 무작위로 된 숫자로 구성되어 있는 것 같이 보이지만 그 속에는 하나의 수학적 비밀이 숨겨져 있다. 

* 그중 하나가 카드 번호가 유효 한지 유효하지 않은 지 검사하는 Luhn 공식이다. 그 공식은 다음과 같다.

```
1. 신용카드의 16자리 숫자에서 맨 우측 수부터 세어 홀수 번째 수는 그대로 두고, 짝수 번째 수를 2배로 만든다.

2. 2배로 만든 짝수 번째 수가 10 이상인 경우, 각 자리의 숫자를 더하고 그 수로 대체한다.

3. 이와 같이 얻은 모든 자리의 수를 더한다.

4. 그 합이 10으로 나뉘면 “정당한 번호”(유효)이고 그렇지 않으면 “부당한 번호”(유효하지 않음)로 판정된다.
```

다음 공식을 이용해 주어진 신용카드의 번호가 유효한지, 유효하지 않은 지 판단해라.

### Restrictions:

* 입력값은 16자리의 정수형 숫자이다.

### Result Case:

| Input | Output |
|---|---|
| 2720992711828767 | True |
| 3444063910462763 | False |
| 6011733895106094 | True |


### Test Code:
```python
def solution(?: ???) -> ???:
    # input your code
    return ???

if __name__ == '__main__':
    arr = [2720992711828767, 3444063910462763, 6011733895106094]
    # input your code
```

### Solution : [바로가기](https://github.com/takhyun12/Algorithm-Essential-Training/blob/main/Solutions/printer.py)
