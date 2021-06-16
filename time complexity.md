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

#### O(1) (Constant)
* 입력 데이터의 크기에 상관없이 언제나 일정한 시간이 걸리는 알고리즘을 나타냅니다. (오직 1단계)
* 데이터가 얼마나 증가하든 성능에 영향을 거의 미치지 않습니다. 

```python
print('hello')
```

#### O(log n) (Logarithmic)
* 입력 데이터의 크기가 커질수록 처리 시간이 로그만큼 짧아지는 알고리즘입니다. (연산마다 특정요인에 의해 줄어듬)
* 데이터가 10배가 되면, 처리 시간은 2배가 됩니다. 
* 예시) 이진 탐색, 재귀가 순기능으로 이루어지는 경우

```python
def binary_search(li, item, first=0, last=None):
    if not last:
        last = len(li)

    midpoint = (last - first) / 2 + first

    if li[midpoint] == item:
        return midpoint

    elif li[midpoint] > item:
        return binary_search(li, item, first, midpoint)

    else:
        return binary_search(li, item, midpoint, last)
```

#### O(n) (Linear)
* 입력 데이터의 크기에 비례해 처리 시간이 증가하는 알고리즘입니다. (단계수와 입력값이 1:1)
* 데이터가 10배가 되면, 처리 시간도 10배가 됩니다. 
* 예시) 1차원 for문

```python
for item in list:
    print(item)
}
```

* 반복문이 따로 2개 있는 경우도 하나의 알고리즘을 대상으로 Big-O Notation을 적용한다

```python
for item in list:
    print(item)
}

for item in list:
    print(item)
}
```

#### O(n log n) (Linear-Logarithmic)
* 데이터가 많아질수록 처리시간이 로그(log) 배만큼 더 늘어나는 알고리즘입니다. (N*(log2N))
* 데이터가 10배가 되면, 처리 시간은 약 20배가 된다. 
* 예시) 병합 정렬, 퀵 정렬

#### O(n²) (quadratic)
* 데이터가 많아질수록 처리시간이 급수적으로 늘어나는 알고리즘입니다. (입력값 n의 제곱)
* 데이터가 10배가 되면, 처리 시간은 최대 100배가 됩니다. 
* 예시) 이중 루프(n² matrix)

```python

def print_each_n_times(li):
    for n in li:
        for m in li:
            print(n, m)
```


#### O(Cⁿ) (Exponential)
* 데이터량이 많아질수록 처리시간이 기하급수적으로 늘어나는 알고리즘입니다. (상수값 C 의 n 제곱)
* 예시) 피보나치 수열, 재귀가 역기능을 할 경우

### 간단한 최적화 예시

* Example 1: O(n^3) -> O(n^2)

```python
def disjoint(A, B, C):
    for a in A: 
        for b in B:
            for c in C: 
                if a == b == c:
                    return False 
    return True
```

* 원리: 바깥쪽 2개의 loop 는 반드시 실행이 되지만, 안쪽 loop 는 a==b 라는 조건을 만족시켰을 때만 실행이 됨

```python
def improved_disjoint(A, B, C): 
    for a in A: 
        for b in B: 
            if a == b: 
                for c in C: 
                    if a == c: 
                        return False 
    return True
```

