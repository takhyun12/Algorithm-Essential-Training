## Referencse
* [Time complexity in Python](https://github.com/takhyun12/Python-Essential-Training/blob/main/time%20complexity.md)

## Time Complexity

### 점근적 표기법(Asymptotic natation)
* 최상의 시간복잡도 : 오메가 표기법 (Big-Ω Notation)
* 평균 시간복잡도 : 세타 표기법 (Big-θ Notation)
* 최악의 시간복잡도 : 빅오 표기법 (Big-O Notation)

### 빅오 표기법 (Big-O Notation)
* 시간복잡도는 입력된 N의 크기에 따라 실행되는 조작의 수를 나타낸다
* 공간복잡도는 알고리즘이 실행될때 사용하는 메모리의 양을 나타낸다


![big o](https://user-images.githubusercontent.com/41291493/122162870-3b095c80-ceaf-11eb-83f8-e61c7a058ecb.png)


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
