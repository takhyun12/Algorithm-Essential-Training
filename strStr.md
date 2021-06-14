## Implement strStr()
* Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

* Example 1:

```
Input: haystack = "hello", needle = "ll" Output: 2
```

* Example 2:

```
Input: haystack = "aaaaa", needle = "bba" Output: -1
```

* Solution
```python
# haystack : Target word
# needle : Word you want to find

class Solution:
    @staticmethod
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


test_cases = {
    'hello my name is Tackhyun Jung': 'ky',
    'aaaaaaaaaaaaaaa': 'bb',
    'aaaa': 'aa',
    'testtesttestking': 'ng'
}

for haystack, needle in test_cases.items():
    result = Solution().strStr(haystack, needle)
    print(f"key:{haystack}, value:{needle}, result:{result}")
    
# Output
# key:hello my name is Tackhyun Jung, value:ky, result:-1
# key:aaaaaaaaaaaaaaa, value:bb, result:-1
# key:aaaa, value:aa, result:0
# key:testtesttestking, value:ng, result:14
```
