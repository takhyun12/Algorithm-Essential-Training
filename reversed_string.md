## Implement revesed()
* 입력된 문자열을 거꾸로 뒤집어 리턴하는 코드를 작성하시오.

### Restrictions:
* len(s) / 2 의 Time complexity 구현하시오.


### Solution:

* 정석적인 방법:
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
s_list.revese()

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
