## Implement factorial()

### Basic Factorial
* 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

* Example 1:

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```

### Factorial 0의 갯수
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
        
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    fact_list = list(str(factorial))
    fact_list_len = len(fact_list)
        
    count = 0
    for i in range(len(fact_list)):
        if fact_list[fact_list_len - 1 - i] != '0':
            break
        elif fact_list[fact_list_len - 1 - i] == '0':
            count += 1
                
    return count
```
