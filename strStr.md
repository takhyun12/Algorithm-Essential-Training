## Implement strStr()
* Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

* Answer Case

```
haystack = "hello", needle = "ll"  -> Output: 2
```

```
haystack = "aaaaa", needle = "bba"  -> Output: -1
```

### Solution
```python
def strStr(haystack: str, needle: str) -> int:
    # null check
    if (haystack == "" and needle == "") or needle == "":
        return 0
    elif haystack == "":
        return -1

    split_result = haystack.split(needle)
    if split_result[0] == haystack:
        return -1
    elif split_result[0] != haystack:
        return len(split_result[0])
```
```python
def strStr2(haystack: str, needle: str) -> int:
    return haystack.find(needle)
```
```python
def strStr3(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    elif needle in haystack:
        return haystack.index(needle)
    else:
        return -1
```
```python
def strStr4(haystack: str, needle: str) -> int:
    m, n = len(needle), len(haystack)
    for i in range(n - m + 1):
        for j in range(m):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i
    return -1
```

### Performance Comparison:
* Test case
```python
n = "ME3"
h = ("AM2CIK4DJCED" * 13312444) + n + ("KDM1EKE" * 100)
```

* Result summary

| Methods | Call count | Call method | Time | 
|---|---|---|---|
| strStr | 2 | split, len | 49ms | 
| strStr2 | 1 | find | 26ms | 
| strStr3 | 1 | index | 53ms | 
| strStr4 | 1 | len | 31042ms | 

![strStr](https://user-images.githubusercontent.com/41291493/123195005-65c46800-d4e2-11eb-9631-686d6ab07852.png)

☕ 더 빠른 알고리즘을 알려주신분께는 Coffee를 사드립니다. (카카오톡 선물하기)
