## 타겟 넘버-프로그래머스

* References : https://programmers.co.kr/learn/courses/30/lessons/43165

### Description

* n개의 음이 아닌 정수가 있습니다. 
* 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
* 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```
* 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때,
* 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

### Restrictions:

* 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
* 각 숫자는 1 이상 50 이하인 자연수입니다.
* 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

### Result Case:

| numbers | target | output |
|---|---|---|
| [1, 1, 1, 1, 1]	 | 3 | 5 |

### Test Code:
```python
def solution(?: ???) -> ???:
    # input your code
    return ???

if __name__ == '__main__':
    numbers: list = [1, 1, 1, 1, 1]
    target: int = 3
    # input your code
```

### Solution : [바로가기](https://github.com/takhyun12/Algorithm-Essential-Training/blob/main/Solutions/si.py)
