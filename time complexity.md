## Referencse
* [Time complexity in Python](https://github.com/takhyun12/Python-Essential-Training/blob/main/time%20complexity.md)

## Time Complexity

### 점근적 표기법(Asymptotic natation)
* 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

* Example 1:

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        print(1)
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```
