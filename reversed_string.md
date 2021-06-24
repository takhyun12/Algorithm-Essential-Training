## Implement revesed()
* 입력된 문자열을 거꾸로 뒤집어 리턴하는 코드를 작성하시오.

### Restrictions:
* len(s) / 2 의 Time complexity 구현하시오.


### Solution:

* 알고리즘적인 방법:
```python
def solution(s: str) -> str:                                                                                
    reversed_list = list(s)                                                                                 
    start, fin = 0, len(s) - 1                                                                              
    while start < fin:                                                                                      
        reversed_list[start], reversed_list[fin] = reversed_list[fin], reversed_list[start]                 
        start += 1                                                                                          
        fin -= 1                                                                                            
    return ''.join(reversed_list)                                                                           
```

* Python Style:

```python
s = 'abcde'
s_list = list(s)
s_list.reverse()

print(''.join(s_list))
```

```python
s = 'abcde'
print(''.join(reversed(s)))
```

```python
s = 'abcde'
print(s[::-1])
```

* 응용방안 : 3번 인덱스 부터 0번 인덱스 까지만 역순으로 출력

```python
s = 'abcde'
print(s[3::-1])
```

### Performance Comparison:

```python
test_case = "Feel so Good!" * 1000000
```


```python
def solution(s: str) -> str:
    reversed_list = list(s)
    start, fin = 0, len(s) - 1
    while start < fin:
        reversed_list[start], reversed_list[fin] = reversed_list[fin], reversed_list[start]
        start += 1
        fin -= 1
    return ''.join(reversed_list)  # average: 647ms


def solution2(s: str) -> str:
    s_list = list(s)
    s_list.reverse()
    return ''.join(s_list)  # average: 134ms


def solution3(s: str) -> str:
    return s[::-1]   # average: 13ms
```

* 실험결과 Solution3의 방법이 join 등 다른 메소드를 사용하지 않아 압도적으로 높은 성능을 보였다

![reverse_string](https://user-images.githubusercontent.com/41291493/123187683-92be4e00-d4d5-11eb-9c16-f93c7ce1cabe.png)



