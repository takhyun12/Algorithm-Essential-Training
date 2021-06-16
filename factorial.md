## Implement factorial()

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
