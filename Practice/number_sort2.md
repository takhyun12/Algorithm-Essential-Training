## 수 정렬하기2

* References : https://www.acmicpc.net/problem/2751
* N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
* 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

### Solution 1: [Link](https://github.com/takhyun12/Algorithm-Essential-Training/blob/main/Solutions/number_sort2.py)

```python
N = int(input())

nums = []

for i in range(N):
    nums.append(int(input()))

nums = sorted(nums)

for num in nums:
    print(num)
```
