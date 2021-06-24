## IBM 빼기1-백준

* References : https://www.acmicpc.net/problem/6321

* 문자열 입력이 주어졌을 때, 각 글자를 알파벳 다음 순서로 써서 출력하는 프로그램을 작성하시오.


### Condition:

*  Input : 입력될 문자열은 최대 1000글자이며, 반드시 대문자로 받아야 한다. 공백, 특수문자, 숫자는 예외처리를 해야한다.
*  Output : 입력된 문자열의 각 글자를 알파벳 다음 순서로 써서 출력한다. 알파벳 Z의 다음 순서는 A이다.

### Result Sample:
* `HAL` -> `IBM`
* `WERC` -> `TXFSD`

### Test Code:
```python
def solution(s: str) -> str:
    return [str]

if __name__ == '__main__':
    test_cases = ['HAL',
                  'SWERC',
                  'Hal',
                  'DNVNIQRWEHJKFBQWHADOQWDCMVJ' * 10000000]

    for case in test_cases:
        print(solution(case))
```
