### Implement strStr().
* Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


```java
// Java
int[] arr1 = {1,2,3};
int[] arr2 = {4,5,6};

int arr1Length = arr1.length;
int arr2Length = arr2.length;

int[] resultArray = Array.copyOf(arr1, arr1Length + arr2Length);
System.arrayCopy(arr2, 0, resultArray, arr1Length, arr2Length);  
```
