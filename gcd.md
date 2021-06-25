## 최대공약수와 최대공배수

* Example 1:

```python
# 유클리드 호제법을 이용하여 최대 공약수를 구함
def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)

    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)

    return n1


# 최소 공배수는 n과 m을 곱한후 최대 공약수로 나누어 준다
def solution(n, m):
    answer = [gcd(n, m), (n * m) / gcd(n, m)]
    return answer
```

* Example 2:

```python
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))


def gcdlcm(a, b):
    answer = [gcd(a,b), lcm(a,b)]
    return answer
```

* Example 3:


```python
from fractions import gcd 
def solution(n, m):
    answer = [gcd(n, m), n*m / gcd(n, m)]
    return answer
```
